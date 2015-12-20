#!/usr/bin/env python
import requests
import argparse

url = "http://api.md5crack.com"
# MD5Crack API Key: 
key = ""

def lookup(h):
	resp = requests.get(url+"/crack/"+key+"/"+h)
	if resp.status_code == 200:
		print "{}".format(resp.text)
	else:
		print "[-] Got back: {}\n{}".format(resp.status_code, resp.text)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("MD5", help="An MD5 to lookup")
	#parser.add_argument("--string", help="A string to hash")
	args = parser.parse_args()
	lookup(args.MD5)
