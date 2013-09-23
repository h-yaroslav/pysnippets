#!/usr/bin/python
# -*- coding: latin-1 -*-

import time
import random

HOURS = 1
TIME = HOURS*3600

dat = dict()
d = list()
a = (1250610626, 1250610626-3600*24)

#for i in xrange(min(a),max(a),TIME):
for i in xrange(min(a),max(a)):
    d.append(i)
    #print time.ctime((i/TIME)*TIME)
for i in d:
    dat[i] = int(random.random()*100)

# Collect and sum values for each hour
res = dict()
print dat
for ts, val in dat.items():
    th = (ts/TIME)*TIME
    # !!! increase value if exists
    res[th] = res.get(th,0) + val

# !!! append dictionary
#d = {'a':[], 'b': {}}
#d.setdefault('a',[]).appen(1)
#d.setdefault('b', {})['val'] = 1

print res
