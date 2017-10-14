#!/usr/bin/env python3.6

from setuptools import setup

setup(name='mass_site_sanner',
      version='0.1',
      description='Query domaintools APIs for reverseip & dnsrecords, and scan associated websites for keywords.',
      url='http://github.com/prisonersDilemma/mass_site_scanner',
      author='C.A.Dupin',
      license='MIT',
      packages=['mass_site_scanner', 'httplib2', 'netaddr'],
      zip_safe=False)
