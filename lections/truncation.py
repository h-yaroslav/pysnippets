s = range(10)
print s
print "s[0:3] :\t\t", s[0:3]
print "s[-1:] :\t\t", s[-1:]
print "s[::3] :\t\t", s[::3]
s[0:0] = [-1, -1, -1]
print "s[0:0] = [-1, -1, -1] :\t", s
del s[2:5]
print "del s[1:3] :\t\t", s
