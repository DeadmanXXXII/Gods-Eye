import requests
import json

def enrich_data(data):
    # Example: Call an external API to enrich the IP data
    response = requests.get(f"https://ipinfo.io/{data['ip']}/json")
    enriched_data = response.json()
    return enriched_data

def publish_to_queue(enriched_data):
    queue_url = "http://rabbitmq-service:15672/api/exchanges/%2F/amq.default/publish"
    payload = {
        "properties": {},
        "routing_key": "data_enriched",
        "payload": json.dumps(enriched_data),
        "payload_encoding": "string"
    }
    response = requests.post(queue_url, json=payload, auth=("user", "password"))
    return response.status_code

# Example data
data = {'ip': '192.168.1.1'}
enriched_data = enrich_data(data)
publish_to_queue(enriched_data)