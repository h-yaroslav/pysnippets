#!/usr/bin/python

from threading import Thread

"""
# PythonDecorators/decorator_with_arguments.py
class decorator_with_arguments(object):

    def __init__(self):
        print("Inside __init__()")
        self.arg1 = '### Hello, World! ###'

    def __call__(self, f):
        print("Inside __call__()")
        def wrapped_f(*args):
            f(self.arg1, *args)
        return wrapped_f

@decorator_with_arguments()
def sayHello(to_kill, a2, a3, a4):
    print "Receive arg:", to_kill
    print('sayHello arguments:', a1, a2, a3, a4)

sayHello("say", "hello", "argument")
print("after first sayHello() call")
sayHello("a", "different", "set of")
"""
to_kill = None

class InterruptableThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.result = None
        global to_kill
        to_kill = False

    """
    def __call__(self, f):
        print("Inside __call__()")
        def wrapped_f(*args):
            f(self.to_kill, *args)
        return wrapped_f

    def run(self):
        try:
            self.result = target(*args, **kwargs)
        except:
            self.result = None
    """

def sayHello():
    print "Receive arg:", to_kill
    print('sayHello arguments')
    return "Hello"

if __name__ == "__main__":

    it = InterruptableThread()
    it.start()
    it.join(2)

    if it.isAlive():
        print 'Still working...'
    else:
        print it.result
