#!/usr/bin/env python3.6

# standard library
import sys #noqa

# pypi
import httplib2

# local
from __init__ import CACHE
import searches



def query(url, cache=CACHE):
    """Return a GET request of a url as string."""
    response, content = httplib2.Http(cache).request(url)
    return content.decode('utf-8')


def scan_with_dns_name(dns_name, cache=CACHE, keyword=None):
    return searches.search_html(keyword, query(dns_name, cache))


def scan_with_cidr_range(cidr_range, cache=CACHE, keyword=None):
    pass


def scan_with_ip_address(ip_address, cache=CACHE, keyword=None):
    pass


if __name__ == '__main__':
    pass
