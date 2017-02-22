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
https://docs.google.com/spreadsheets/d/1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/pubhtml
# It's not easy to determine what URL parameters Google makes available for a
# Google Spreadsheet that has been 'published'. Here's some dope:
# http://stackoverflow.com/questions/23446449/google-sheet-embed-url-
# documentation.
# 
# Here's some more useful dope:
# http://acrl.ala.org/techconnect/post/query-a-google-spreadsheet-like-a-
# database-with-google-visualization-api-query-language
# 
# this URL will take you to the published spreadsheet:
# https://docs.google.com/spreadsheets/d/
# 1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/edit#gid=0
# 
# You can get a plain html representation here:
# https://docs.google.com/spreadsheets/d/
# 1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/pubhtml
# 
# You can also get jsonp (json with padding) from a URL that looks like this:
# href="https://spreadsheets.google.com/feeds/list/
# 1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic?alt=json-in-
# script"
# 
# You can also get some sort of xml, like this:
# https://spreadsheets.google.com/feeds/list/
# 1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic?format=xml
# 
# inexplicably, you get the same result if you specify format=csv or just:
# https://spreadsheets.google.com/feeds/list/
# 1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic
# 
# for our purposes here, some prettyprinted json is easiest to work with:
# https://spreadsheets.google.com/feeds/list/
# 1OPNQC3xBp3iQTpjVfd6cpvvA0BpHWhb3QiNOvGFZ9z8/od6/public/basic?prettyprint=true
# &alt=json

# our sample spreadsheet looks like this:
# 
# Sample Spreadsheet : Sheet1
# 
# name	    city	        state	zip
# ***************************************
# bob	    Seattle	        Wa	    98116
# carol	    San Francisco	Ca	    62742
# ted	    Detroit	        Mi	    48104
# alice	    Denver	        Co	    54321


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
