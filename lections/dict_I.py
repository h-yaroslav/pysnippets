#!/usr/bin/python
# -*- coding: latin-1 -*-

# Словарь (хэш, ассоциативный массив) - это изменчивая структура
# данных для хранения пар ключ-значение, где значение однозначно
# определяется ключом. В качестве ключа может выступать неизменчивый
# тип данных (число, строка, кортеж и т.п.).
# Порядок пар ключ-значение произволен.
import os, sys

d = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
d0 = {0: 'zero'}
print d[1]        # берется значение по ключу
d[0] = 0          # присваивается значение по ключу
del d[0]          # удаляется пара ключ-значение с данным ключом
print d
for key, val in d.items():   # цикл по всему словарю
  print key, val
for key in d.keys():   # цикл по ключам словаря
  print key, d[key]
for val in d.values():   # цикл по значениям словаря
  print val
d.update(d0)  # пополняется словарь из другого
print len(d)  # количество пар в словаре 


dd = {'hello1': 'one', 'hello2': 'two', 'hello3': 'three', 'hello4': 'four'}
print "dd['hello3'][0:3]  = ", dd['hello3'][0:3]
print "tiple(dd) = ",  tuple(dd)

rp = {'hello1': 'one', 'hello1': 'two', 'hello1': 'three', 'hello4': 'four'}
print "rp = ", rp
print "rp['hello1'] = ", rp['hello1']

rpp = {'hello1': [10, 20, 30, 40], 'hello2': 'two', 'hello2': 'three', 'hello4': 'four'}
rpp['hello5'] = 'five'
rpp['hello6'] = 'six'
rpp['hello7'] = 'seven'
rpp['hello1'].append(60)

rpp.update(d)

print " keys loop:"
for k in rpp.keys():
    print k
print

print "items loop:"
for k, v in rpp.iteritems():
    print k, "\t \t", v
print

print "dict loop:"
for loop in rpp.iteritems():
    print loop
print
print "rpp = ", rpp
print "len(rpp) = ", len(rpp)
print "rpp.keys() = ", rpp.keys()
kk = dict()
kk[1]='good'
kk[2]='bad'
try:
    kk[3].append('one')
except KeyError, e:
    kk[3] = list()
    kk[3].append('one')
kk[3].append('two')
print kk

lst = list()
lst.append(kk[1])
lst.append('2' + kk[2])
print "lst = ", lst
#print "rpp = ", ",".join(rpp['hello1'])
print "rpp = ", lst[0] + ":" + str(rpp['hello1'])[1:-1]

print rpp
print rpp['hello1'][0]
filename = key[1:-1] for key in rpp.keys()
print filename