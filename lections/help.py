#!/usr/bin/python
# -*- coding: latin-1 -*-

import __builtin__

def help(object, spacing=10, collapse=1):
    """Выводит методы и строки документации.
    
    В качестве аргумента может использоваться модуль, класс, список, словарь
    или строка."""
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %
                      (method.ljust(spacing),
                       processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])

if __name__ == "__main__":
    print help.__doc__
    
print "***************** List: *****************"
li = []
help(li)
print "**************** Tuple: *****************"
la = ()
help(la)
print "************** Dictionary: **************"
lb = {}
help(lb)
print "**************** String: ****************"
lc = ''
help(lc)
print "***************** int: ******************"
ld = 5
help(ld)
print "**************** float: *****************"
le = 5.56
help(le)
print "**************** builtin: *****************"
help(__builtin__)
print "*****************************************"
