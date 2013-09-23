#!/usr/bin/python
# -*- coding: latin-1 -*-

#import __builtin__

def my_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
        return mod
        
print my_import("os")
