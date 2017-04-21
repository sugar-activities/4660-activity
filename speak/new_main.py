#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

import urllib2

def internet_on():
    try:
        response=urllib2.urlopen('http://74.125.113.99',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

print internet_on()