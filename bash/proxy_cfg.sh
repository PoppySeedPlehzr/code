#!/bin/bash

# I'm writing this script because I'm tired of having to
# turn off all of my farkin proxy settings whenever I jack
# my laptop from work into my home connection -.-

iface=$(route get 0.0.0.0 | awk '/interface: / {print $2}')
proxy='XXX.XXX'

if [ $iface == 'en0' ]
then
    # echo Network active
    # Do Proxy stuff here
    ip=$(ifconfig $iface | awk '{ print $2 }' | grep -E -o '[1-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}');
    sub=$(echo $ip | grep -E -o '^[0-9]{1,3}\.[0-9]{1,3}')
    if [ $sub == $proxy ]
    then
        # Perform proxy config for net here
    else
    else
        # Otherwise, no configs, add DNS if wanted.
    fi
fi
