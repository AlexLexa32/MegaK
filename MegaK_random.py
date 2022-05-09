from tkinter import *

def pr():
    def change():
        import random
        x = ot.get()
        y = do.get()
        z = int(kr.get())
        x = int(x)
        y = int(y)
        a = random.randint(x, y)
        butilka['text'] = a-(a%z)

    oknoa = Tk()
    oknoa.title('генератор случайных чисел')
    oknoa.geometry('350x300+300+200')
    # okno['bg'] = '#a34b72'

    R = Canvas(oknoa, width=350, height=300, bg='#a34b72')
    R.pack()
    R.create_oval((5.4, 80), (35.4, 110), fill='#802951', outline='#802951')
    R.create_oval((90, 200), (130, 240), fill='#802951', outline='#802951')
    R.create_oval((280, 10), (298, 28), fill='#802951', outline='#802951')
    R.create_oval((310, 40), (340, 70), fill='#802951', outline='#802951')
    R.create_oval((280, 200), (305.1, 225.1), fill='#802951', outline='#802951')
    R.create_oval((55, 10.2), (74.5, 29.7), fill='#802951', outline='#802951')
    R.create_oval((4, 270), (23, 289), fill='#802951', outline='#802951')
    R.create_oval((200, 250), (215, 265), fill='#a34b72', outline='#802951')
    R.create_oval((8, 8), (31, 31), fill='#a34b72', outline='#802951')
    R.create_oval((320, 130), (298.9, 108.9), fill='#a34b72', outline='#802951')

    la = Label(oknoa, text='введите минимальное число', bg="#a34b72", fg="#ffffff")
    la.place(x=75, y=3)
    ot = Entry(oknoa, bg='#a34d72', fg='#ffffff')
    ot.place(x=75, y=23)
    lb = Label(oknoa, text='введите максимальное число', bg="#a34b72", fg="#ffffff")
    lb.place(x=75, y=53)
    do = Entry(oknoa, bg='#a34d72', fg='#ffffff')
    do.place(x=75, y=73)
    lc = Label(oknoa, text='кратные числу:', bg="#a34b72", fg="#ffffff")
    lc.place(x = 75, y = 103)
    kr = Entry(oknoa, bg='#a34d72', fg='#ffffff')
    kr.place(x=75, y=123)
    butilka = Label(oknoa, width=23, height=2, bg='#a34d72', fg='#ffffff')
    butilka.place(x=65, y=153)
    knopka = Button(oknoa, text='сгенерировать случайное число', command=change, fg='#a34d72')
    knopka.place(x=50, y=253)

    oknoa.mainloop()

def change():
    import random
    x = ot.get()
    y = do.get()
    x = int(x)
    y = int(y)
    a = random.randint(x, y)
    butilka['text'] = a


okno = Tk()
okno.title('генератор случайных чисел')
okno.geometry('350x300+150+100')
# okno['bg'] = '#a34b72'

R = Canvas(okno, width=350, height=300, bg='#a34b72')
R.pack()
R.create_oval((5.4, 80), (35.4, 110), fill='#802951', outline='#802951')
R.create_oval((90, 200), (130, 240), fill='#802951', outline='#802951')
R.create_oval((280, 10), (298, 28), fill='#802951', outline='#802951')
R.create_oval((310, 40), (340, 70), fill='#802951', outline='#802951')
R.create_oval((280, 200), (305.1, 225.1), fill='#802951', outline='#802951')
R.create_oval((55, 10.2), (74.5, 29.7), fill='#802951', outline='#802951')
R.create_oval((4, 270), (23, 289), fill='#802951', outline='#802951')
R.create_oval((200, 250), (215, 265), fill='#a34b72', outline='#802951')
R.create_oval((8, 8), (31, 31), fill='#a34b72', outline='#802951')
R.create_oval((320, 130), (298.9, 108.9), fill='#a34b72', outline='#802951')

la = Label(okno, text='введите минимальное число', bg="#a34b72", fg="#ffffff")
la.place(x=75, y=3)
ot = Entry(okno, bg='#a34d72', fg='#ffffff')
ot.place(x=75, y=23)
lb = Label(okno, text='введите максимальное число', bg="#a34b72", fg="#ffffff")
lb.place(x=75, y=53)
do = Entry(okno, bg='#a34d72', fg='#ffffff')
do.place(x=75, y=73)
butilka = Label(okno, width=23, height=2, bg='#a34d72', fg='#ffffff')
butilka.place(x=65, y=103)
knopka = Button(okno, text='сгенерировать случайное число', command=change, fg='#a34d72')
knopka.place(x=50, y=143)
qbutilka = Button(okno, text='вызвать генератор с делимостью', command = pr, fg='#a34b72')
qbutilka.place(x = 50, y = 180)


okno.mainloop()
