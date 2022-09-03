from turtle import Turtle, bgcolor
from math import *
from tkinter import *


root = Tk()
t = Turtle()
function = 'sin(x)*10'


def start():
    global function
    function = input_record.get()
    for i in range(-350, 350):
        y_record = ''
        for elem in function:
            if elem == 'x':
                y_record += str(i)
            else:
                y_record += elem
        y = eval(y_record)
        t.setposition(i, y)
        t.down()


def clear():
    t.clear()


root.title('управление')
root.geometry('250x250')
r = Canvas(root, bg='#074452', width=250, height=250)
r.pack()
photo = PhotoImage(file="megak_logo.png")
r.create_image(0, 0, anchor=NW, image=photo)
Label(root, text='y=', bg='#074452', fg='#fbb').place(x=32, y=4)
input_record = Entry(root, bg='#889988')
input_record.place(x=55, y=2)
Button(root, text='пуск', command=start).place(x=20, y=40)
Button(root, text='очистить', command=clear).place(x=120, y=40)

bgcolor("#111")
t.pencolor("#78912f")
t.speed(0)
t.up()


mainloop()
root.mainloop()
