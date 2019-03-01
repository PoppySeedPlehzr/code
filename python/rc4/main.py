from rc4 import RC4

import argparse
import logging
import os
import sys

logging.basicConfig(
    level=logging.INFO,
    format='[%(process)d][%(name)s][%(asctime)s]: %(message)s',
    datefmt='%m-%d-%Y-%H:%M'
)
logger = logging.getLogger("RC4 Driver")


def main(content: str = None, key: str = None):
    
    # First encrypt
    enc = encrypt(content, key)
    logger.info("Encrypted Message Length: {}".format(len(enc)))
    logger.info("Encrypted Message: {}".format(enc))

    # Then decrypt
    dec = encrypt(enc, key)

    logger.info("Decrypted Message Length: {}".format(len(dec)))
    assert(len(content) == len(dec))
    logger.info("Decrypted Message: {}".format(dec))
    assert(content == dec)

def encrypt(content: str = None, key: str = None):
    crypter: RC4 = RC4(key)
    return crypter.encrypt(content)

if __name__ == "__main__":
    desc: str = "A simple RC4 encrypt/decrypt script"
    ap = argparse.ArgumentParser(description=desc)
    # TODO: File in, file out, stdin, stdout, ...
    ap_group = ap.add_mutually_exclusive_group(
        required=True
    )

    ap_group.add_argument(
        "--file",
        default=None,
        help="An optional file path to encrypt. Encrypted text will be " +
             "written to the file name with `.enc` appended."
    )
    ap_group.add_argument(
        "--stdin",
        default=None,
        help="Read text from stdin for encryption. This option is mutually " +
             "exclusive from the file encryption option."
    )

    ap.add_argument("key", metavar="k", help="Key used for encryption")

    args = ap.parse_args()
    content: str = ""
    if args.file:
        if os.path.exists(args.file):
            fout: str = args.file + ".enc"
            with open(args.file, "r") as f:
                content = f.read()
            enc = encrypt(content, args.key)
            with open(fout, 'w') as f:
                f.write(enc)
        else:
            logger.error(
                "Failed to find file for encryption: {}".format(args.file)
            )
            sys.exit(1)
    else:
        content = args.stdin
        main(content, args.key)
