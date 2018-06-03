#!/usr/bin/python
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import requests
import sys

TERM=sys.argv[1]
print "Szukamy %s" % TERM
URL="https://www.compart.com/en/unicode/search?q=%s#characters" % TERM
print URL

r = requests.get(URL)
parsed = BeautifulSoup(r.text)
print parsed.body.find('h1').text
print parsed.body.findAll('div', 'table-cell')
