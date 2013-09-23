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
    pprint.pprint(res)
    return 0

if __name__ == "__main__":
    sys.exit(main())
