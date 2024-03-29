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
print "*** ", dd['hello3'][0:3]


print tuple(dd)