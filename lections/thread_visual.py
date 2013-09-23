#!/usr/bin/python
# -*- coding: utf8 -*-

import threading, time, sys
from Tkinter import Tk, Canvas, Button, LEFT, RIGHT, NORMAL, DISABLED

global champion

# Задается дистанция, цвет полосок и другие параметры
distance = 300
colors = ["Red","Orange","Yellow","Green","Blue","DarkBlue","Violet"]
nrunners = len(colors)      # количество дополнительных потоков
positions = [0] * nrunners  # список текущих позиций
h, h2 = 20, 10              # параметры высоты полосок

def run(n):
  """Программа бега n-го участника (потока)"""
  global champion
  while 1:
    for i in range(10000):           # интенсивные вычисления
      pass
    graph_lock.acquire()
    positions[n] += 1                # передвижение на шаг
    if positions[n] == distance:     # если уже финиш
      if champion is None:           # и чемпион еще не определен,
        champion = colors[n]         # назначается чемпион
      graph_lock.release()
      break
    graph_lock.release()

def ready_steady_go():
  """Инициализация начальных позиций и запуск потоков"""
  graph_lock.acquire()
  for i in range(nrunners):
    positions[i] = 0
    threading.Thread(target=run, args=[i,]).start()
  graph_lock.release()

def update_positions():
  """Обновление позиций"""
  graph_lock.acquire()
  for n in range(nrunners):
    c.coords(rects[n], 0, n*h, positions[n], n*h+h2)
  tk.update_idletasks()  # прорисовка изменений
  graph_lock.release()

def quit():
  """Выход из программы"""
  tk.quit()
  sys.exit(0)

# Прорисовка окна, основы для прямоугольников и самих прямоугольников,
# кнопок для пуска и выхода
tk = Tk()
tk.title("Соревнование потоков")
c = Canvas(tk, width=distance, height=nrunners*h, bg="White")
c.pack()
rects = [c.create_rectangle(0, i*h, 0, i*h+h2, fill=colors[i])
         for i in range(nrunners)]
go_b = Button(text="Go", command=tk.quit)
go_b.pack(side=LEFT)
quit_b = Button(text="Quit", command=quit)
quit_b.pack(side=RIGHT)

# Замок, регулирующий доступ к функции пакета Tk
graph_lock = threading.Lock()

# Цикл проведения соревнований
while 1:
  go_b.config(state=NORMAL), quit_b.config(state=NORMAL)
  tk.mainloop()             # Ожидание нажатия клавиш
  champion = None
  ready_steady_go()
  go_b.config(state=DISABLED), quit_b.config(state=DISABLED)
  # Главный поток ждет финиша всех участников
  while sum(positions) < distance*nrunners:
    update_positions()
  update_positions()
  go_b.config(bg=champion)     # Кнопка окрашивается в цвет победителя
  tk.update_idletasks()
