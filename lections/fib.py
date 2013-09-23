#!/usr/bin/python
# -*- coding: latin-1 -*-

import os, sys

def fib(n): # Вивід чисел Фібоначчі до заданого n
    result = [1]
    a, b = 0, 1
    while b < n:
#	print b,
	a, b = b, a+b
	result.append(b)
    return result


a = fib(1000)

print a