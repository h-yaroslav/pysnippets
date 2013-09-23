#!/usr/bin/python
# -*- coding: latin-1 -*-

print "Таблица Unicode (русские буквы)".center(18*4)
i = 0
for c in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"\
         "абвгдежзийклмнопрстуфхцчшщъыьэюя":
    u = unicode(c, 'koi8-r')  
    print "%3i: %1s %s" % (ord(u), c, `u`),
    i += 1
    if i % 4 == 0:
	print