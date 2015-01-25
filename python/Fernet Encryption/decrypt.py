import sys
import os
import argparse
from cryptography.fernet import Fernet

def decrypt(fname, key):
    data = open(os.path.join(os.getcwd(), fname), 'rb').read()
    fout_name = '.'.join(fname.split(".")[:-1]) if len(fname.split(".")) > 1 else fname
    fout = open(os.path.join(os.getcwd(), fout_name+".clear"), 'wb')
    fdec = Fernet(key)
    print "[+] Decrypting {} to {}.clear . . .".format(fname,fout_name)
    fout.write(fdec.decrypt(data))
    fout.close()
    print "[+] Decryption Completed!"
    print "[+] Decrypted data has been written to {}.clear".format(fout_name)

if __name__ == "__main__":

    fname  = ''
    key    = ''
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--encryptedfile", type=str, help="Encrypted file. should be in the local directory")
    parser.add_argument("-k","--key", type=str, help="Decryption Key, must be a Fernet Key from the python cryptography module")
    args = parser.parse_args()

    if not os.path.exists(os.path.join(os.getcwd(), args.encryptedfile)):
        print "[-] Encrypted file not found in current working directory."
        sys.exit()
    elif not os.path.exists(os.path.join(os.getcwd(), args.key)):
        print "[-] Decryption key file not found in current working directory."
        sys.exit()
    else:
        key = open(os.path.join(os.getcwd(), args.key), "rb").read()
    decrypt(args.encryptedfile, key)
