#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

# Создать подобное изображение

if __name__ == '__main__':

    # Создаем графический интерфейс
    root = Tk()
    root.title('Рисунок')
    root.geometry('500x500')

    # Создаем окно Canvas
    c = Canvas(root, width=500, height=400, bg='white')
    c.pack()

    # Создаем различные фигуры
    circle = c.create_oval(383, 18, 450, 84, fill="#FFFF00")
    rectangle = c.create_rectangle(129, 143, 340, 360, fill='#FF0800')
    rectangle1 = c.create_rectangle(164, 166, 301, 215, fill='#14FCF8')
    rectangle2 = c.create_rectangle(226, 165, 236, 215, fill='#524842')
    rectangle3 = c.create_rectangle(198, 282, 248, 360, fill='#524842')
    triangle = c.create_polygon(232, 30, 90, 144, 375, 143, fill='#804040')
    circle = c.create_oval(232, 318, 240, 328, fill="#400000")

    # Создаем цикл, для вывода травы
    x = 0
    while x < 500:
        c.create_arc(x, 455, x+40, 350, start=180, extent=-80, style=ARC, width=3, outline='green')
        x += 15

    # Запуск программы
    root.mainloop()
