#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

#   Решите задачу: напишите программу по следующему описанию.
#   Нажатие Enter в однострочном текстовом поле приводит к перемещению текста из него в список (экземпляр
#   Listbox ).
#   При двойном клике ( <Double-Button-1> ) по элементу-строке списка, она должна копироваться в текстовое поле.


# Создаем функцию добавления в список
def add_item(event):
    name = ent.get()
    lbox.insert(0, name)
    ent.delete(0, 'end')


# Создаем функцию удаления из списка и добавления в текстовое поле
def delete_item(event):
    product = []
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        op = lbox.get(i)
        product.append(op)
    for val in product:
        ent.insert(0, val)
    for k in select:
        lbox.delete(k)


if __name__ == '__main__':

    # Создаем графический интерфейс
    root = Tk()
    root.title('Перемещение текста')
    root.geometry('364x200')

    # Создаем формы для ввода значений
    ent = Entry(root, width=20, font=36)

    # Создаем списки с помощью интерфейса
    lbox = Listbox(width=30)

    # Выводим
    ent.grid(row=1, column=1)
    lbox.grid(row=2, column=1, pady=5)

    # Бинды
    ent.bind('<Return>', add_item)
    lbox.bind('<Double-Button-1>', delete_item)

    # Запуск программы
    root.mainloop()
