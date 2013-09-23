#!/usr/bin/python
# -*- coding: latin-1 -*-



mydata = [(1, 2, 3), (1, 3, 4)]
import csv

# Запись в файл:
f = file("my.csv", "w") 
writer = csv.writer(f)
for row in mydata:
    writer.writerow(row)
f.close()

# Чтение из файла:
reader = csv.reader(file("my.csv"))
for row in reader:
    print row
