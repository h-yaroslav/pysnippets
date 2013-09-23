#!/usr/bin/python

import threading
import time
import socket

def timeout(func, args=(), kwargs={}, timeout_duration=1, default=None):
    """
    ASPN receipe written by dustin lee to call a function with
    a timeout using threads:
    http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/473878

    Small patch: add setDaemon(True) to allow Python to leave whereas the
    thread is not done.
    """
    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = None

        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except:
                self.result = default

    it = InterruptableThread()
    it.setDaemon(True)
    it.start()
    it.join(timeout_duration)
    if it.isAlive():
        return default
    else:
        return it.result



def sayHello():
    i = 0
    while True:
        print i, "Running..."
        time.sleep(0.5)
        i += 1
        if i == 15:
            return "Done. Hello, World!"
        try:
            a = socket.gethostbyname_ex('dggddgdgdgmail.ru')
        except socket.gaierror:
            #pass
            print "Exception raised"
            continue
        print a

if __name__ == "__main__":

    res = timeout(sayHello, timeout_duration=4.0, default='The function has been '
        'interupted')
    print res
