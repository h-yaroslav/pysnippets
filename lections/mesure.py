#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
f1 = open("mesure.txt", "w")

for i in xrange(0, 3600):
    f1.write("111,222,333,444,55,777\n")

f1.close()
