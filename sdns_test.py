import requests, yaml


# Load configuration
with open("config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)

url = "https://api.cloudflare.com/client/v4/zones/{}/dns_records/".format(config.get('cf_zone'))

headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": "{}".format(config.get('cf_email')),
    "X-Auth-Key": "{}".format(config.get('cf_api'))
}

response = requests.request("GET", url, headers=headers)

print(response.text)
'''
ip = requests.get('https://api64.ipify.org').text
print('My public IP address is: {}'.format(ip))
'''