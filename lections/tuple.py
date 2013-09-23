#!/usr/bin/python
# -*- coding: latin-1 -*-

# кортеж
# Для представления константной последовательности
# (разнородных) объектов используется тип кортеж.

p = (1.2, 3.4, 0.9) 
for s in "one", "two", "three":
  print s

print p

one_item = (1,)
empty = ()
p1 = 1, 3, 9
p2 = 3, 8, 5,

print one_item
print empty

p1, p2 = p2, p1

print p1
print p2
