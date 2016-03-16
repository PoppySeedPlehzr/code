#!/usr/bin/env python
import argparse
import requests
import json
from config import VT_URL
from keys import VT_API_KEY



def main(d):
    params = {"resource":d, 'apikey':VT_API_KEY}
    resp = requests.post(VT_URL, params)
    if resp.status_code == 200:
        print(resp.text)
    else:
        print("[-] Got back: {}\n{}".format(resp.status_code, resp.text))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("digest", help="md5/sha1/sha256 hash to search")
    args = parser.parse_args()
    main(args.digest)
