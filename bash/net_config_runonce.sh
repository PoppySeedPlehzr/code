#!/bin/bash

wifi="Wi-Fi"
eth="Thunderbolt Ethernet"

# Run-Once script to setup network-aware proxy
sudo networksetup -createlocation Work populate
sudo networksetup -createlocation Home populate

# Configure the Sandia Proxy network
sudo networksetup -switchtolocation Work

# Set the DNS Servers to be Sandia's
sudo networksetup -setdnsservers $wifi 134.253.16.5 134.253.181.25
sudo networksetup -setdnsservers $eth 134.253.16.5 134.253.181.25

# Turn on proxy for WiFi
sudo networksetup -setwebproxy $wifi wwwproxy.sandia.gov 80
sudo networksetup -setsecurewebproxy $wifi wwwproxy.sandia.gov 80
sudo networksetup -setftpproxy $wifi wwwproxy.sandia.gov 80

# Turn on proxy for Eth
sudo networksetup -setwebproxy $eth wwwproxy.sandia.gov 80
sudo networksetup -setsecurewebproxystate $eth wwwproxy.sandia.gov 80
sudo networksetup -setftpproxy $eth wwwproxy.sandia.gov 80

# Configure Home network
sudo networksetup -switchtolocation Home

# Set DNS to Google and OpenDNS
sudo networksetup -setdnsservers $wifi 8.8.8.8 208.67.222.222
sudo networksetup -setdnsservers $eth 8.8.8.8 208.67.222.222

# Turn off the proxy for WiFi
sudo networksetup -setwebproxystate $wifi off
sudo networksetup -setsecurewebproxystate $wifi
sudo networksetup -setftpproxystate $wifi off

# Turn off the proxy for Eth
sudo networksetup -setwebproxystate $eth off
sudo networksetup -setsecurewebproxystate $eth off
sudo networksetup -setftpproxystate $eth off
