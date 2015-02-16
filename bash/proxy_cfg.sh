#!/bin/bash

# I'm writing this script because I'm tired of having to
# turn off all of my farkin proxy settings whenever I jack
# my laptop from work into my home connection -.-

iface=$(route get 0.0.0.0 | awk '/interface: / {print $2}')
proxy='134.253'
if [ $iface == 'en0' ]
then
    # echo Network active
    # Do Proxy stuff here
    ip=$(ifconfig $iface | awk '{ print $2 }' | grep -E -o '[1-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}');
    sub=$(echo $ip | grep -E -o '^[0-9]{1,3}\.[0-9]{1,3}')
    if [ $sub == $proxy ]
    then
        # Perform Sandia Proxy information here
        export http_proxy="http://wwwproxy.sandia.gov:80"
        export https_proxy="http://wwwproxy.sandia.gov:80"
        export ftp_proxy="http://wwwproxy.sandia.gov:80"
        export HTTP_PROXY="http://wwwproxy.sandia.gov:80"
        export HTTPS_PROXY="http://wwwproxy.sandia.gov:80"
        export FTP_PROXY="http://wwwproxy.sandia.gov:80"
    else
    else
        # Setup DNS and... other shit here

    fi
fi
