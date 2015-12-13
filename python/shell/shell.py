#!/usr/bin/env python
import socket
import argparse
import subprocess
import multiprocessing

MAX_BUFF = 0x1000
DBG      = True

def shell(s, addr):
    s.send("$ ")
    data = s.recv(MAX_BUFF)
    while 'exit' not in data:
        if DBG: print "[+] Got Command: {}".format(data)
        try:
            subprocess.Popen(args=data.split(), stdin=None, stdout=s, stderr=s)
        except Exception as e:
            s.send("[-] Invalid Command.\n")
        s.send("$ ")
        data = s.recv(MAX_BUFF)
    if DBG: print "[+] Shutting down connection from: {}".format(addr)
    s.shutdown(socket.SHUT_RDWR)
    s.close()

def handle(addr, port, dbg):
    global DBG
    DBG = dbg
    sock = socket.socket()
    sock.bind((addr, port))
    sock.listen(1)
    while True:
        (s, addr) = sock.accept()
        if DBG: print "[+] Got connection from: {}".format(addr)
        p = multiprocessing.Process(target=shell, args=(s,addr,))
        p.daemon = True
        p.start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--address", type=str, default="localhost", help="Address the shell should listen on. Default is localhost.")
    parser.add_argument("--port", type=int, default=31337, help="Port the shell should listen on.  Default is 31337")
    parser.add_argument("--debug", type=bool, default=True, help="Write verbose output to stdout. Default is True")
    args = parser.parse_args()
    handle(args.address, args.port, args.debug)
