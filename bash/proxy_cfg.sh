#!/bin/bash

# I'm writing this script because I'm tired of having to
# turn off all of my farkin proxy settings whenever I jack
# my laptop from work into my home connection -.-

if [ "$(id -u)" != "0" ]; then
  echo "This script must be run as root!"
  echo "Exiting."
  exit 1
fi

# Great way to get the active iface
iface=$(route get 0.0.0.0 | awk '/interface: / {print $2}')
proxy='134.253'
ip=$(ifconfig $iface | awk '{ print $2 }' | grep -E -o '[1-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}');
sub=$(echo $ip | grep -E -o '^[0-9]{1,3}\.[0-9]{1,3}')

if [ $sub == $proxy ]
then
    echo "[+] At work: subnet [ $sub ]. Turning on network proxy and DNS"

    export http_proxy="http://wwwproxy.sandia.gov:80"
    export https_proxy="http://wwwproxy.sandia.gov:80"
    export ftp_proxy="http://wwwproxy.sandia.gov:80"
    export HTTP_PROXY="http://wwwproxy.sandia.gov:80"
    export HTTPS_PROXY="http://wwwproxy.sandia.gov:80"
    export FTP_PROXY="http://wwwproxy.sandia.gov:80"
    sudo networksetup -switchtolocation Work > /dev/null
else
    echo "[+] Not at work: subnet [ $sub ]. Turning off network proxy and DNS."

    export http_proxy=""
    export https_proxy=""
    export ftp_proxy=""
    export HTTP_PROXY=""
    export HTTPS_PROXY=""
    export FTP_PROXY=""
    sudo networksetup -switchtolocation Home > /dev/null
fi
