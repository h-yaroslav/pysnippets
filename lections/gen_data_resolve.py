#!/usr/bin/python

import time
import random
import sys


HOUR = 60*60
DAY = 24*HOUR

def gen_data():
    """ Generate dict {timestamp: rand, ...}
    """

    data = dict()
    end = int(time.time())
    start = end - DAY
    for i in xrange(start,end):
        data[i] = int(random.random()*100)

    return data


def main():
    import pprint
    res = gen_data()
    
    ress = dict()
    for i,j in res.items():
        ts = (i/HOUR)*HOUR
        #ress[ts] = ress.get(ts,0) + j
        key = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))
        ress[key] = ress.get(key,0) + j
    pprint.pprint(ress)
    print len(ress)
    return 0

if __name__ == "__main__":
    sys.exit(main())
