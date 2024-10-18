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
