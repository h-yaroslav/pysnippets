#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
f1 = open("file1.txt", "r")
f2 = open("file2.txt", "w")
for line in f1.readlines():
  f2.write(line, )
  f2.write("+++",)
print type(line)

f2.close()
f1.close()
