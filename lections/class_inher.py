#!/usr/bin/python

class A(object):
    def test(self):
        print "running A().test()"

class B(A):
    def test(self):
        print "running B().test()"
        super(B, self).test()

class C(A):
    def test(self):
        print "running C().test()"
        super(C, self).test()

class D(B, C):
    hello = 1
    def test(self):
        print "running D().test()"
        super(D, self).test()

if __name__ == "__main__":
    d = D()
    d.test()
    print D.__mro__

