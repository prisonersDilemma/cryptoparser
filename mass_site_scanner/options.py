#!/usr/bin/env python3.6

from argparse import ArgumentParser

from __init__ import (HOME, CACHE, RC_FILE, OUTPUT_FILE, API_KEY, API_SITE)


def parse():
    parser = ArgumentParser(prog='mass_website_scanner.py',
                            description='',
                            epilog='')

    source_type = parser.add_mutually_exclusive_group()
    source_type.add_argument('-cidr', '--cidr-range', nargs=2, metavar='N', help='cidr-range')
    source_type.add_argument('-ip', '--ip-address', metavar='IP', help='ip address')
    source_type.add_argument('-dns', '--dns-name', metavar='URL', help='dns name, (less the protocol)')

    parser.add_argument('--ignore-ssl-cert', default=True, action='store_false',
                        help=('toggle `ignore-ssl-cert`;' 'default: True'))

    parser.add_argument('-i', '--case-insensitive', default=False, action='store_true',
                        help=('case insensitive search for keyword;' 'default: False'))
    parser.add_argument('-k', '--keyword', metavar='STRING', required=True, help='search string')
    parser.add_argument('-p', '--port', nargs='+', default=[80, 443],
                        help=('port(s);' 'default: 80, 443'))
    #parser.add_argument('-r', '--record-type', metavar='TYPE', default='A', choices=['A', 'MX'],
    #                    help=('type of record for a dnsrecord API query; default: A'))
    parser.add_argument('-t', '--throttle', type=int, default=5, metavar='FLOAT',
                        help=('time in secs to throttle checks;' 'default: 5'))

    parser.add_argument('--api-site', default=API_SITE, metavar='URL',
                        help=('url to site api;' 'default: {}'.format(API_SITE)))
    parser.add_argument('--api-key', default=API_KEY, metavar='KEY',
                        help=('api key string associated with site-api;' 'default: {}'.format(API_KEY)))
    parser.add_argument('--api-output', default='json', choices=['xml', 'json'], metavar='TYPE',
                        help=('type of output requested from site-API;' 'defaul: json'))
    parser.add_argument('--api-query', default='reverseip', choices=['reverseip', 'dnsrecord'],
                        metavar='TYPE', help=('type of API query; default: reverseip'))

    parser.add_argument('--set-cache', default=CACHE, metavar='PATH',
                        help=('path to directory to store cached html files;' ' default: {}'.format(CACHE)))
    parser.add_argument('--set-home', default=HOME, metavar='PATH',
                        help=('path to directory to store related program files;' 'default: {}'.format(HOME)))
    parser.add_argument('--set-outfile', default=OUTPUT_FILE, metavar='PATH',
                        help=('file name for output;' 'default: {}'.format(OUTPUT_FILE)))
    parser.add_argument('--set-rcfile', default=RC_FILE, metavar='PATH',
                        help=('path to configuration file;' 'default: {}'.format(RC_FILE)))

    return parser.parse_args()


if __name__ == '__main__':
    print(parse())
