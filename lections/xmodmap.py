#!/usr/bin/python
# -*- coding: latin-1 -*-

import os
import sys

#xkeymap.keycode.108 = 0×138 # Alt_R
#xkeymap.keycode.106 = 0×135 # KP_Divide
#xkeymap.keycode.104 = 0×11c # KP_Enter
f1 = open("xmodmap.txt", "r")
for line in f1.readlines():
    ll = line.strip().split(" ")
    #print ll
    try:
        num, code, name = ll[0], ll[4], ll[5]
    except IndexError:
        code = ''
        name = ''
    print "xkeymap.keycode.%s = %s # %s" % (num.strip(), code.strip(),
            name.strip())

f1.close()
