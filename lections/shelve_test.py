#!/usr/bin/python
# -*- coding: latin-1 -*-


import shelve
data = ("abc", 12)      # - данные (объект)
key = "key"             # - ключ (строка)
filename = "polka.dat"  # - имя файла для хранения полки
d = shelve.open(filename)       # открытие полки
d[key] = data           # сохранить данные под ключом key 
                        # (удаляет старое значение, если оно было)
data = d[key]           # загрузить значение по ключу 
len(d)                  # получить количество объектов на полке
d.sync()                # запись изменений в БД на диске
print d
del d[key]              # удалить ключ и значение
flag = d.has_key(key)   # проверка наличия ключа
lst = d.keys()          # список ключей 
d.close()               # закрытие полки
