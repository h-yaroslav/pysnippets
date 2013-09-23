#!/usr/bin/python

import os
import time

#print os.path.isfile('path.py')

print os.path.exists('/root')
#while True:
print os.path.exists('/mnt/maxima/temp')
#print os.path.isdir('/root/Desktop')

print time.time()
print time.localtime(time.time())

t = ("3", "hello", "55", "zzz")
print t
print "/".join(t)

#dirname = "/".join(time.localtime(time.time())[0:4])
#print dirname

datefmt = "%Y/%m/%d/%H/%M"
dirname = time.strftime(datefmt, time.localtime(time.time()))
print dirname

#for i in range(60):
#    print int(i/10)               

print "**************************"
namelist = list(time.localtime())
namelist[4] = int(namelist[4]/10)
print namelist
datefmt = "/%Y/%m/%d/%H/%M"
name = time.strftime(datefmt, namelist)
print name
