#!/usr/bin/env python

import multiprocessing
from datetime import datetime
import argparse
import socket
import select
import time
import ssl
import sys
import os


MAX_BUFF = 0x1000
STDIO_MUTEX = multiprocessing.Lock()
SOCKET_MUTEX = multiprocessing.Lock()
EXITING = False


# Helper function to send messages
def sender(s, stdin_fileno, stdout_fileno):
    global EXITING
    # We re-open stdin here, so we can use raw_input inside a child process.
    sys.stdin = os.fdopen(stdin_fileno)
    sys.stdout = os.fdopen(stdout_fileno)
    msg = raw_input("$ ")
    while msg != 'EXIT':
        senders = []
        select.select([], senders, [], 2)
        for sock in senders:
            SOCKET_MUTEX.acquire()
            sock.sendall(msg)
            SOCKET_MUTEX.release()

            STDIO_MUTEX.acquire()
            print "{} You:  {}\n".format(datetime.now(), msg)
            STDIO_MUTEX.release()
        msg = raw_input("$ ")
    EXITING = True


# Helper function to receive messages
def listener(s, stdout_fileno):
    sys.stdout = os.fdopen(stdout_fileno)
    while not EXITING:
        try:
            readers = []
            select.select(readers, [], [], 2)
            for r in readers:
                SOCKET_MUTEX.acquire()
                msg = r.recv(MAX_BUFF)
                SOCKET_MUTEX.release()

                STDIO_MUTEX.acquire()
                print "{} Them: {}\n".format(datetime.now(), msg)
                STDIO_MUTEX.release()
        except Exception as e:
            print "[-] {}".format(e)
            time.sleep(1)
    print "[-] Listener exiting"


# Main handler.
def main(host, port):
    # Standard TCP IPv4 Socket.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile="certs/ca-bundle.crt")
    conn = context.wrap_socket(sock, server_hostname=u"Nick Anderson")
    conn.connect((host, port))

    try:
        conn.settimeout(2)
        conn.setblocking(0)
        stdin_copy = sys.stdin.fileno()
        stdout_copy = sys.stdout.fileno()
        s = multiprocessing.Process(target=sender, args=(conn,stdin_copy,stdout_copy,))
        s.daemon = True
        s.start()

        l = multiprocessing.Process(target=listener, args=(conn,stdout_copy,))
        l .daemon = True
        l.start()

        # Loop forever
        while not EXITING:
            pass

    except Exception as e:
        print e

    finally:
        # Tear down the socket.
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--listen", type=str, default="127.0.0.1", help="The server host to connect to")
    parser.add_argument("-p", "--port", type=int, default=31337, help="The port on which the server is listening for "
                                                              "connections")
    args = parser.parse_args()
    main(args.listen, args.port)