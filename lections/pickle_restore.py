#!/usr/bin/python


import pickle
input_file = open("mydata.dat", "r")
mydata = pickle.load(input_file)
print mydata
input_file.close()
