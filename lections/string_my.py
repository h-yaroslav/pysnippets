#!/usr/bin/python
# -*- coding: koi8-r -*-

lst1 = list("ниавд")

print lst1

lst1.reverse()
print lst1

s = unicode("ниавд", "utf-8")
print s

for i in s:
    for j in s:
        for k in s:
            for l in s:
                for m in s:
                    print i + j + k + l + m

