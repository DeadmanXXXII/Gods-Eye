import os

# Define target IP range and output file
target_ip_range = "192.168.1.0/24"
output_file = "nmap_scan_results.txt"

# Run Nmap scan
os.system(f"nmap -sV --script=vuln --script-args=unsafe=1 {target_ip_range} -oN {output_file}")

# Parse and analyze Nmap output
with open(output_file, 'r') as file:
    scan_results = file.readlines()

# Print or process the results
for line in scan_results:
    if "VULNERABLE" in line:
        print(line)
