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
