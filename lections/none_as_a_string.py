#!/usr/bin/python
# -*- coding: latin-1 -*-
a = {'info': 'tcp/ip', 'type': None, 'sig': 'None'}
n = {'None': None}

# return None no matter 'None' or None is given
b = n.get(a.get('info'), a.get('info'))

