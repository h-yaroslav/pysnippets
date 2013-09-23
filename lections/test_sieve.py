#!/usr/bin/python
# -*- coding: latin-1 -*-

# file: test_Sieve.py
import sieve, sets
import unittest
 
class TestSieve(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def testone(self):
        primes = Sieve.primes(1)
        self.assertEqual(primes, sets.Set())
 
    def test100(self):
        primes = Sieve.primes(100)
        self.assert_(primes == sets.Set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
                53, 59, 61, 67, 71, 73, 79, 83, 89, 97]))
 
if __name__ == '__main__':
    unittest.main()
