#!/usr/bin/python3 
import requests, yaml, json

# Load configuration file
with open("config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)

# Step 1 - get the public IP address of the machine
ip = requests.get('https://api.ipify.org').text
print('My public IP address is: {}'.format(ip))

# Step 2 - get the object ID's of the records to be updated
# First, get the records for the zone
url = "https://api.cloudflare.com/client/v4/zones/{}/dns_records/".format(config.get('cf_zone'))

headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": "{}".format(config.get('cf_email')),
    "X-Auth-Key": "{}".format(config.get('cf_api'))
}

response_json = requests.request("GET", url, headers=headers)
response = json.loads(response_json.text)

# Parse the response to find the records to be updated - this version of the script just grabs the ID's of the type "A" records
records_to_update = []
for record in response['result']:
    if record['type'] == 'A': 
        if record['content'] != ip: records_to_update.append(record['id']) # Only add the record if the IP address has changed

if len(records_to_update) == 0:
    print("No records to update.")

# Step 3 - update the records with the new IP address
# Reference: https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-update-dns-record?schema_url=https%3A%2F%2Fraw.githubusercontent.com%2Fcloudflare%2Fapi-schemas%2Fmain%2Fopenapi.yaml#Request
for record in records_to_update:
    url = "https://api.cloudflare.com/client/v4/zones/{}/dns_records/{}".format(config.get('cf_zone'), record)

    payload = {
        "content": "{}".format(ip),
        "name": "{}".format(config.get('domain')),
        "proxied": True,
        "type": "A",
        "ttl": 3600
    }

    # Note - reusing the "headers" variable from Step 2 above
    response = requests.request("PUT", url, json=payload, headers=headers)

    print(response.text)

# TODO - Meaningful logging or notification of results. Recommendations welcome!