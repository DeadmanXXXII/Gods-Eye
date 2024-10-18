#!/bin/bash

# Define a list of target IP ranges
target_ips=("192.168.1.0/24" "203.0.113.0/24")

# Loop through each range and scan using Nmap
for ip in "${target_ips[@]}"
do
    echo "Scanning $ip"
    nmap -sV --script=vuln --script-args=unsafe=1 $ip -oN nmap_scan_results.txt
done
