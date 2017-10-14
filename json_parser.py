#!/usr/bin/env python3.6

# Standard Library.
import json

# Relative.
import __init__


def load_json(path=None, http_response=None):
    """Return the dict from the json file."""
    if path:
        with open(path) as f:
            return json.load(f)
    elif http_response: return json.load(http_response)
    else: raise Exception('ERROR: invalid filetype for json')


def domains(json_dict=None):
    """Return a list of domains from the json response dict returned by the reverseip API call."""
    if not json_dict: json_dict = load_json(__init__.json_response_file)
    return [domain['name'] for domain in json_dict['response']['domains']]


def domain_count(json_dict=None):
    """Return the number of associated domains with the host as an integer from the
    json response dict returned by the reverseip API call.
    """
    if not json_dict: json_dict = load_json(__init__.json_response_file)
    return int(json_dict['response']['domain_count'])


def host_ip(json_dict=None):
    """Return the IP address of the queried domain name from the json response dict returned
    by the reverseip API call.
    """
    if not json_dict: json_dict = load_json(__init__.json_response_file)
    return json_dict['query']['host']


def reverseip_dict(json_dict):
    """Return a dict of the domains, domain_count, and host_ip from the json response
    dict returned by the reverseip API call.
    """
    return {'domains': domains(json_dict),
            'domain_count': domain_count(json_dict),
            'host_ip': host_ip(json_dict)}


def dnsrecord_ips(json_dict):
    """Return the IPs associated with the dnsrecord API call in a list."""
    return [ip['data'] for ip in json_dict['response']]


if __name__ == '__main__':
    import os
    json_dict = load_json(os.path.join(__init__.HOME,
                          'json_test_response.json'))


    def print_results(hst=None, dmn_ct=None, dmns=None):
        """Print host, domain_count, and domains if provided. Domains is a list."""
        if hst: print('host_ip: {}'.format(hst))
        if dmn_ct: print('domain_count: {}'.format(dmn_ct) )
        if dmns:
            print('domains:')
            for domain in dmns:
                print('  {}'.format(domain))


    print_results(host_ip(json_dict),
                  domain_count(json_dict),
                  domains(json_dict))


## Sample JSON reverseip response:
#
# JSON Response (output=xml) SAMPLE
#
# {
#     "query": {
#         "tool": "reverseip_PRO",
#         "host": "199.59.148.10"
#     },
#     "response": {
#         "domain_count": "4",
#         "domains": [
#             {
#                 "name": "gezwitscher.com",
#                 "last_resolved": "2011-04-04"
#             },
#             {
#                 "name": "twitter.com",
#                 "last_resolved": "2011-04-04"
#             },
#             {
#                 "name": "twitterfriendblaster.com",
#                 "last_resolved": "2012-01-11"
#             },
#             {
#                 "name": "twttr.com",
#                 "last_resolved": "2012-02-21"
#             }
#         ]
#     }
# }
