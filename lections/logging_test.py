#!/usr/bin/python

import logging
import sys

def old_main():
    #from common import logutil
    #log = logutil.getStdLogger()
    log = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    log.addHandler(handler)
    log.setLevel(logging.CRITICAL)

    log.debug('This is a debug message')
    log.info('This is an info message')
    log.warning('This is a warning message')
    log.error('This is an error message')
    log.critical('This is a critical error message')

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

def main():
    if len(sys.argv) > 1:
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)
        logging.basicConfig(level=level)
        print "level:", level

    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical error message')


if __name__ == "__main__":
    #old_main()
    main()
    #print help.__doc__

