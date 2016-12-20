#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import urllib2
from time import time

url = 'https://www.arin.net/simplewebutils/whatsmyip.html?_=%s'
ip4_pattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

try:
    resp = urllib2.urlopen(url % int(1000 * time()))
    ip4 = ip4_pattern.search(resp.read()).group()
except Exception as e:
    print(e)
    ip4 = ''
print(ip4)
