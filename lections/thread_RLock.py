#!/usr/bin/python

import threading
import os, sys

words_cnt = dict()
def open_file(name):
    f = open(name, "r")
    try:
        for line in f:
            ll = line.strip('\n')
            words_cnt[ll] = words_cnt.get(ll, 0) + 1
    finally:
        f.close()


thread1 = threading.Thread(target=open_file, args=['dict.txt'])
thread2 = threading.Thread(target=open_file, args=['dict.txt'])
thread3 = threading.Thread(target=open_file, args=['dict.txt'])
__lock = threading.RLock()
__lock.acquire()
thread1.start()
__lock.release()
__lock.acquire()
thread2.start()
__lock.release()
__lock.acquire()
thread3.start()
__lock.release()
print words_cnt
