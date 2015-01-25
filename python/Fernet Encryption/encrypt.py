import sys
import os
import argparse
from cryptography.fernet import Fernet

def encrypt(fname, key):
    data = open(os.path.join(os.getcwd(), fname), 'rb').read()
    fout_name = '.'.join(fname.split(".")[:-1]) if len(fname.split(".")) > 1 else fname
    fout = open(os.path.join(os.getcwd(), fout_name+".enc"), 'wb')
    kout = open(os.path.join(os.getcwd(), "key.out"), 'wb')
    fenc = Fernet(key)
    print "[+] Encrypting {} to {}.enc . . .".format(fname,fname)
    fout.write(fenc.encrypt(data))
    kout.write(key)
    fout.close()
    kout.close()
    print "[+] Encryption Completed!"
    print "[+] Encrypted data has been written to {}.enc".format(fname)
    print "[+] Key file has been written to {}.  Keep this file safe!!".format("key.out")

if __name__ == "__main__":

    fname  = ''
    key    = ''
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--clearfile", type=str, help="File to Encrypt, should be in the local directory")
    parser.add_argument("-k","--key", type=str, help="Encryption Key, must be a Fernet Key from the python cryptography module")
    args = parser.parse_args()

    #print "[+] DBG - args.key: {}".format(args.key)
    #print "[+] DBG - args.clearfile: {}".format(args.clearfile)

    if not os.path.exists(os.path.join(os.getcwd(), args.clearfile)):
        print "[-] Clear Text file not found in current working directory."
        sys.exit()
    elif not args.key:
        print "[+] Generating new encryption key.  Key will be written to {}".format(os.path.join(os.getcwd(), "key.out"))
        key = Fernet.generate_key()
    elif not os.path.exists(os.path.join(os.getcwd(), args.key)):
        print "[-] Encryption key file not found in current working directory."
        sys.exit()
    else:
        key = open(os.path.join(os.getcwd(), args.key), "rb").read()

    encrypt(args.clearfile, key)
