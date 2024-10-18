import shodan

# Initialize Shodan API
SHODAN_API_KEY = 'your_shodan_api_key'
api = shodan.Shodan(SHODAN_API_KEY)

# Search for devices with open HTTP ports (which might serve video feeds)
query = 'port:80,443 has_screenshot:true'
results = api.search(query)

# Process results
for result in results['matches']:
    ip = result['ip_str']
    org = result.get('org', 'n/a')
    product = result.get('product', 'n/a')
    print(f"IP: {ip}, Organization: {org}, Product: {product}")
    print(f"Open ports: {result['port']}")
    print(f"Location: {result['location']}")
    print("--------")
