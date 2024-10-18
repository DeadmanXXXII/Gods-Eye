# G.E-P.O.C.S.O.C

Myth-buster
---

1. Setup and Automation Script (Install Dependencies)

This script will set up the environment, installing the required tools like Shodan, Nmap, and Python dependencies.

setup.sh
```bash
#!/bin/bash

# Update system
sudo apt update -y && sudo apt upgrade -y

# Install dependencies
sudo apt install -y nmap exiftool openvpn git python3-pip

# Install OpenCV and YOLO for real-time video monitoring
pip3 install opencv-python numpy

# Install Shodan CLI
pip3 install shodan
shodan init <your_shodan_api_key>

# Install Ansible for automation
sudo apt install -y ansible

# Install geopy and requests for geolocation
pip3 install geopy requests

# Clone your OSINT platform repository
git clone https://github.com/your-osint-platform.git
cd your-osint-platform

# Install additional Python dependencies
pip3 install -r requirements.txt

echo "Setup complete. All tools installed."
```

---

2. Shodan Script for Continuous IP Scanning and Geo-Location

This Python script uses Shodan to scan for internet-connected devices within a specific geographic range and retrieve their location. It uses OpenCage Data to convert latitude and longitude to an 8-figure grid reference.

shodan_scan.py
```python
import shodan
import requests

# Initialize Shodan API
SHODAN_API_KEY = 'your_shodan_api_key'
api = shodan.Shodan(SHODAN_API_KEY)

# Search query to find devices with GPS data
query = 'geo:"51.5074,-0.1278" port:80,443 has_screenshot:true'

# Make the query
results = api.search(query)

# Function to get 8-figure grid reference using latitude and longitude
def get_grid_reference(lat, lon):
    url = f'https://api.opencagedata.com/geocode/v1/json?q={lat}+{lon}&key=your_opencagedata_api_key'
    response = requests.get(url).json()
    # Parse response and get grid reference if available
    try:
        grid_ref = response['results'][0]['annotations']['OSM']['grid_reference']
        return grid_ref
    except KeyError:
        return "Grid reference not available"

# Loop through results
for result in results['matches']:
    ip = result['ip_str']
    lat = result['location']['latitude']
    lon = result['location']['longitude']

    # Get grid reference
    grid_ref = get_grid_reference(lat, lon)

    print(f"IP: {ip}, Latitude: {lat}, Longitude: {lon}, Grid Reference: {grid_ref}")
```

---

3. Nmap Script for Continuous Scanning

This bash script uses Nmap to scan for devices within specific IP ranges, checking for open ports and potential vulnerabilities. The script can be run periodically via a cron job.

nmap_scan.sh
```bash
#!/bin/bash

# Define a list of target IP ranges
target_ips=("192.168.1.0/24" "203.0.113.0/24")

# Loop through each range and scan using Nmap
for ip in "${target_ips[@]}"
do
    echo "Scanning $ip"
    nmap -sV --script=vuln $ip -oN scan_results.txt
done
```

---

4. IP Geolocation and Distance Calculation

This Python script retrieves the geolocation (latitude and longitude) of an IP address and calculates the distance from the target. It is useful for finding the proximity of devices to a specific location.

ip_geolocation.py
```python
import requests
from geopy.distance import geodesic

def get_ip_location(ip):
    url = f'http://ipinfo.io/{ip}/geo'
    response = requests.get(url).json()
    if 'loc' in response:
        lat, lon = response['loc'].split(',')
        return float(lat), float(lon)
    return None, None

# Function to calculate distance between two locations
def calculate_distance(lat1, lon1, lat2, lon2):
    location1 = (lat1, lon1)
    location2 = (lat2, lon2)
    return geodesic(location1, location2).km

# Example IP and target location
ip = '8.8.8.8'  # Google DNS as an example
target_lat, target_lon = 51.5074, -0.1278  # London

# Get the location of the IP
ip_lat, ip_lon = get_ip_location(ip)

# Calculate the distance to the target
if ip_lat and ip_lon:
    distance = calculate_distance(target_lat, target_lon, ip_lat, ip_lon)
    print(f"Distance to target: {distance:.2f} km")
```

---

5. Automation with Ansible Playbook

This Ansible playbook automates the installation and configuration of the required tools and dependencies for scanning and tracking devices across multiple machines.

osint-playbook.yml

---
```Ansible
- hosts: osint_nodes
  become: yes
  tasks:

    - name: Update apt cache
      apt: 
        update_cache: yes

    - name: Install required packages
      apt:
        name: ['nmap', 'exiftool', 'python3-pip', 'git']
        state: present

    - name: Install Python dependencies
      pip:
        name:
          - shodan
          - opencv-python
          - numpy
          - geopy
          - requests
          - selenium

    - name: Clone OSINT platform repository
      git:
        repo: 'https://github.com/your-osint-platform.git'
        dest: /opt/osint-platform

    - name: Install platform dependencies
      pip:
        requirements: /opt/osint-platform/requirements.txt
```

---

6. Kubernetes Deployment for Distributed Scanning

You can deploy the entire IP scanning system in a Kubernetes cluster for scalability and distributed tracking.

ip-scanning-deployment.yml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ip-scanning-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ip-scanner
  template:
    metadata:
      labels:
        app: ip-scanner
    spec:
      containers:
      - name: ip-scanner-container
        image: your_ip_scanning_image:latest
        command: ["python", "shodan_scan.py"]
---
apiVersion: v1
kind: Service
metadata:
  name: ip-scanning-service
spec:
  selector:
    app: ip-scanner
  ports:
    - protocol: TCP
      port: 8080
      targetPort: 80
  type: LoadBalancer
```

---

7. Setting Up Recurring Jobs (Cron)

To automate recurring scans, set up a cron job that periodically runs the Shodan, Nmap, or geolocation scripts.

Example Cron Jobs:
```cron
# Run Shodan scan every hour
0 * * * * /path/to/shodan_scan.py

# Run Nmap scan every 30 minutes
*/30 * * * * /path/to/nmap_scan.sh
```

---


You're right, I forgot to include the social media checkers that are essential for tracking recurring activity across social media platforms. Below are the steps and scripts to incorporate social media tracking into the system.


---

9. Social Media Checkers

For tracking social media profiles, messaging, and posts related to the identified IPs, we can use tools such as theHarvester, Social Mapper, and API access to platforms like Telegram or Twitter.

A. Social Media Profile Search with theHarvester

theHarvester is a tool that can gather information such as emails, names, and social profiles from various platforms (LinkedIn, Twitter, etc.) related to a domain or IP range.

Command to use theHarvester:

# theHarvester example command for LinkedIn and Twitter
theHarvester -d targetdomain.com -b linkedin,twitter

You can also automate this using a script:

social_media_harvest.sh
```bash
#!/bin/bash

# Run theHarvester to find social media profiles related to the IP/domain
target="targetdomain.com"
output_file="harvest_results.txt"

# Search for LinkedIn and Twitter profiles
theHarvester -d $target -b linkedin,twitter -f $output_file

echo "Social media profiles saved in $output_file"
```
B. Social Media Correlation with Social Mapper

Social Mapper uses facial recognition to correlate social media profiles across different platforms. It takes an image or list of people and searches for matching profiles on LinkedIn, Facebook, Instagram, etc.

Social Mapper Example Command:
```
# Social Mapper to correlate LinkedIn profiles
python social_mapper.py -f imagefolder -i "linkedin" -m fast
```
You can create a folder with images of individuals and Social Mapper will search for profiles across platforms.


---

C. Telegram Public Channel Monitoring

You can use Telegram's API to monitor public channels and look for recurring messages related to the target.

1. Set up a Telegram Bot to get the API key.


2. Use the Telethon Python library to interact with Telegram.


```
telegram_monitor.py

from telethon.sync import TelegramClient

# Replace these with your Telegram API credentials
api_id = 'your_api_id'
api_hash = 'your_api_hash'
phone = 'your_phone_number'

# Initialize the Telegram client
client = TelegramClient(phone, api_id, api_hash)
client.start()

# Target public channel or group
target_channel = 'target_public_channel'

# Fetch messages from the target channel
for message in client.iter_messages(target_channel):
    print(f"Sender ID: {message.sender_id}, Message: {message.text}")
```

This script monitors public Telegram channels and tracks messages from specific users.
Also use and automate Telethon.

---

D. Twitter API for Public Tweets Monitoring

To track public tweets related to your targets, use the Twitter API via tweepy.

1. Set up Twitter Developer API credentials.


2. Use Tweepy to fetch and track tweets containing specific keywords or hashtags.



twitter_monitor.py

```python
import tweepy

# Replace with your Twitter API credentials
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Define the keyword/hashtag to track
keyword = 'target_keyword'

# Fetch public tweets containing the keyword
for tweet in tweepy.Cursor(api.search, q=keyword, lang="en").items(50):
    print(f"User: {tweet.user.screen_name}, Tweet: {tweet.text}")
```

This script retrieves public tweets containing a specific keyword or hashtag related to your target.


---

10. Integrating Social Media Checkers into the Workflow

You can automate the social media checking process with a cron job or integrate it into your Ansible playbook.

Automated Social Media Check with Cron Job:

Create a cron job to run theHarvester and Telegram or Twitter scripts periodically.

Example Cron Job:
```cron
# Run social media check every day at 1 AM
0 1 * * * /path/to/social_media_harvest.sh

# Monitor Telegram messages every 30 minutes
*/30 * * * * /path/to/telegram_monitor.py
```

---

11. Integration with Kubernetes

You can also integrate the social media checkers into your Kubernetes deployment as a separate container that performs social media monitoring:

social-media-checker-deployment.yml:

apiVersion: apps/v1
kind: Deployment
metadata:
  name: social-media-checker-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: social-media-checker
  template:
    metadata:
      labels:
        app: social-media-checker
    spec:
      containers:
      - name: social-media-checker-container
        image: your_social_media_checker_image
        command: ["python", "twitter_monitor.py"]
---
apiVersion: v1
kind: Service
metadata:
  name: social-media-checker-service
spec:
  selector:
    app: social-media-checker
  ports:
    - protocol: TCP
      port: 8081
      targetPort: 80
  type: LoadBalancer


---



Complete Workflow:

1. Setup the environment using the setup.sh script, which installs all necessary dependencies.


2. Scan for internet-connected devices using Shodan with the shodan_scan.py script. This script retrieves device IP addresses and location information.


3. Run Nmap scans on the identified IPs to find open ports and vulnerabilities using the nmap_scan.sh script.


4. Retrieve IP geolocation and calculate the proximity of devices using the ip_geolocation.py script.


5. Check social media for related profiles, posts, or public messaging using:

theHarvester for social media profiles.

Social Mapper for cross-platform profile matching.

Telegram API to track public channels.

Twitter API to track public tweets and hashtags.



6. Automate the process across multiple machines using the Ansible playbook (osint-playbook.yml).


7. Deploy the system on Kubernetes for scalability using the Kubernetes deployment and service files (ip-scanning-deployment.yml).


8. Set up cron jobs for periodic scanning, geolocation, and social media monitoring.




---

This setup gives you continuous monitoring of IP-connected devices and their related social media activity, ensuring that you track lateral movement across the internet and social platforms getting loc stats as you go in 8 figure grid references.

Comprehensive OSINT Platform with SOC-like Features:

To build an advanced OSINT platform using a combination of tools like Creepy, Nmap, Maltego, and more, we’ll develop a custom OSINT solution that can gather intelligence from various sources, including social media, geolocation data, network mapping, and metadata extraction.

Here’s how we’ll build this OSINT platform, integrating these tools and using advanced techniques to automate data collection and analysis.


---

1. OSINT Platform Components

The platform will consist of the following modules:

1. Geolocation Tracking – Using Creepy and metadata extraction.


2. Network Mapping and Vulnerability Scanning – Using Nmap and Maltego.


3. Social Media and Personal Information Gathering – Using tools like theHarvester and Social Mapper.


4. Automated Metadata Extraction – Using ExifTool and IP-based geolocation.




---

2. Creepy: Geolocation Tracking

Creepy is a tool that gathers location-related information from social networking platforms and image metadata (such as GPS coordinates).

Step 1: Install Creepy

To install Creepy:

```
sudo apt-get install creepy
```

Step 2: Use Creepy for Geolocation

Creepy will search public social media accounts for posts that contain geolocation data (like check-ins or geotagged images). It can also extract metadata from images uploaded online.


1. Launch Creepy.


2. Select the Target Username (for example, a social media username).


3. Specify the Platforms (Twitter, Instagram, Flickr, etc.).


4. Run the query to gather geolocation data and map it on a world map.



You can export the data to CSV or KML for further analysis.

Automating Creepy with a Python Wrapper:

Creepy doesn’t have an official Python API, but you can automate its functionality by parsing the output files (e.g., CSV). Here’s an example of how you could wrap Creepy in Python:

```python
import os

# Define the target username and output path
username = "target_username"
output_file = f"/path/to/output/{username}_creepy_output.csv"

# Run Creepy from command line (adjust path to creepy as needed)
os.system(f"creepy --user {username} --output {output_file}")

# Parse and analyze the output CSV
import pandas as pd
data = pd.read_csv(output_file)

# Process the geolocation data (for example, plotting it on a map)
for index, row in data.iterrows():
    print(f"Location: {row['latitude']}, {row['longitude']}, Date: {row['timestamp']}")
```

---

3. Nmap: Network Mapping and Vulnerability Scanning

Nmap can be used for network reconnaissance and vulnerability scanning, identifying open ports and services across devices.

Step 1: Advanced Nmap Scan with Scripts

The following Nmap command scans for devices with specific services (e.g., HTTP, SSH) and checks for known vulnerabilities:

```
nmap -sV --script=vuln --script-args=unsafe=1 <target_ip_range> -oN nmap_scan_results.txt
```

-sV: Service detection to identify running services.

--script=vuln: Run vulnerability scripts to detect known vulnerabilities.

--script-args=unsafe=1: Enables potentially dangerous script scanning.

-oN nmap_scan_results.txt: Save the scan results to a file.


Automate Nmap with Python:

Here’s how you can integrate Nmap with your Python-based OSINT platform:

```python
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
```

---

4. Maltego: Advanced Network and Relationship Mapping

Maltego is a powerful data mining and visualization tool that allows you to gather OSINT data from various sources and map relationships between people, organizations, and online entities.

Step 1: Install and Launch Maltego

Install Maltego from the official website: Maltego Downloads.

Step 2: Use Maltego Transforms

Maltego allows you to run transforms (automated data-mining queries) that collect data from:

Social media profiles

Domain names

Email addresses

IP addresses


Example of mapping a target email to associated entities:

1. Start with the email address of the target.


2. Run the Email to Social Media transform to discover linked social media profiles.


3. Run the Domain to DNS Names transform to map domains to IPs and DNS servers.


4. Use the Person to Address transform to find physical locations.



Automating Maltego Using Paterva Transforms in Python:

Here’s how you can call Maltego’s Python API for automating certain transforms:

```python
from maltego_trx.transform import DiscoverableTransform
from maltego_trx.maltego import UIM_TYPES

class SocialMediaTransform(DiscoverableTransform):
    @classmethod
    def create_entities(cls, request, response):
        target_email = request.Value
        # Example transform logic to find social media profiles linked to an email
        social_profiles = find_social_profiles(target_email)  # Custom logic
        for profile in social_profiles:
            response.addEntity('maltego.SocialMedia', profile)
```
This will allow you to build custom transforms and include them in your automated OSINT tool.


---

5. Metadata Extraction with ExifTool

ExifTool extracts metadata from images and other media files, which often includes GPS data, camera settings, timestamps, and more.

Step 1: Install ExifTool

sudo apt-get install exiftool

Step 2: Extract Metadata from Images

Run the following command to extract all metadata from an image:

exiftool image.jpg

To automate metadata extraction and integrate it into your OSINT platform, here’s a Python script that calls ExifTool and processes the output:

```python
import subprocess
import json

# Function to extract metadata using ExifTool
def extract_metadata(file_path):
    result = subprocess.run(['exiftool', '-json', file_path], stdout=subprocess.PIPE)
    metadata = json.loads(result.stdout.decode('utf-8'))
    return metadata

# Test the function
metadata = extract_metadata('image.jpg')
print(metadata)
```

This script can be extended to process multiple files, automatically storing GPS data, timestamps, and other metadata into a database.


---

6. Integration of Tools into a Centralized OSINT Platform

You can combine all the above tools and modules into one centralized OSINT platform, managed by a Kubernetes setup or a virtual machine cluster.

Here’s a high-level architecture of how you can combine these tools:

1. Geolocation (Creepy):

Extract and plot geolocation data from social media profiles and images.

Store geolocation results in a central database for further analysis.



2. Network Mapping and Scanning (Nmap + Maltego):

Periodically scan for open ports and vulnerabilities.

Visualize relationships between IPs, domains, and services using Maltego.



3. Metadata Extraction (ExifTool):

Automate the extraction of image metadata (GPS, timestamps).

Feed metadata into the OSINT platform for geo-based intelligence.



4. Social Media Data (theHarvester, Social Mapper):

Gather data from social media platforms.

Correlate social profiles across platforms.



5. Automation & Scheduling:

Use Ansible to automate setup and configuration of OSINT tools across multiple machines.

Set up cron jobs to periodically run scans and social media checks.





---

7. Example Workflow Using All Tools

1. Creepy: Use geolocation data from social media to track the movement of a target.


2. Nmap: Continuously scan IP ranges for vulnerabilities and services.


3. Maltego: Visualize and correlate relationships between domains, IPs, and entities.


4. ExifTool: Extract metadata from images to retrieve GPS coordinates and timestamps.


5. theHarvester: Gather social media profiles related to an IP or domain.


6. Social Mapper: Correlate facial recognition across multiple platforms.


7. Cron Jobs: Set up cron jobs for periodic scanning and metadata extraction.




---

Conclusion

By combining these advanced OSINT tools (Creepy, Nmap, Maltego, ExifTool, theHarvester, and Social Mapper), you can build a powerful, automated platform capable of gathering and correlating intelligence from multiple sources. You can also integrate the system into a Kubernetes cluster or automate it using Ansible for deployment across multiple nodes.

1. Lateral Movement Detection:

Scanning Web-Connected Devices: By utilizing tools like Nmap and Shodan, the system can continuously scan for internet-connected devices, identify vulnerabilities, and discover lateral movement opportunities.

IP Management: The platform can dynamically update the list of active IPs found during scans and check for known vulnerabilities. It can also use the discovered IPs as placeholders for further analysis.



2. Geolocation Tracking:

Creepy and ExifTool Integration: By extracting geolocation data from social media profiles and image metadata, you can track individuals or devices' movements over time. This data can be correlated with IP address information to establish the physical locations of web-connected devices.

8-Figure Grid Reference: Using geolocation APIs, the system can convert latitude and longitude into an 8-figure grid reference, allowing for precise tracking of physical locations.



3. Social Media Checkers:

Data Collection from Social Media: Tools like theHarvester and Social Mapper can gather information about individuals, including their social media profiles, activity, and connections.

Monitoring Public Channels: By leveraging APIs from platforms like Telegram and Twitter, the system can monitor public communications for relevant keywords or discussions, providing insights into ongoing activities related to the target.



4. Vulnerability Scanning:

Nmap and Maltego: These tools can be used to scan devices for open ports and running services, identifying vulnerabilities. Maltego can visualize relationships between discovered devices, IPs, and social media profiles, enhancing situational awareness.



5. Automated Data Processing:

Integration of Various Tools: The system can be automated to run periodic scans, gather data from various sources, and store this information in a centralized database. This database can be queried to generate reports or alerts based on specific criteria (e.g., discovering new devices, finding active social media profiles).

Using Cron Jobs: Set up scheduled tasks to ensure the system runs continuously, gathering and analyzing data without manual intervention.



6. User Interface and Reporting:

Dashboard Development: Consider creating a web-based dashboard (using Flask, Django, or similar frameworks) that can visualize the gathered data, allowing users to interactively explore devices, social media profiles, geolocation data, and alerts.

Alerts and Notifications: Implement a notification system that can alert users to significant events, such as discovering new devices, unusual activities on social media, or proximity alerts when a device enters a specified area.




Implementation Overview

Here’s how you can structure the implementation:

1. Data Collection Module:

Use Shodan and Nmap for active scanning of IP addresses and vulnerability detection.

Incorporate ExifTool for metadata extraction and Creepy for geolocation data.

Use web scraping with Selenium to gather additional data from social media.



2. Database Storage:

Store all collected data (IP addresses, geolocation, social media profiles) in a database (like SQLite or PostgreSQL) for efficient querying and management.



3. Analysis and Reporting:

Use data processing scripts (Python-based) to analyze the data periodically and generate reports based on predefined criteria.

Consider building visualizations using libraries like Matplotlib or Dash.



4. Automation and Scheduling:

Set up cron jobs for automated scanning and monitoring.

Use Ansible or Kubernetes to manage deployments and scaling.




Limitations

While this setup can emulate many functions of a traditional SOC, there are some limitations:

Real-Time Response: Traditional SOCs often have dedicated personnel who monitor and respond to incidents in real-time. Your system will rely on automated responses, which may not react as quickly as human analysts.

Incident Management: An SOC typically has defined processes for incident management, while your system would need additional features for tracking and responding to incidents effectively.

Compliance and Legal Considerations: Ensure that the collection and processing of data, particularly from social media and other public platforms, comply with relevant legal frameworks and privacy regulations.


Conclusion

In summary, the proposed OSINT platform can effectively replicate many of the functionalities of a Security Operations Center, focusing on lateral movement detection, geolocation tracking, social media monitoring, and vulnerability scanning of web-connected devices. With proper automation, data management, and visualization, this platform can serve as a robust tool for security monitoring and intelligence gathering, mimicking the effects of Gods Eye from the fast amd the furious movie.


