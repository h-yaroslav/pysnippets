#!/usr/bin/python

## Try to create directory
import os, time, sys

common_directory = '/tmp'

try:
    os.mkdir(os.path.join(common_directory, "B_lock"))
except OSError, e:
    ## Failed: another instance is running
    sys.exit(e)
## Create the PID file
# (...)
try:
    while True:
	time.sleep(2)
    ## Application code
    # (...)
finally:
    ## Remove the PID file
    # (...)
    ## Delete directory
    os.rmdir(os.path.join(common_directory, "B_lock"))
