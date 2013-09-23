#!/usr/bin/python 
# -*- coding: latin-1 -*- 
 
def swiss_knife(arg1, *args, **kwargs):
    print arg1
    print args
    print kwargs
    return None
    
"""
print swiss_knife(1)
print swiss_knife(1, 2, 3, 4, 5)
print swiss_knife(1, 2, 3, a='abc', b='sdf')
# print swiss_knife(1, a='abc', 3, 4)  # !!! ошибка
"""
lst = [2, 3, 4, 5]
dct = {'a': 'abc', 'b': 'sdf'}

print swiss_knife(1, *lst, **dct)
