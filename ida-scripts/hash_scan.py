#from idautils import *
#from idc import *
import sys
import argparse
import os
import multiprocessing


# This program will scan through a binary file (typically encoded/unstructured shellcode)
# and look for hashes of common Windows API libraries
# Construted based off of the article here:
# http://web.archive.org/web/20150121164227/https://www.nccgroup.com/en/blog/2014/06/extracting-the-payload-from-a-cve-2014-1761-rtf-document/
#
# ExitProcess   5F9E0942H
# Sleep         9ACE3327h

# Hold up y'all... This code gunna be slow :P

STDIO_LOCK = multiprocessing.Lock()

# Takes the binary data and an API function, and scans the data for
# hashes of the function
def scan(data, lib, fun, hashes):
    for h in hashes:
        offs = 0x00000000
        while offs < len(data):
            # TODO: Is there an endianness issue here?
            if h == data[offs:len(h)]: # Found a hash match
                STDIO_LOCK.acquire()
                print "[+] Found Hash Match for {}:{} at {}".format(lib, fun, hashes)


def handler(fname, dbg=False):
    # Construct the Hash table
    lib_hashes = []
    fin = open("hashes.csv",'r').readlines()
    lib = ''
    for l in fin[2:]:
        if l.startswith('#'):
            lib = l.split(',')[0].replace('#','')
            if dbg: print "[+] Added new library: {}".format(lib)
            lib_hashes[lib] = {}
        else:
            fn = l.split(0)
            lib_hashes[lib][fn] = [] # Make a list for each lib function
            for hsh in l.split(',')[1:]:
                lib_hashes[lib][fn].append(hsh) # Append each hash
            if dbg: print "[+] Added hashes for {}".format(fn)

    if dbg: print "[+] Hash library successfully imported."

    # Read in the binary file.
    data = open(fname, 'rb').read()
    for lib in lib_hashes.keys():
        for fun in lib_hashes[lib].keys():
            p = multiprocessing.Process(target=scan, args=(data, lib, fun, lib_hashes[lib][fun],))
            p.start()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan for common Windows API hashes in a binary file, typically Shellcode")
    parser.add_argument("--debug", default=False, help="Turn on scanning verbosity")
    parser.add_argument("file", help="Binary file to scan")
    args = parser.parse_args()
    if os.path.exists(args.file): handler(args.file, args.debug)
