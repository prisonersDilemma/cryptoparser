#!/usr/bin/env python3.6

## Example output:
# ex: Crypto-Loot.com,show-anime.com,104.31.78.233,1
#     ^^args.keyword  ^^domain       ^^ip,         ^found vs not found
#
## Example of keyword (javascript) embedded in html.
# A match in use should look something like this, specifically in the case
# of crypto-loot.com: <script src="https://crypto-loot.co>


# Python standard library.
import os
import re
import subprocess
import sys

# Third-party modules from pypi.
try:
    import netaddr # Not part of standard library. Found on https://pypi.python.org/pypi/netaddr/0.7.19
except ImportError:
    # Trying to install while in HOME will cause an error because pip will think the
    # cache is meant for it.
    os.chdir(os.path.expanduser('~'))
    proceed = input('Do you wish to install module "netaddr" for Python3 (y/n)? ')
    if proceed:
        if subprocess.run(['sudo', 'pip3.6', 'install', 'netaddr']).returncode != 0:
            sys.stderr.write('error: pip install module `netaddr` failed\n')
            sys.exit(1)
    else:
        sys.stdout.write('Cannot continue without "netaddr module. Exiting.\n"')
        sys.exit(0)

import netaddr #noqa


# Relative: Modules for this package.
from __init__ import (CACHE, HOME, JSON_REVERSEIP_RESPONSE_FILE, # Variables.
                      JSON_DNSRECORD_RESPONSE_FILE, OUTPUT_FILE)
import json_parser
import options
import scans
import searches


# IP Address pattern.
ipaddr = re.compile(r'\d{3}\.\d{3}\.\d{,3}\.\d{,3}').match


def scan_sites(sites, keyword):
    pass


def output(keyword, domain, host_ip, n):
    return ','.join((keyword, domain, host_ip, n))


def reverseip_lookup(url, path, keyword):
    with open(path, 'w') as f: # Located in CACHE. Necessary to write to file first?
        f.write(scans.query(url)) # json_response from API call.

    # Get the HTML of these hosts, and check for the keyword.

    reverseip = json_parser.reverseip_dict( # 'host_ip', 'domain_count', 'domains'
        json_parser.load_json(path))

    for domain in reverseip['domains'][0]:
        # Compose the URI.
        uri = ''.join(('http://', domain)) # httplib2.Http().request(URL) requires absolute URI.

        #scans.scan(domain, args.keyword)
        #scans.scan_with_dns_name(domain, args.keyword)

        ip = reverseip['host_ip']
        if searches.keyword_found(keyword, scans.query(uri)):
            return output(keyword, domain, ip, 1)
        return output(keyword, domain, ip, 0)


def dnsrecord_lookup(url, domain, path, keyword):
    json_response = scans.query(url)
    with open(path, 'w') as f:
        f.write(json_response)
    dnsrecord_dict = json_parser.dnsrecord_parser(json_parser.load_json(path)) #noqa

    # What data are we looking for, and then what are we doing with it?
    ips = json_parser.dnsrecord_ips(dnsrecord_dict)
    # Now scan these and write to outfile.
    for ip in ips:
        uri = ''.join(('http://', ip))
        if searches.keyword_found(keyword, scans.query(uri)):
            return output(keyword, domain, ip, 1)
        return output(keyword, domain, ip, 0)


def main():
    args = options.parse()

    # Create necessary directories if they do not exist.
    for path in [HOME, CACHE]:
        if not os.path.exists(path): os.mkdir(path)

    # Determine the host from either a dns_name or ip_address provided as an argument.
    # 'host' is either args.ip_address, args.dns_name, or args.cidr_range
    #host = args.dns_name if args.dns_name else args.ip_address
    #if host is None: raise Exception('ERROR: no domain/dns name or ip address provided')

    # The api_url is specific to the type of API call (contingent on args.ip_address/cidr_range,
    # or args.dns_name), and further, to A/MX records if dnsrecord API (--dns_name provided)is used.
    # The results of each are different and require different JSON parsing.

    common_prefix = args.api_site
    common_suffix = ''.join(('&apikey=', args.api_key, '&output=', args.api_output))

    if args.ip_address: # reverseip
        # Force forms to be appropriate: e.g., ip_address is an ip_pattern.
        try: ipaddr(args.ip_address).group()
        except AttributeError:
            sys.stdout.write('error: --ip-address requires a valid ip address. Please try again.\n')
            sys.exit(1)

        # Construct the url needed for the reverseip API call.
        middle = ''.join(('reverseip/', '?host=', args.ip_address))
        url = middle.join((common_prefix, common_suffix))
        #try:
        out = reverseip_lookup(url, JSON_REVERSEIP_RESPONSE_FILE, args.keyword)
        #except ConnectionRefusedError: #noqa
        #    # Sleep? Try again? How many times?
        #    print('Connection refused.')
        #    return

    elif args.dns_name: # dnsrecord
        middle = ''.join(('dnsrecord/', '?domain=', args.dns_name, '&recordtype=', 'A'))
        url = middle.join((common_prefix, common_suffix))
        out = dnsrecord_lookup(url, args.dns_name, JSON_DNSRECORD_RESPONSE_FILE, args.keyword)

    elif args.cidr_range:
        # Should be same as ip_address (e.g., reverseip_lookup()), but will in a loop.
        #startip, endip = args.cidr_range[0], args.cidr_range[1] #noqa
        # cidrs = netaddr.iprange_to_cidrs(startip, endip)
        pass


    print(out) # Testing.
    # Write to csv style output to OUTPUT_FILE.
    with open(OUTPUT_FILE, 'a') as o:
        o.write(out)
    # Print to stdout if verbose, or a different level of logging is enabled?
    #print(out)


if __name__ == '__main__':
    main()
