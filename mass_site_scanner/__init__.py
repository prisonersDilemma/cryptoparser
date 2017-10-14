#!/usr/bin/env python3.6

import os


HOME        = os.path.join(os.path.expanduser('~'), 'Desktop/mass_website_scanner')  # Location of things like cache.
CACHE       = os.path.join(HOME, 'cache') # Needed for httplib2.
OUTPUT_FILE = os.path.join(HOME, 'mass_website_scanner.txt')
RC_FILE     = os.path.join(HOME, 'mass_website_scannerrc')
API_KEY     = '' # ADD ME!
API_SITE    = 'https://api.viewdns.info/'

reverseip = 'test_reverseip_json_response.json' # Testing.
dnsrecord = 'test_dnsrecord_json_response.json' # Testing.
JSON_REVERSEIP_RESPONSE_FILE = os.path.join(CACHE, reverseip)
JSON_DNSRECORD_RESPONSE_FILE = os.path.join(CACHE, dnsrecord)
