#!/bin/bash

# OS X Bash script to determine what network one is connected to, and set the
# proxy and DNS settings accordingly.
#
# This is super not finished yet :|

if [ "$(id -u)" != "0" ]; then
  echo "This script must be run as root!"
  echo "Exiting."
  exit 1
fi

# Great way to get the active iface
iface=$(route get 0.0.0.0 | awk '/interface: / {print $2}')
proxy='' # Set this to be the subnet which needs to have a proxy set
ip=$(ifconfig $iface | awk '{ print $2 }' | grep -E -o '[1-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}');
sub=$(echo $ip | grep -E -o '^[0-9]{1,3}\.[0-9]{1,3}')

if [ $sub == $proxy ]
then
    echo "[+] At work: subnet [ $sub ]. Turning on network proxy and DNS"
    # Export/Configure the settings for work here. 
    #sudo networksetup -switchtolocation Work > /dev/null
else
    echo "[+] Not at work: subnet [ $sub ]. Turning off network proxy and DNS."
    # Turn off any work configuration settings/configure home network here.
    #sudo networksetup -switchtolocation Home > /dev/null
fi
