#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys

#for i in range(0, 256):
#    print chr(i)


print unicode('Привіт всім. Як справи?', 'utf-8').encode('utf-8'),

"""
    print chr(i), 
    result = []
    for c in unicode(chr(i), 'cp437'):
        try:
            result.append(c.encode('utf-8'))
        except:
            pass
    print ''.join(result)
"""    
    
    
#    print unicode(chr(128), 'cp437').encode('utf-8')