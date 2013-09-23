#!/usr/bin/python


import pickle, time
mydata = ("abc", 12, [1, 2, 3])
output_file = open("mydata.dat", "w")
p = pickle.Pickler(output_file)
p.dump(mydata) # dump into the file
pstr = pickle.dumps(mydata) # dump into the string
print pstr
output_file.close()
