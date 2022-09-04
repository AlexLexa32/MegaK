from tkinter import Tk, Canvas, Label, Button, Entry
import random
import turtle
import math

#   :)
# все функции 1 окна
def F1():
    x = float(a.get())
    y = float(b.get())
    if x + y < 10 ** 30:
        l['text'] = "ответ:", round(x + y, 5)
    else:
        l['text'] = "слишком большое число"


def F2():
    x = float(a.get())
    y = float(b.get())
    if x - y < 10 ** 30:
        l['text'] = "ответ:", round(x - y, 5)
    else:
        l['text'] = "слишком большое число"


def F3():
    x = float(a.get())
    y = float(b.get())
    if x / y < 10 ** 30:
        l['text'] = "ответ:", round(x / y, 5)
    else:
        l['text'] = "слишком большое число"


def F4():
    x = float(a.get())
    y = float(b.get())
    if x * y < 10 ** 30:
        l['text'] = "ответ:", round(x * y, 5)
    else:
        l['text'] = "слишком большое число"


def F5():
    x = float(a.get())
    y = float(b.get())
    if x * y / 100 < 10 ** 30:
        l['text'] = "ответ:", round(x * y / 100, 5)
    else:
        l['text'] = "слишком большое число"


def F6():
    x = float(a.get())
    y = float(b.get())
    if x ** y < 10 ** 30:
        l['text'] = "ответ:", round(x ** y, 5)
    else:
        l['text'] = "слишком большое число"


def F7():
    x = float(a.get())
    y = float(b.get())
    if x * y / 1000 < 10 ** 30:
        l['text'] = "ответ:", round(x * y / 1000, 5)
    else:
        l['text'] = "слишком большое число"


def F8():
    x = float(a.get())
    y = float(b.get())
    l['text'] = "ответ:", round(x ** (1 / y), 5)


def okno():
    def change():
        x = ot.get()
        y = do.get()
        x = int(x)
        y = int(y)
        a = random.randint(x, y)
        butilka['text'] = a

    okno = Tk()
    okno.title('генератор случайных чисел')
    okno.geometry('350x300+150+100')
    okno.resizable(0, False)

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

    okno.mainloop()


def New():
    # все функции 2 окна
    def fun1():
        G = float(k.get())
        laba['text'] = G ** 2

    def fun2():
        G = float(k.get())
        laba['text'] = G ** 3

    def fun3():
        G = float(k.get())
        laba['text'] = G ** 0.5

    def fun4():
        G = float(k.get())
        laba['text'] = G ** (1 / 3)

    def fun5():
        G = float(k.get())
        G = math.sin(math.radians(G))
        laba['text'] = round(G, 15)

    def fun6():
        G = float(k.get())
        G = math.cos(math.radians(G))
        laba['text'] = round(G, 15)

    def fun7():
        G = float(k.get())
        G = math.tan(math.radians(G))
        laba['text'] = round(G, 15)

    def fun8():
        G = float(k.get())
        G = math.tan(math.radians(G))
        laba['text'] = round(1/G, 15)

    def fun9():
        G = int(k.get())
        n = 1
        for i in range(1, G+1):
            n = n*i
        laba['text'] = n

    def fun10():
        G = int(k.get())
        n = 0
        while G!=0:
            n = n+G%10
            G = G//10
        laba['text'] = n

    def fun11():
        G = float(k.get())
        laba['text'] = math.log2(G)

    def fun12():
        G = float(k.get())
        laba['text'] = G**4

    def fun13():
        G = float(k.get())
        laba['text'] = math.log10(G)

    def fun14():
        G = float(k.get())
        laba['text'] = G**0.25

    window = Tk()
    window.title("калькулятор")
    window.geometry('250x300')
    window['bg'] = '#f2bb0c'
    #x33window.resizable(0, False)

    oval = Canvas(window, width=250, height=300, bg='#f2bb0c')
    oval.pack()
    oval.create_oval((4, 4), (27, 27), fill='#d0990a', outline='#d0990a')
    oval.create_oval((10, 90), (21.1, 101.1), fill='#d0990a', outline='#d0990a')
    oval.create_oval((25, 110), (40, 125), fill='#d0990a', outline='#d0990a')
    oval.create_oval((10, 200), (30.7, 220.7), fill='#d0990a', outline='#d0990a')
    oval.create_oval((30, 270), (45, 285), fill='#d0990a', outline='#d0990a')
    oval.create_oval((220, 20), (239, 39), fill='#d0990a', outline='#d0990a')
    oval.create_oval((230, 111), (247.1, 128.1), fill='#d0990a', outline='#d0990a')
    oval.create_oval((215, 190), (225, 200), fill='#d0990a', outline='#d0990a')
    oval.create_oval((220, 270), (241, 291), fill='#d0990a', outline='#d0990a')
    oval.create_oval((130, 285), (140, 295), fill='#f2bb0c', outline='#d0990a')
    oval.create_oval((10, 140), (31.2, 161.2), fill='#f2bb0c', outline='#d0990a')
    oval.create_oval((230, 60), (215, 75), fill='#f2bb0c', outline='#d0990a')

    lab = Label(window, bg='#f2bb0c', text='введите число', fg='#905506')
    lab.place(x=80, y=3)
    k = Entry(window, bg='#d0990a')
    k.place(x=30, y=23)
    label = Label(window, bg='#f2bb0c', text='выбирете действие', fg='#905506')
    label.place(x=65, y=53)
    kv = Button(window, bg='#d0990a', text='x²', command=fun1)
    kv.place(x=50, y=73)
    kva = Button(window, bg='#d0990a', text='x³', command=fun2)
    kva.place(x=100, y=73)
    kvb = Button(window, bg='#d0990a', text='√x', command=fun3)
    kvb.place(x=50, y=101)
    kvc = Button(window, bg='#d0990a', text='∛x', command=fun4)
    kvc.place(x=100, y=101)
    kvd = Button(window, bg='#d0990a', text='sin(x)', command=fun5)
    kvd.place(x=50, y=129)
    kve = Button(window, bg='#d0990a', text='cos(x)', command=fun6)
    kve.place(x=50, y=157)
    kvf = Button(window, bg='#d0990a', text='tg(x)', command=fun7)
    kvf.place(x=50, y=185)
    kvg = Button(window, bg='#d0990a', text='ctg(x)', command=fun8)
    kvg.place(x=50, y=213)
    kvh = Button(window, bg='#d0990a', text='x!', command=fun9)
    kvh.place(x = 150, y = 73)
    kvi = Button(window, bg='#d0990a', text='∑', command=fun10)
    kvi.place(x=130, y=157)
    kvi = Button(window, bg='#d0990a', text='log₂(x)', command=fun11)
    kvi.place(x=125, y=129)
    kvj = Button(window, bg='#d0990a', text='x⁴', command=fun12)
    kvj.place(x=150, y=101)
    kvk = Button(window, bg='#d0990a', text='log₁₀(x)', command=fun13)
    kvk.place(x=120, y=185)
    kvl = Button(window, bg='#d0990a', text='∜x', command=fun14)
    kvl.place(x=125, y=213)
    laba = Label(window, bg='#f2bb0c')
    laba.place(x=80, y=269)

    window.mainloop()


def weh():
    # все функции 3 окна

    def up():
        T.up()

    def down():
        T.down()

    def zv():
        xp = float(voda.get())
        yp = float(vodb.get())
        T.setposition(xp, yp)

    T = turtle.Turtle()
    turtle.bgcolor("#55dd55")
    T.pencolor("#8810bd")
    T.speed(1)
    T.left(42)
    turtle.title("построение графиков")

    dino = Tk()
    dino.title('управление')
    dino.geometry('200x200')
    dino['bg'] = '#55dd55'
    dino.resizable(0, False)

    krugi = Canvas(dino, bg='#55dd55')
    krugi.pack()
    krugi.create_oval((40, 55), (55, 70), fill='#33bb33', outline='#33bb33')
    krugi.create_oval((150, 150), (172, 172), fill='#33bb33', outline='#33bb33')
    krugi.create_oval((10, 120), (30, 140), fill='#55dd55', outline='#33bb33')
    krugi.create_oval((170, 5), (185, 20), fill='#55dd55', outline='#33bb33')
    krugi.create_oval((30, 5), (50, 25), fill='#55dd55', outline='#33bb33')

    tea = Label(dino, bg='#55dd55', text='введите X')
    tea.place(x=58, y=5)
    voda = Entry(dino, bg='#33bb33')
    voda.place(x=4, y=25)
    teb = Label(dino, bg='#55dd55', text='введите Y')
    teb.place(x=58, y=55)
    vodb = Entry(dino, bg='#33bb33')
    vodb.place(x=4, y=75)
    kn = Button(dino, text='пуск', command=zv, bg='#33bb33')
    kn.place(x=68, y=105)

    knup = Button(dino, bg='#33bb33', command=up, text='поднять перо')
    knup.place(x=5, y=135)
    kndown = Button(dino, bg='#33bb33', command=down, text='опустить перо')
    kndown.place(x=5, y=165)

    turtle.mainloop()
    dino.mainloop()


def prst():
    # все функции 4 окна
    def skorost():
        # расчёты по формулам
        def changea():
            x = qef.get()
            y = tet.get()
            x = float(x)
            y = float(y)
            x = x * 10000
            z = x // y
            z = z / 10000
            label['text'] = round(z, 7), 'м/с'
            print(':)')
            print(' ')

        # параметры окна
        a = Tk()
        a.title('расчёт скорости')
        a['bg'] = '#c2b48c'
        a.wm_attributes('-alpha', 0.9)
        a.geometry("400x250+200+300")
        a.resizable(0, False)
        text1 = Label(a, text='     введите путь в метрах       ', bg='#c2b48c', font=40)
        text1.pack()
        qef = Entry(a, bg='#c2b48c')
        qef.pack()
        text2 = Label(a, text='   введите врямя в секундах   ', bg='#c2b48c', font=40)
        text2.pack()
        tet = Entry(a, bg='#c2b48c')
        tet.pack()
        button = Button(a, text='    кнопка                ', bg='#c2b48c', command=changea)
        button.pack()
        label = Label(a, width=21, height=2, bg='#c2b48c')
        label.pack()
        a.mainloop()

    def davlenie():
        def changeb():
            x = qef.get()
            y = tet.get()
            x = float(x)
            y = float(y)
            x = x * 10000
            z = x // y
            z = z / 10000
            label['text'] = round(z, 7), 'паскаль'
            print(':)')
            # //print(' ')

        b = Tk()
        b.title('расчёт давления')
        b['bg'] = '#c2b48c'
        b.wm_attributes('-alpha', 0.9)
        b.geometry("400x250+200+300")
        b.resizable(0, False)
        text1 = Label(b, text='    введите силу в ньютонах    ', bg='#c2b48c', font=40)
        text1.pack()
        qef = Entry(b, bg='#c2b48c')
        qef.pack()
        text2 = Label(b, text='введите площадь в кв. метрах', bg='#c2b48c', font=40)
        text2.pack()
        tet = Entry(b, bg='#c2b48c')
        tet.pack()
        button = Button(b, text='                кнопка                ', bg='#c2b48c', command=changeb)
        button.pack()
        label = Label(b, width=21, height=2, bg='#c2b48c')
        label.pack()
        b.mainloop()

    def teplo():
        def afa():
            y = 340000
            x = float(qef.get())
            z = x * y / 1000
            label['text'] = round(z, 7), 'кДж'
        def bfa():
            y = 87000
            x = float(qef.get())
            z = x * y / 1000
            label['text'] = round(z, 7), 'кДж'
        def cfa():
            y = 12000
            x = float(qef.get())
            z = x * y / 1000
            label['text'] = round(z, 7), 'кДж'
        def dfa():
            y = 210000
            x = float(qef.get())
            z = x * y / 1000
            label['text'] = round(z, 7), 'кДж'
        def efa():
            y = 110000
            x = float(qef.get())
            z = x * y / 1000
            label['text'] = round(z, 7), 'кДж'
        def ffa():
            y = 67000
            x = float(qef.get())
            z = x * y / 1000
            label['text'] = round(z, 7), 'кДж'
        def gfa():
            y = 25000
            x = float(qef.get())
            z = x * y / 1000
            label['text'] = round(z, 7), 'кДж'
        def hfa():
            y = 84000
            x = float(qef.get())
            z = x * y / 1000
            label['text'] = round(z, 7), 'кДж'

        # параметры окна
        c = Tk()
        c.title('расчёт количество теплоты при плавлении')
        c['bg'] = '#c2b48c'
        c.wm_attributes('-alpha', 0.9)
        c.geometry("400x340+200+300")
        c.resizable(0, False)

        text1 = Label(c, text='выберете вешевство', bg='#c2b48c', font=40)
        text1.pack()

        # блок с этими круглами штуками вобшем
        a11 = Button(c, text="лёд", command = afa, bg='#c2b48c')
        b11 = Button(c, text="серебро", command = bfa, bg='#c2b48c')
        c11 = Button(c, text="ртуть", command = cfa, bg='#c2b48c')
        d11 = Button(c, text="медь", command = dfa, bg='#c2b48c')
        e11 = Button(c, text="спирт", command = efa, bg='#c2b48c')
        f11 = Button(c, text="золото", command = ffa, bg='#c2b48c')
        g11 = Button(c, text="свинец", command = gfa, bg='#c2b48c')
        h11 = Button(c, text="сталь", command = hfa, bg='#c2b48c')
        a11.pack()
        b11.pack()
        c11.pack()
        d11.pack()
        e11.pack()
        f11.pack()
        g11.pack()
        h11.pack()
        # -----------------------------------------------------------------------------------------------------------------

        text2 = Label(c, text='введите массу в килограммах', bg='#c2b48c', font=40)
        text2.pack()

        qef = Entry(c, bg='#c2b48c')
        qef.pack()

        #button = Button(c, text='                кнопка                ', bg='#c2b48c', command=changec)
        #button.pack()

        label = Label(c, width=21, height=2, bg='#c2b48c')
        label.pack()

        c.mainloop()

    def teplo1():

        def af():
            labelwq['text'] = "0°C"
        def bf():
            labelwq['text'] = "962°C"
        def cf():
            labelwq['text'] = "-39°C"
        def df():
            labelwq['text'] = "1085°C"
        def ef():
            labelwq['text'] = "-114°C"
        def ff():
            labelwq['text'] = "1064°C"
        def gf():
            labelwq['text'] = "327°C"
        def hf():
            labelwq['text'] = "1500°C"

        # параметры окна
        d = Tk()
        d.title('выеснение температуры плавления')
        d['bg'] = '#c2b48c'
        d.wm_attributes('-alpha', 0.9)
        d.geometry("400x350+200+300")
        d.resizable(0, False)

        text = Label(d, text='выберете вещевство', bg='#c2b48c', font=40)
        text.pack()

        # 1
        a1 = Button(d, text="лёд", command = af, bg='#c2b48c')
        b1 = Button(d, text="серебро", command = bf, bg='#c2b48c')
        c1 = Button(d, text="ртуть", command = cf, bg='#c2b48c')
        d1 = Button(d, text="медь", command = df, bg='#c2b48c')
        e1 = Button(d, text="спирт", command = ef, bg='#c2b48c')
        f1 = Button(d, text="золото", command = ff, bg='#c2b48c')
        g1 = Button(d, text="свинец", command = gf, bg='#c2b48c')
        h1 = Button(d, text="сталь", command = hf, bg='#c2b48c')
        a1.pack()
        b1.pack()
        c1.pack()
        d1.pack()
        e1.pack()
        f1.pack()
        g1.pack()
        h1.pack()
        # -----------------------------------------------------------------------------------------------------------------

        labelwq = Label(d, width=21, height=2, bg='#c2b48c')
        labelwq.pack()

        d.mainloop()

    def sila():
        def afb():
            y = 3.68
            x = float(qef1.get())
            z = x * y
            label['text'] = round(z, 7), 'Н'

        def bfb():
            y = 8.76
            x = float(qef1.get())
            z = x * y
            label['text'] = round(z, 7), 'Н'

        def cfb():
            y = 9.81
            x = float(qef1.get())
            z = x * y
            label['text'] = round(z, 7), 'Н'

        def dfb():
            y = 3.47
            x = float(qef1.get())
            z = x * y
            label['text'] = round(z, 7), 'Н'

        def efb():
            y = 24.6
            x = float(qef1.get())
            z = x * y
            label['text'] = round(z, 7), 'Н'

        def ffb():
            y = 10.37
            x = float(qef1.get())
            z = x * y
            label['text'] = round(z, 7), 'Н'

        def gfb():
            y = 8.17
            x = float(qef1.get())
            z = x * y
            label['text'] = round(z, 7), 'Н'

        def hfb():
            y = 11.06
            x = float(qef1.get())
            z = x * y
            label['text'] = round(z, 7), 'Н'

        # параметры окна
        e = Tk()
        e.title('расчёт силы на разных планетах')
        e['bg'] = '#c2b48c'
        e.wm_attributes('-alpha', 0.9)
        e.geometry("400x350+200+300")
        e.resizable(0, False)

        text1 = Label(e, text='выберете планету', bg='#c2b48c', font=40)
        text1.pack()

        # блок с этими круглами штуками вобшем
        a3 = Button(e, text="Меркурий", command = afb, bg='#c2b48c')
        b3 = Button(e, text="Венера", command = bfb, bg='#c2b48c')
        c3 = Button(e, text="Земля", command = cfb, bg='#c2b48c')
        d3 = Button(e, text="Марс", command = dfb, bg='#c2b48c')
        e3 = Button(e, text="Юпитер", command = efb, bg='#c2b48c')
        f3 = Button(e, text="Сатурн", command = ffb, bg='#c2b48c')
        g3 = Button(e, text="Уран", command = gfb, bg='#c2b48c')
        h3 = Button(e, text="Нептун", command = hfb, bg='#c2b48c')
        a3.pack()
        b3.pack()
        c3.pack()
        d3.pack()
        e3.pack()
        f3.pack()
        g3.pack()
        h3.pack()
        # -----------------------------------------------------------------------------------------------------------------

        text2 = Label(e, text='введите массу в килограммах', bg='#c2b48c', font=40)
        text2.pack()

        qef1 = Entry(e, bg='#c2b48c')
        qef1.pack()

        label = Label(e, width=21, height=2, bg='#c2b48c')
        label.pack()

        e.mainloop()

    def plotnost():

        def changef():
            x = qef.get()
            y = swc.get()
            x = float(x)
            y = float(y)
            z = x / y
            label['text'] = round(z, 7), 'кг/м³'

            print(':)')
            print(' ')

        # параметры окна
        f = Tk()
        f.title('расчёт плотности')
        f['bg'] = '#c2b48c'
        f.wm_attributes('-alpha', 0.9)
        f.geometry("400x350+200+300")
        f.resizable(0, False)

        text = Label(f, text='введите массу в килограммах', bg='#c2b48c', font=40)
        text.pack()

        qef = Entry(f, bg='#c2b48c')
        qef.pack()

        text = Label(f, text='введите обЪём в кубических метрах', bg='#c2b48c', font=40)
        text.pack()

        swc = Entry(f, bg='#c2b48c')
        swc.pack()

        button = Button(f, text='                кнопка                ', bg='#c2b48c', command=changef)
        button.pack()

        label = Label(f, width=21, height=2, bg='#c2b48c')
        label.pack()

        f.mainloop()

    def res():
        def OM():
            i = float(I.get())
            u = float(U.get())
            R = u / i
            Om['text'] = round(R, 7)

        res = Tk()
        res['bg'] = '#c2b48c'
        res.resizable(0, False)
        res.title('расчёт сопротивления')
        res.geometry('200x200+100+200')

        Label(res, text='введите силу тока в A', bg = '#c2b48c').pack()
        I = Entry(res, bg = '#c2b48c')
        I.pack()
        Label(res, text='введите напряжение в В', bg = '#c2b48c').pack()
        U = Entry(res, bg = '#c2b48c')
        U.pack()
        Button(res, command=OM, bg = '#c2b48c', text = 'подсчитать').pack()
        Om = Label(res, bg = '#c2b48c')
        Om.pack()
        res.mainloop()

    def Auit():
        def AUIt():
            i = int(AI.get())
            u = int(AU.get())
            t = int(At.get())
            Al['text'] = str(i * u * t) + ' Дж'

        A = Tk()
        A.title('работа')
        A['bg'] = '#c2b48c'
        A.geometry('300x300')
        A.resizable(0, False)

        Label(A, text='введите I в А', bg='#c2b48c').place(x=90, y=0)
        AI = Entry(A, bg='#c2b48c')
        AI.place(x=40, y=30)
        Label(A, text='введите U в В', bg='#c2b48c').place(x=90, y=60)
        AU = Entry(A, bg='#c2b48c')
        AU.place(x=40, y=90)
        Label(A, text='t в с', bg='#c2b48c').place(x=120, y=120)
        At = Entry(A, bg='#c2b48c')
        At.place(x=40, y=150)
        Button(A, text='кнопка', command=AUIt, bg='#c2b48c').place(x=100, y=180)
        Al = Label(A, bg='#c2b48c')
        Al.place(x=100, y=210)

        A.mainloop()

    ro = Tk()
    ro.title("физика")
    ro['bg'] = '#c2b48c'
    ro.resizable(False, False)
    gs = Label(ro, text="Интерактивный помощник", bg='#c2b48c')
    gs.pack()
    prva = Button(ro, text="расчёт скорости", width=40, command=skorost, bg='#c2b48c')
    prva.pack()
    prvb = Button(ro, text="расчёт давления", width=40, command=davlenie, bg='#c2b48c')
    prvb.pack()
    prvc = Button(ro, text="расчёт количество теплоты при плавлении", width=40, command=teplo, bg='#c2b48c')
    prvc.pack()
    prvd = Button(ro, text="выеснение температуры плавления", width=40, command=teplo1, bg='#c2b48c')
    prvd.pack()
    prve = Button(ro, text="расчёт силы на разных планетах", width=40, command=sila, bg='#c2b48c')
    prve.pack()
    prvf = Button(ro, text="расчёт плотности", width=40, command=plotnost, bg='#c2b48c')
    prvf.pack()
    prvg = Button(ro, text = 'выеснение сопротивления', width=40, command=res, bg = '#c2b48c')
    prvg.pack()
    prvh = Button(ro, text='выеснение работы тока', width=40, command=Auit, bg='#c2b48c')
    prvh.pack()
    ro.mainloop()


def mega():
    def giga():
        x = float(megch.get())
        megl['text'] = x*10**9

    def Mega():
        x = float(megch.get())
        megl['text'] = x * 10 ** 6

    def kilo():
        x = float(megch.get())
        megl['text'] = x * 10 ** 3

    def gekto():
        x = float(megch.get())
        megl['text'] = x * 10 ** 2

    def deka():
        x = float(megch.get())
        megl['text'] = x * 10

    def dizi():
        x = float(megch.get())
        megl['text'] = x / 10

    def santi():
        x = float(megch.get())
        megl['text'] = x / 10 ** 2

    def milli():
        x = float(megch.get())
        megl['text'] = x / 10 ** 3

    def mikro():
        x = float(megch.get())
        megl['text'] = x / 10 ** 6

    def nano():
        x = float(megch.get())
        megl['text'] = x / 10 ** 9

    meg = Tk()
    meg.geometry('300x300')
    meg['bg'] = '#0779a3'
    meg.resizable(0, 0)
    meg.title('MegaK 0.2')

    Label(meg, bg = '#0779a3', text = 'введите число', fg = '#7e3c05').place(x = 100, y = 4)
    megch = Entry(meg, bg = '#055781')
    megch.place(x = 50, y = 29)
    Button(meg, bg = '#055781', text = 'гига', command=giga).place(x = 2, y = 59)
    Button(meg, bg='#055781', text='мега', command=Mega).place(x=70, y=59)
    Button(meg, bg='#055781', text='кило', command=kilo).place(x=140, y=59)
    Button(meg, bg='#055781', text='гекто', command=gekto).place(x=210, y=59)
    Button(meg, bg='#055781', text='дека', command=deka).place(x=2, y=89)
    Button(meg, bg='#055781', text='дици', command=dizi).place(x=70, y=89)
    Button(meg, bg='#055781', text='санти', command=santi).place(x=140, y=89)
    Button(meg, bg='#055781', text='милли', command=milli).place(x=210, y=89)
    Button(meg, bg='#055781', text='микро', command=mikro).place(x=35, y=120)
    Button(meg, bg='#055781', text='нано', command=nano).place(x=105, y=120)
    megl = Label(meg, bg = '#0779a3')
    megl.place(x = 100, y = 270)

    meg.mainloop()


root = Tk()
root.title("калькулятор")
root.geometry('300x450')
# root['bg'] = '#aabbaa'
root.resizable(0, 0)

# //   ;)
r = Canvas(root, bg='#aabbaa', width=300, height=450)
r.pack()
r.create_oval((10, 10), (30, 30), fill='#889988', outline='#889988')
r.create_oval((260, 40), (270, 30), fill='#889988', outline='#889988')
r.create_oval((40, 90), (70, 120), fill='#889988', outline='#889988')
r.create_oval((90, 200), (75, 215), fill='#889988', outline='#889988')
r.create_oval((190, 250), (215, 275), fill='#889988', outline='#889988')
r.create_oval((40, 80), (30, 70), fill='#889988', outline='#889988')
r.create_oval((270, 70), (295, 95), fill='#889988', outline='#889988')
r.create_oval((250, 189), (265, 204), fill='#889988', outline='#889988')
r.create_oval((30, 225), (45.1, 240.1), fill='#aabbaa', outline='#889988')
r.create_oval((200, 200), (210, 210), fill='#aabbaa', outline='#889988')

l1 = Label(root, bg='#aabbaa', text='введите первое число', fg='#334433')
l1.place(x=80, y=4)
a = Entry(root, bg='#889988')
a.place(x=60, y=29)
l2 = Label(root, bg='#aabbaa', text='введите второе число', fg='#334433')
l2.place(x=80, y=58)
b = Entry(root, bg='#889988')
b.place(x=60, y=91)
p = Button(root, bg='#aabbaa', text='+', command=F1)
p.place(x=10, y=130)
m = Button(root, bg='#aabbaa', text='-', command=F2)
m.place(x=80, y=130)
d = Button(root, bg='#aabbaa', text='/', command=F3)
d.place(x=170, y=130)
u = Button(root, bg='#aabbaa', text='*', command=F4)
u.place(x=240, y=130)
q = Button(root, bg='#aabbaa', text='%', command=F5)
q.place(x=10, y=170)
s = Button(root, bg='#aabbaa', text='^', command=F6)
s.place(x=80, y=170)
w = Button(root, bg='#aabbaa', text='‰', command=F7)
w.place(x=170, y=170)
klmn = Button(root, bg='#aabbaa', text='y√x', command=F8)
klmn.place(x=240, y=170)
l = Label(root, bg='#aabbaa', fg='#334433')
l.place(x=10, y=210)
v = Button(root, bg='#aabbaa', text='вызвать калькулятор для 1 числа', command=New)
v.place(x=15, y=250)
vd = Button(root, bg='#aabbaa', text='вызвать генератор случайных чисел', command=okno)
vd.place(x=15, y=290)
vdq = Button(root, bg='#aabbaa', text='вызвать рисователя графиков', command=weh)
vdq.place(x=15, y=330)
prstv = Button(root, bg='#aabbaa', text='вызвать физический калькулятор', command=prst)
prstv.place(x=15, y=370)
megv = Button(root, bg='#aabbaa', text='приставки си', command=mega)
megv.place(x=15, y=410)

root.mainloop()