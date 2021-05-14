#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


#   Решите задачу: напишите программу по описанию.
#   Размеры многострочного текстового поля определяются значениями, введенными в однострочные текстовые поля.
#   Изменение размера происходит при нажатии мышью на кнопку, а также при нажатии клавиши Enter.
#   Цвет фона экземпляра Text светлосерый ( lightgrey ), когда поле не в фокусе, и белый, когда имеет фокус.
#   Событие получения фокуса обозначается как <FocusIn> , потери – как <FocusOut>.

# Создаем функцию изменения высоты и ширины
def change(event):
    a = ent1.get()
    b = ent2.get()
    soul['width'] = a
    soul['height'] = b


# Создаем функцию для изменения высоты и ширины
def change_for_button():
    a = ent1.get()
    b = ent2.get()
    soul['width'] = a
    soul['height'] = b


# Создаем функцию получения фокуса и изменения цвета
def focus(event):
    soul['bg'] = 'white'


# Создаем функцию потери фокуса и возвращения цвета
def unfocus(event):
    soul['bg'] = 'lightgrey'


if __name__ == '__main__':

    # Создаем графический интерфейс
    root = Tk()
    root.title('Перемещение текста')
    root.geometry('364x200')

    # Создаем метки
    label1 = Label(root, text="Ширина ", font=35)
    label2 = Label(root, text="Высота ", font=35)

    # Создаем формы для ввода значений
    ent1 = Entry(root, width=10, font=36, justify=CENTER)
    ent2 = Entry(root, width=10, font=36, justify=CENTER)

    # Создаем кнопки для выполнения определенных действий
    button = Button(height=1, width=8, text='Изменить', command=change_for_button)

    # Создаем поле для ввода большого текста
    soul = Text(root, width=5, height=5, bg="lightgrey", wrap=WORD, font=12)

    # Выводим
    ent1.grid(row=1, column=1)
    ent2.grid(row=2, column=1)

    label1.grid(row=1, column=0)
    label2.grid(row=2, column=0)

    button.grid(row=1, column=2, padx=10)

    soul.grid(row=3, column=0)

    # Бинды
    button.bind('<Return>', change)
    soul.bind('<FocusIn>', focus)
    soul.bind('<FocusOut>', unfocus)

    # Запуск программы
    root.mainloop()
