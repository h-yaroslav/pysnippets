#!/usr/bin/python
# -*- coding: latin-1 -*-

import os, sys


def Denary2Binary(n):
    '''convert denary integer n to binary string bStr'''
    bStr = ''
    if n < 0:  raise ValueError, "must be a positive integer"
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr

if __name__ == "__main__":

    for i in range(1, 38):
        print i, ":\t", Denary2Binary(i)

