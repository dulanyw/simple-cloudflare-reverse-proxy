# Super Simple Reverse-Proxy Using Cloudflare

Who needs a dedicated reverse-proxy client when Cloudflare exists? With this script, you certainly don't! 

This system implements a simple, transparent reverse-proxy using Cloudflare infrastructure. This does not implement of all the steps required to get a fully functioning reverse-proxy connection (see "Prerequisites" below), but it covers the ongoing update of the dynamic DNS service (in this case, Cloudflare).

## Prerequisites

1. Python 3 installed on the computer requiring the reverse-proxy'ing.
2. A Cloudflare account. A free tier is available for hobbyist applications.
3. A domain name. This does not have to be purchased through Cloudflare, and some sites do offer (limited) free options.
4. Adding your domain to your Cloudflare account. This includes updating the name servers for your domain so that they point to Cloudflare (just follow the prompts - Cloudflare's process for onboarding new domains is really good).

To get the full benefits of a reverse-proxy configuration, you'll also need to set up port forwarding on your router (or other device you use to connect to the Internet). This script redirects the domain to your router's IP address, but the visitor won't make it past the router/firewall/etc. without port forwarding. This step is somewhat hardware specific and out of the scope of this document, but you can find a lot of great references for this via search engines.

## Deployment

1. Clone this repo to the computer requiring the reverse-proxy'ing. 
2. Run 'python -m pip install -r requirements.txt'
3. Rename 'config.example' to 'config.yaml'.
4. Open 'config.yaml' and enter your specific information for each line.
	a. "domain" is the domain name for your site (like "example.com").
	b. "cf_email" is your Cloudflare login email.
	c. "cf_api" is your Cloudflare API key, found [here](https://dash.cloudflare.com/profile/api-tokens) under "Global API Key".
	d. "cf_zone" is the "zone" associated with the domain. In the Cloudflare dashboard, click on the domain, then copy the Zone ID found under the "API" heading.
5. Update your system to periodically run "simpleddns.py" (as a cron job on Linux, or as a scheduled task on Windows).

## License

Released under Creative Commons CC BY-SA license. No support offered or implied - this is open source, so use at your own risk.