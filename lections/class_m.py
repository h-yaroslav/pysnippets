#!/usr/bin/python
# -*- coding: latin-1 -*-

class C:
    def __init__(self, N):
        self.a = N

    #@classmethod
    @staticmethod
    def f():
        print "Call f()", a

if __name__ == "__main__":
    #C.f()
    b = C("Yo")
    b.f()

