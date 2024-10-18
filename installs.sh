#!/bin/bash

# Update system
sudo apt update -y && sudo apt upgrade -y

# Install dependencies
sudo apt install -y nmap exiftool openvpn git python3-pip chromium-chromedriver

# Install Python packages
pip3 install -r requirements.txt

# Install additional tools
sudo apt install -y ansible iodine haproxy retroshare

echo "Setup complete. All tools installed."
