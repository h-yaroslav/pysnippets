#!/usr/bin/python
# -*- coding: latin-1 -*-

# список
# В "чистом" Python нет массивов с произвольным типом элемента.
# Вместо них используются списки.

lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
lst2 = [x**2 for x in range(10) if x % 2 == 1]
lst3 = list("abcde")

print lst1, "SIZE=%i" % len(lst1)
print lst2
print lst3

lst1.reverse()
print lst1

print lst3[0], lst3[-1], lst3[3], lst3[-2],

print
lst = list()
if bool(lst):
    print bool(lst), lst
else:
    print bool(lst), "Empty"

assert bool(lst), "Error"