#!/usr/bin/python

if __name__ == '__main__':
    import getopt
    import sys
    import os
 
    usage = 'usage: %s -m master [[-m master1]...] \
-s slave [[-s slave1]...] [-t time]' % (os.path.basename(sys.argv[0])) 

    try:
        opts, args = getopt.getopt(sys.argv[1:],
                "m:s:t:", ["master=", "slave=", "time="])
    except getopt.GetoptError, e:
        print usage
        sys.exit(1)

    if len(opts) < 1:
        print "No options"
        sys.exit(1)

    print opts
    print len(opts)

    for o, a in opts:
        if o in ('-m', '--master'):
            print "option: ", o, a
        if o in ('-s', '--slave'):
            print "option: ", o, a
        if o in ('-t', '--threshold'):
            print "option: ", o, a

