#!/usr/bin/python
# -*- coding: latin1 -*-

import os, sys


s = unicode("Привіт друже", 'utf-8')
print s
#s.decode('utf-8')
print s


"""
for i in range(0, 256):
    print unicode(chr(i), 'koi8-r').encode('utf-8'),
    print chr(i), 
    result = []
    for c in unicode(chr(i), 'koi8-u'):
        try:
            result.append(c.encode('utf-8'))
        except:
            pass
    print ''.join(result)
"""    
    
    
#    print unicode(chr(128), 'cp437').encode('utf-8')