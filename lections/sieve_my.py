#!/usr/bin/python
# -*- coding: latin-1 -*-

import sets
import math
"""Модуль для вычисления простых чисел от 2 до N """
def primes(N):
  """Возвращает все простые от 2 до N"""
  sieve = sets.Set(range(2, N))
  print "math.sqrt(N)", math.sqrt(N)
  for i in range(2, math.sqrt(N)):
    print i,
    if i in sieve:
      sieve -= sets.Set(range(2*i, N, i))
  print
  print
  return sieve

#print primes(1000)
#profile.run("Sieve.primes(100000)")

