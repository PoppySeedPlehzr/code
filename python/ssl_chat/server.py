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
def sender(s, fileno):
    global EXITING
    # We re-open stdin here, so we can use raw_input inside a child process.
    sys.stdin = os.fdopen(fileno)
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
def listener(s):
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


def main(host, port):
    # Standard TCP IPv4 Socket.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set the up the SSL context wrapper.
    context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="certs/cert.pem", keyfile="certs/key.pem")

    try:
        sock.bind((host, port))
        sock.listen(5)
        print "[+] Server side is listening on {}:{}".format(host, port)

        s, addr = sock.accept()

        connstream = context.wrap_socket(s, server_side=True)
        connstream.settimeout(2)
        connstream.setblocking(0)

        stdin_copy = sys.stdin.fileno()
        p = multiprocessing.Process(target=sender, args=(connstream,stdin_copy,))
        p.daemon = True
        p.start()

        l = multiprocessing.Process(target=listener, args=(connstream,))
        l .daemon = True
        l.start()

        while not EXITING:
            pass

    except Exception as e:
        print e

    finally:
        print "[-] {}: Server side, shutting down socket".format(datetime.now())
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--listen", type=str, default="127.0.0.1", help="The IP Address on which to listen")
    parser.add_argument("-p", "--port", type=int, default=31337, help="The Port on which to listen")
    args = parser.parse_args()
    main(args.listen, args.port)