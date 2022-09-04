#tkinter
'''''
from bs4 import BeautifulSoup
import requests
from datetime import datetime


dollar_rub = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE&aqs=chrome.0.0i131i433i512l2j69i57j0i131i433i512l2j0i433i512l2j69i61.11094j1j7&sourceid=chrome&ie=UTF-8'
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
    full_page = requests.get(dollar_rub, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    bot.send_message(message.chat.id, f'<b>доллар в Российских рублях: {convert[0].text}</b>', parse_mode='html')
    print(message)
'''
from tkinter import *
from currency import f
'''''
def f(link):
    dollar_rub = link
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
    full_page = requests.get(dollar_rub, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    return convert
'''

def USD():
    dollar_rub = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE&aqs=chrome.0.0i131i433i512l2j69i57j0i131i433i512l2j0i433i512l2j69i61.11094j1j7&sourceid=chrome&ie=UTF-8'
    text['text'] = f"Доллар США в Российских рублях: {f(dollar_rub)[0].text}"

def EUR():
    eur = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&sxsrf=ALiCzsYeBzoNMUVTBGNIgt7_MgbtF3kj0w%3A1652561872724&ei=0BeAYs3tK8yqrgS8t76wDg&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5&gs_lcp=Cgdnd3Mtd2l6EAEYADIECCMQJzIECCMQJzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyBQgAEIAEMgsIABCABBCxAxDJAzIFCAAQkgMyCAgAEIAEELEDOgcIABBHELADOgoIABBHELADEMkDOggIABCSAxCwAzoSCC4QxwEQ0QMQyAMQsAMQQxgBOgoIABCxAxCDARBDOgsIABCABBCxAxCDAToJCCMQJxBGEIICSgQIQRgASgQIRhgAUKsEWPUZYN0naAFwAXgAgAFLiAHXA5IBATiYAQCgAQHIAQvAAQHaAQQIARgI&sclient=gws-wiz'
    text['text'] = f"Евро в Российских рублях: {f(eur)[0].text}"

def LKR():
    lkr = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%88%D1%80%D0%B8+%D0%BB%D0%B0%D0%BD%D0%BA%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B9+%D1%80%D1%83%D0%BF%D0%B8%D0%B8+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sxsrf=ALiCzsb5xPp_lzK7jvsIr-qVVJROZOIoIg%3A1652617729473&ei=AfKAYoOjHO6IrwTv6I2ACA&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%88%D1%80%D0%B8&gs_lcp=Cgdnd3Mtd2l6EAEYADIJCCMQJxBGEIICMgoIABCABBCHAhAUMgQIABAKMgcIABCxAxAKMgUIABCABDIECAAQCjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjELADECc6BwgAEEcQsAM6BwgAELADEEM6BAgjECc6BAgAEEM6EAgAEIAEEIcCELEDEIMBEBQ6CAgAEIAEELEDOg0IABCABBCHAhCxAxAUOgsIABCABBCxAxCDAToECAAQAkoECEEYAEoECEYYAFDeDVi6LmDdOGgDcAF4AIABZogBwQOSAQM1LjGYAQCgAQHIAQrAAQE&sclient=gws-wiz'
    text['text'] = f"Шри-ланская рупия в Российских рублях: {f(lkr)[0].text}"

def EGP():
    egp = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B3%D0%B8%D0%BF%D0%B5%D1%82%D1%81%D0%BA%D0%BE%D0%B3%D0%BE+%D1%84%D1%83%D0%BD%D1%82%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sxsrf=ALiCzsanI37SlcKG2RMy388SlUw1ESqrhA%3A1652617538041&ei=QvGAYtuOAsGQrgSBxonIBw&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B3%D0%B8&gs_lcp=Cgdnd3Mtd2l6EAEYADIJCCMQJxBGEIICMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIABBHELADOgkIABCABBAKECo6CggAEIAEEIcCEBQ6DQgAEIAEEIcCELEDEBQ6CwgAEIAEELEDEIMBOggIABCxAxCDAToECAAQAzoECCMQJzoQCAAQgAQQhwIQsQMQgwEQFDoICAAQgAQQsQM6CwgAEIAEELEDEMkDOgUIABCSA0oECEEYAEoECEYYAFC7BliHImCzK2gBcAF4AIABUogB7wKSAQE1mAEAoAEByAEIwAEB&sclient=gws-wiz'
    text['text'] = f"Египецкий фунт в Российских рублях: {f(egp)[0].text}"

def main(root):
    r = Canvas(root, width=300, height=400)
    r.pack()
    BG_photo = PhotoImage(file='bg_photo.png')
    r.create_image(150, 200, image=BG_photo)

    global text
    text = Label(root, bg = '#78909c', width = 32, height=2)
    text.place(x = 3, y = 3)

    Button(root, text = 'USD', command=USD).place(x = 10, y = 80)
    Button(root, text = 'EUR', command=EUR).place(x = 10, y = 110)
    Button(root, text='LKR', command=LKR).place(x=10, y=140)
    Button(root, text='EGP', command=EGP).place(x=10, y=170)


    root.mainloop()

if __name__ == '__main__':
    root = Tk()
    root.title('MegaK currency')
    root.geometry('300x400+450+100')

    main(root)