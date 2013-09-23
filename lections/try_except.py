#!/usr/bin/python
# -*- coding: latin-1 -*-

import os, sys

a = {1:'a', 2:'b', 3:'c'}
try:
    zz = a[4]
except KeyError, e:
    raise e
else:
    print "Hello"

