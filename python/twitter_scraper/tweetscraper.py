#!/usr/bin/env python

__author__ = 'Muffins'

import twitter
import argparse
import json
from conf import *


# Takes a twitter user and a 'since_id' to get tweets from a user since a given ID.
def scrape(tu, since=0, dbg=True):
    api    = twitter.Api(consumer_key = TWTR_CK, consumer_secret = TWTR_CS, access_token_key = TWTR_AT,
                      access_token_secret = TWTR_ATS)
    twts   = []
    tweets = api.GetUserTimeline(screen_name=tu, since_id=0)
    for t in tweets:
        dump = {}
        dump["user"]  = tu
        dump["id"]    = t.id
        dump["time"]  = t.created_at
        dump["tweet"] = t.text
        print "[+] {}".format(json.dumps(dump))
        twts.append(dump)
    return twts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script to scrape tweets from a given user.")
    parser.add_argument('user', help="Twitter user to get tweets from")
    parser.add_argument('--since', '-s', help="Since ID, get all tweets since a specified Tweet ID")
    parser.add_argument('--debug', '-d', default=True, help="Display debugging verbosity")
    args = parser.parse_args()
    scrape(args.user, args.since, bool(args.debug))
