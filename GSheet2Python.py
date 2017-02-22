#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import requests
import urllib2
from pprint import pprint
import re
import json

"""
takes Google's json encoded spreadsheet and prints a python dictionary keyed by
the values in the first column of the SS.
"""



ssURL = "https://spreadsheets.google.com/feeds/list/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic?prettyprint=true&alt=json"

response = urllib2.urlopen(ssURL)
stringIn = response.read()
SSin = json.loads(stringIn)
entry_list = SSin['feed']['entry']
fields = ["name", "city", "state", "zip"]

SSdict = {}

def parsestring(rowstring, fields):
    """yields tuples of (fieldname, fieldvalue)"""
    i = iter(fields[1:])
    field = i.next()
    start = end = 0
    try:
        while True:
            lastfield = field
            field = i.next()
            if rowstring.find(field) == -1:
                field = lastfield
                continue
            end = rowstring.find(field)
            yield lastfield, re.sub('^.*?:', '', rowstring[start:end].strip().strip(',')).strip()
                    
            start = end
    
    except StopIteration:
        start = rowstring.find(field)
        yield lastfield, re.sub('^.*?:', '', rowstring[start:].strip().strip(',')).strip()
        
for e in entry_list:
    entrydict = dict([x for x in parsestring(e['content']['$t'], fields)])
    SSdict[e['title']['$t']] = entrydict


print stringIn
#pprint(SSdict)
