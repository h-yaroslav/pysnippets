#!/usr/bin/python

import os, time, sys

top = './'
datefmt = "%Y/%m/%d %H:%M"
#name = time.strftime(datefmt, namelist)

try:
    for root, dirs, files in os.walk(top, topdown=False):
    #for name in files:
        #print os.path.join(root, name)
        #print os.stat(os.path.join(root, name))
	for name in dirs:
            dirname=os.path.join(root, name)
	    print dirname
    	    #print os.stat(dirname).st_ctime
            #print "edge =", time.time() - os.stat(dirname).st_ctime, " seconds"
	    #stat = list(os.stat(dirname))
            #stat[7]=time.strftime(datefmt, time.localtime(stat[7]))
	    #stat[8]=time.strftime(datefmt, time.localtime(stat[8]))
            #stat[9]=time.strftime(datefmt, time.localtime(stat[9]))
	    #print stat
except ValueError, e:
    sys.exit(e)

