import os
import random
import smtplib
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image



def password_admin(event):
    frame = Frame(window, bd=5)
    frame.place(relwidth=1, relheight=1)

    def username_password():
        if name_entry.get() == 'admin' and password_entry.get() == 'admin':
            os.system(r'C:\Users\Admin\PycharmProjects\pythonProject\project\pizza_order.db')

        else:
            messagebox.showerror('errors', 'Your name or password is incorrect')

    canvas = Canvas(frame, bg='white')
    canvas.place(x=520, y=160)

    name_label = Label(frame, text="Adınızı daxil edin", fg='white', bg='#6F4E37', font='Ariel 10 bold')
    name_label.place(x=580, y=230)
    password_label = Label(frame, text=" Parolunuzu daxil\n edin ", fg='white', bg='#6F4E37', font='Ariel 10 bold')
    password_label.place(x=580, y=270)
    label = Label(frame, text='Admin Panel', bg='white', font='ariel 14 bold')
    label.place(x=655, y=180)

    name_entry = Entry(frame, width=18, font='Ariel 10 bold', bd=3)
    name_entry.place(x=710, y=230)
    password_entry = Entry(frame, width=18, font='Ariel 10 bold', bd=3, show='*')
    password_entry.place(x=710, y=270)

    button = Button(frame, text='Giriş', bg='#6F4E37', fg='white', width=15, bd=3, command=username_password)
    button.place(x=710, y=320)

    button_home = Button(frame, text='Geri qayıd', bg='#6F4E37', fg='white', width=15, bd=3, command=lambda:
    frame.destroy())
    button_home.place(x=580, y=320)


def order():
    frame = Frame(window, bd=5, bg='white')
    frame.place(relwidth=1, relheight=1)

    def gmail_message():
        sender = 'pizzaorderaze@gmail.com'
        password = 'AlPay1122'
        body = f"salam {name_lastname_entry.get()} bizi seçdiyiniz üçün təşəkkülər\nsizin ümumi borcunuz {price3}-AZN  "
        subject = 'pizza siparisi'
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = str(gmail_entry.get())
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        text = message.as_string()
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(sender, password)
        mail.sendmail(sender, str(gmail_entry.get()), text)
        mail.close()

    def data_bsae_order():
        con = sqlite3.connect('pizza_order.db')
        cursor = con.cursor()

        def tabloolustr():
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS siparisverenler(AdSoyad TEXT, Address,Telfon INT,barbekyu TEXT,kabab TEXT, Sosuso TEXT,Qarisiq,havay,serqToyuqu,Salyami,rengbereng,YekunQiymet TEXT)""")

        def tabloolustrrr():
            cursor.execute(
                f"""INSERT INTO siparisverenler VALUES ('{name_lastname_entry.get()}', '{address_entry.get()}', '{phone_entry.get()}',{str(pizza_list[4])},{str(pizza_list[5])},{str(pizza_list[7])},{pizza_list[6]},{pizza_list[2]},{pizza_list[0]},{pizza_list[3]},{pizza_list[1]},{price3})""")
            con.commit()
            con.close()
            gmail_message()

        tabloolustr()
        tabloolustrrr()

    def save():
        if len(phone_entry.get()) < 10:
            messagebox.showerror('error', 'Zəhmət olmasa nömrəni düzgün daxil edin!')
        elif len(cardnum_entry.get()) != 16:
            messagebox.showerror('error', 'Zəhmət olmasa kartın nömrəsin \n düzgün daxil edin!')
        elif len(cvc_card_entry.get()) > 4:
            messagebox.showerror('error', 'Zəhmət olmasa kartın CCV \n düzgün daxil edin!')
        elif len(card_data_entry.get()) > 5:
            messagebox.showerror('error', 'Zəhmət olmasa kartın parolun \n düzgün daxil edin!')
        elif len(name_lastname_entry.get()) == 0:
            messagebox.showerror('error', 'Zəhmət olmasa ad daxil  \nedin parolun!')
        elif len(address_entry.get()) == 0:
            messagebox.showerror('error', 'Zəhmətp olmasa address \ndaxil edin!')
        elif len(gmail_entry.get()) == 0:
            messagebox.showerror('error', 'Zəhmət olmasa gmail\n daxil edin')
        else:
            messagebox.showinfo('pizza order', 'Sifariş qeydə alındı')
            data_bsae_order()
            frame.destroy()

    my_pic9 = Image.open('../../Desktop/pro/img/pizza_arxa_plan.jpg')
    resized9 = my_pic9.resize((600, 600), Image.ANTIALIAS)
    new_pic9 = ImageTk.PhotoImage(resized9)
    pizza8_label = Label(frame, image=new_pic9)
    pizza8_label.place(x=400, y=30)

    Label(frame, text='Sipariş et', font='arial 14 bold', bg='white', fg='green').pack()
    Label(frame, text='       Ad-Soyad         ', bg='#6F4E37', fg='white', font='arial 10 bold').place(x=535, y=170)
    Label(frame, text='          Unvan:        ', bg='#6F4E37', fg='white', font='arial 10 bold').place(x=535, y=205)
    Label(frame, text='  Telefon nömrəsi:  ', bg='#6F4E37', fg='white', font='arial 10 bold').place(x=535, y=245)
    Label(frame, text='     Kartın nömrəsi    ', bg='#6F4E37', fg='white', font='arial 10 bold').place(x=535, y=285)
    Label(frame, text='        CVC2/CVV2      ', bg='#6F4E37', fg='white', font='Ariel 10  bold').place(x=535, y=325)
    Label(frame, text='    Isdifdə müddəti    ', bg='#6F4E37', fg='white', font='Ariel 10  bold').place(x=535, y=365)
    Label(frame, text='       mail unvani           ', bg='#6F4E37', fg='white', font='Ariel 10  bold').place(x=535,
                                                                                                             y=405)

    phone_intvar = IntVar()
    phone_intvar.set("+994")

    name_lastname_entry = Entry(frame, width=30, bd=5)
    name_lastname_entry.place(x=690, y=170)
    address_entry = Entry(frame, width=30, bd=5)
    address_entry.place(x=690, y=202)
    phone_entry = Entry(frame, width=30, bd=5, textvariable=phone_intvar)
    phone_entry.place(x=690, y=242)
    cardnum_entry = Entry(frame, width=30, bd=5)
    cardnum_entry.place(x=690, y=282)
    cvc_card_entry = Entry(frame, width=30, bd=5)
    cvc_card_entry.place(x=690, y=322)
    card_data_entry = Entry(frame, width=30, bd=5)
    card_data_entry.place(x=690, y=361)
    gmail_entry = Entry(frame, width=30, bd=5)
    gmail_entry.place(x=690, y=401)

    save_button = Button(frame, text='Siparişi Yekunlaşdırmaq', width=18, height=1, bg='#6F4E37', fg='white', bd=3,
                         command=save)
    save_button.place(x=690, y=440)
    back_button = Button(frame, text='Geri Qayıd', width=18, height=1, bg='#6F4E37', fg='white', bd=3,
                         command=frame.destroy)
    back_button.place(x=535, y=440)

    price = int(price_entry_sosuso.get()) + float(price_entry_kabab.get()) + int(price_entry_bar.get()) + int(
        price_entry_mixed.get())
    price2 = float(price_entry_serq.get()) + int(price_entry_r.get()) + int(price_entry_hav.get()) + int(
        price_entry_sal.get())
    price3 = price2 + price
    Label(frame, text=f'Yekun qiymət\n{price3} AZN', fg='black', bg='white', font="ariel 10 bold").place(x=837, y=440)



window = Tk()
window.geometry('900x600')
window.title('Pizza Order')
window.configure(bg='white')

pizza_list = []
frame = Frame(window, bd=5, bg='white')
frame.place(relwidth=1, relheight=1)


def multifuc_s():
    pizza_list.insert(0, display_serq.get())
    messagebox.showinfo('pizza sipariş', 'sipariş qeydə alındı')



def plus_entry_serq():
    global serq_t_count
    global serq_t_price_count
    serq_t_count = serq_t_count + 1
    display_serq.delete(0, END)
    display_serq.insert(0, serq_t_count)
    serq_t_price_count = serq_t_price_count + float(9.50)
    price_entry_serq.delete(0, END)
    price_entry_serq.insert(0, serq_t_price_count)


def negative_but_serq():
    global serq_t_count
    global serq_t_price_count
    if serq_t_count >= 1:
        serq_t_count = serq_t_count - 1
        display_serq.delete(0, END)
        display_serq.insert(0, serq_t_count)
        serq_t_price_count = serq_t_price_count - float(9.50)
        price_entry_serq.delete(0, END)
        price_entry_serq.insert(0, serq_t_price_count)


plus_button_serq = Button(frame, text='+', bg='white', fg='green', command=plus_entry_serq)
plus_button_serq.place(x=380, y=1000)
negative_button_serq = Button(frame, text='-', bg='white', fg='green', command=negative_but_serq)
negative_button_serq.place(x=440, y=1000)
display_serq = Entry(frame, width=2, textvariable=IntVar())
display_serq.place(x=415, y=1000)
price_money_label_serq = Label(frame, text='AZN', bg='white')
price_money_label_serq.place(x=510, y=1000)
price_entry_serq = Entry(frame, width=5, textvariable=IntVar())
price_entry_serq.place(x=470, y=1000)
pizza8_button = Button(frame, text='Səbətə əlavə et', width=15, height=2, bg='#6F4E37', fg='white', font='20',
                       command=multifuc_s)
pizza8_button.place(x=380, y=1000)
pizza_list.insert(0, display_serq.get())


#
def multifuc_r():
    pizza_list.insert(1, display_r.get())
    messagebox.showinfo('pizza sipariş', 'sipariş qeydə alındı')


def plus_entry_r():
    global renbereng_count
    global rengbereng_price_count
    renbereng_count = renbereng_count + 1
    display_r.delete(0, END)
    display_r.insert(0, renbereng_count)
    rengbereng_price_count = rengbereng_price_count + 10
    price_entry_r.delete(0, END)
    price_entry_r.insert(0, rengbereng_price_count)


def negative_but_r():
    global renbereng_count
    global rengbereng_price_count
    if renbereng_count >= 1:
        renbereng_count = renbereng_count - 1
        display_r.delete(0, END)
        display_r.insert(0, renbereng_count)
        rengbereng_price_count = rengbereng_price_count - 10
        price_entry_r.delete(0, END)
        price_entry_r.insert(0, rengbereng_price_count)


plus_button_r = Button(frame, text='+', bg='white', fg='green', command=plus_entry_r)
plus_button_r.place(x=999, y=1000)
negative_button_r = Button(frame, text='-', bg='white', fg='green', command=negative_but_r)
negative_button_r.place(x=1051, y=1000)
display_r = Entry(frame, width=2, textvariable=IntVar())
display_r.place(x=1028, y=1000)
price_money_label_r = Label(frame, text='AZN', bg='white')
price_money_label_r.place(x=1110, y=1000)
price_entry_r = Entry(frame, width=5, textvariable=IntVar())
price_entry_r.place(x=1075, y=1000)
pizza7_button = Button(frame, text='Səbətə əlavə et', width=15, height=2, bg='#6F4E37', bd=3, fg='white', font='20',
                       command=multifuc_r)
pizza7_button.place(x=970, y=1000)
pizza_list.insert(1, display_r.get())


def multifuc_h():
    pizza_list.insert(2, display_hav.get())
    messagebox.showinfo('pizza sipariş', 'sipariş qeydə alındı')


def plus_entry_h():
    global havay_count
    global havay_price_count
    havay_count = havay_count + 1
    display_hav.delete(0, END)
    display_hav.insert(0, havay_count)

    havay_price_count = havay_price_count + 10
    price_entry_hav.delete(0, END)
    price_entry_hav.insert(0, havay_price_count)


def negative_but_h():
    global havay_count
    global havay_price_count
    if havay_count >= 1:
        havay_count = havay_count - 1
        display_hav.delete(0, END)
        display_hav.insert(0, havay_count)
        havay_price_count = havay_price_count - 10
        price_entry_hav.delete(0, END)
        price_entry_hav.insert(0, havay_price_count)


plus_button_hav = Button(frame, text='+', bg='white', fg='green', command=plus_entry_h)
plus_button_hav.place(x=70, y=1000)
negative_button_hav = Button(frame, text='-', bg='white', fg='green', command=negative_but_h)
negative_button_hav.place(x=120, y=1000)
display_hav = Entry(frame, width=2, textvariable=IntVar())
display_hav.place(x=100, y=1000)
price_money_label_hav = Label(frame, text='AZN', bg='white')
price_money_label_hav.place(x=176, y=1000)
price_entry_hav = Entry(frame, width=5, textvariable=IntVar())
price_entry_hav.place(x=140, y=1000)
pizza6_button = Button(frame, text='Səbətə əlavə et', width=15, height=2, bg='#6F4E37', fg='white', font='20',
                       command=multifuc_h)
pizza6_button.place(x=60, y=1000)
pizza_list.insert(2, display_hav.get())


def multifuc_sal():
    pizza_list.insert(3, display_sal.get())
    messagebox.showinfo('pizza sipariş', 'sipariş qeydə alındı')


def plus_entry_sal():
    global salyami_count
    global salyami_price_count
    salyami_count = salyami_count + 1
    display_sal.delete(0, END)
    display_sal.insert(0, salyami_count)
    salyami_price_count = salyami_price_count + 10
    price_entry_sal.delete(0, END)
    price_entry_sal.insert(0, salyami_price_count)


def negative_but_sal():
    global salyami_count
    global salyami_price_count
    if salyami_count >= 1:
        salyami_count = salyami_count - 1
        display_sal.delete(0, END)
        display_sal.insert(0, salyami_count)
        salyami_price_count = salyami_price_count - 10
        price_entry_sal.delete(0, END)
        price_entry_sal.insert(0, salyami_price_count)


plus_button_sal = Button(frame, text='+', bg='white', fg='green', command=plus_entry_sal)
plus_button_sal.place(x=698, y=1000)
negative_button_sal = Button(frame, text='-', bg='white', fg='green', command=negative_but_sal)
negative_button_sal.place(x=750, y=1000)
display_sal = Entry(frame, width=5, textvariable=IntVar())
display_sal.place(x=727, y=1000)
price_entry_sal = Entry(frame, width=5, textvariable=IntVar())
price_entry_sal.place(x=775, y=1000)
price_label_sal = Label(frame, text='AZN', bg='white')
price_label_sal.place(x=810, y=1000)
pizza5_button = Button(frame, text='Səbətə əlavə et', width=15, height=2, bg='#6F4E37', fg='white', font='20',
                       command=multifuc_sal)
pizza5_button.place(x=690, y=1000)
pizza_list.insert(3, display_sal.get())


#


def multufuc_b():
    pizza_list.insert(4, display_bar.get())
    messagebox.showinfo('pizza sipariş', 'sipariş qeydə alındı')


def plus_entry_b():
    global barbacue_count
    global barbacue_price_count
    barbacue_count = barbacue_count + 1
    display_bar.delete(0, END)
    display_bar.insert(0, barbacue_count)
    barbacue_price_count = barbacue_price_count + 10
    price_entry_bar.delete(0, END)
    price_entry_bar.insert(0, barbacue_price_count)


def negative_but_b():
    global barbacue_count
    global barbacue_price_count
    if barbacue_count >= 1:
        barbacue_count = barbacue_count - 1
        display_bar.delete(0, END)
        display_bar.insert(0, barbacue_count)
        barbacue_price_count = barbacue_price_count - 10
        price_entry_bar.delete(0, END)
        price_entry_bar.insert(0, barbacue_price_count)


plus_button_bar = Button(frame, text='+', bg='white', fg='green', command=plus_entry_b)
plus_button_bar.place(x=70, y=400)
negative_button_bar = Button(frame, text='-', bg='white', fg='green', command=negative_but_b)
negative_button_bar.place(x=120, y=400)
display_bar = Entry(frame, width=2, textvariable=IntVar())
display_bar.place(x=100, y=402)
price_money_label_bar = Label(frame, text='AZN', bg='white')
price_money_label_bar.place(x=176, y=402)
price_entry_bar = Entry(frame, width=5, textvariable=IntVar())
price_entry_bar.place(x=140, y=402)
pizza_button_bar = Button(frame, text='Səbətə əlavə et', width=15, height=2, bg='#6F4E37', fg='white', font='20',
                          command=multufuc_b)
pizza_button_bar.place(x=60, y=500)
pizza_list.insert(4, display_bar.get())


def multufuc_k():
    pizza_list.insert(5, display_kabab.get())
    messagebox.showinfo('pizza sipariş', 'sipariş qeydə alındı')


def plus_entry_k():
    global khabab_count
    global khabab_price_count
    khabab_count = khabab_count + 1
    display_kabab.delete(0, END)
    display_kabab.insert(0, khabab_count)
    khabab_price_count = khabab_price_count + float(12.50)
    price_entry_kabab.delete(0, END)
    price_entry_kabab.insert(0, khabab_price_count)


def negative_but_k():
    global khabab_count
    global khabab_price_count
    if khabab_count >= 1:
        khabab_count = khabab_count - 1
        display_kabab.delete(0, END)
        display_kabab.insert(0, khabab_count)
        khabab_price_count = khabab_price_count - float(12.50)
        price_entry_kabab.delete(0, END)
        price_entry_kabab.insert(0, khabab_price_count)


plus_button_kabab = Button(frame, text='+', bg='white', fg='green', command=plus_entry_k)
plus_button_kabab.place(x=380, y=400)
negative_button_kabab = Button(frame, text='-', bg='white', fg='green', command=negative_but_k)
negative_button_kabab.place(x=440, y=399)
display_kabab = Entry(frame, width=2, textvariable=IntVar())
display_kabab.place(x=415, y=402)
price_money_label_kabab = Label(frame, text='AZN', bg='white')
price_money_label_kabab.place(x=510, y=402)
price_entry_kabab = Entry(frame, width=5, textvariable=IntVar())
price_entry_kabab.place(x=470, y=402)
pizza3_button = Button(frame, text='Səbətə əlavə et', width=15, height=2, bg='#6F4E37', fg='white', font='20',
                       command=multufuc_k)
pizza3_button.place(x=380, y=500)
pizza_list.insert(5, display_kabab.get())


def multufuc_mixed():
    pizza_list.insert(6, display_mixed.get())
    messagebox.showinfo('pizza sipariş', 'sipariş qeydə alındı')


def plus_entry():
    global mixed_count
    global mixed_price_count
    mixed_count = mixed_count + 1
    display_mixed.delete(0, END)
    display_mixed.insert(0, mixed_count)
    mixed_price_count = mixed_price_count + 10
    price_entry_mixed.delete(0, END)
    price_entry_mixed.insert(0, mixed_price_count)


def negative_but():
    global mixed_count
    global mixed_price_count
    if mixed_count >= 1:
        mixed_count = mixed_count - 1
        display_mixed.delete(0, END)
        display_mixed.insert(0, mixed_count)
        mixed_price_count = mixed_price_count - 10
        price_entry_mixed.delete(0, END)
        price_entry_mixed.insert(0, mixed_price_count)


plus_button_mixed = Button(frame, text='+', bg='white', fg='green', command=plus_entry)
plus_button_mixed.place(x=999, y=399)
negative_button_mixed = Button(frame, text='-', bg='white', fg='green', command=negative_but)
negative_button_mixed.place(x=1051, y=399)
display_mixed = Entry(frame, width=2, textvariable=IntVar())
display_mixed.place(x=1028, y=402)
price_money_label_mixed = Label(frame, text='AZN', bg='white')
price_money_label_mixed.place(x=1110, y=402)
price_entry_mixed = Entry(frame, width=5, textvariable=IntVar())
price_entry_mixed.place(x=1075, y=402)
pizza2_button = Button(frame, text='Səbətə əlavə et', width=15, height=2, bg='#6F4E37', bd=3, fg='white',
                       font='20', command=multufuc_mixed)
pizza2_button.place(x=970, y=500)
pizza_list.insert(6, display_mixed.get())


def multifuc_sosuso():
    pizza_list.insert(7, display_sosuso.get())
    messagebox.showinfo('pizza sipariş', 'sipariş qeydə alındı')


def plus_entry():
    global sosuso_count
    global sosuso_price_count
    sosuso_count = sosuso_count + 1
    display_sosuso.delete(0, END)
    display_sosuso.insert(0, sosuso_count)
    sosuso_price_count = sosuso_price_count + 12
    price_entry_sosuso.delete(0, END)
    price_entry_sosuso.insert(0, sosuso_price_count)


def negative_but():
    global sosuso_count
    global sosuso_price_count
    if sosuso_count >= 1:
        sosuso_count = sosuso_count - 1
        display_sosuso.delete(0, END)
        display_sosuso.insert(0, sosuso_count)
        sosuso_price_count = sosuso_price_count - 12
        price_entry_sosuso.delete(0, END)
        price_entry_sosuso.insert(0, sosuso_price_count)


plus_button_sosuso = Button(frame, text='+', bg='white', fg='green', command=plus_entry)
plus_button_sosuso.place(x=698, y=395)
negative_button_sosuso = Button(frame, text='-', bg='white', fg='green', command=negative_but)
negative_button_sosuso.place(x=750, y=395)
display_sosuso = Entry(frame, width=1, textvariable=IntVar())
display_sosuso.place(x=727, y=398)
price_entry_sosuso = Entry(frame, width=5, textvariable=IntVar())
price_entry_sosuso.place(x=775, y=401)
price_label_sosuso = Label(frame, text='AZN', bg='white')
price_label_sosuso.place(x=810, y=400)
pizza4_button = Button(frame, text='Səbətə əlavə et', width=15, height=2, bg='#6F4E37', fg='white', font='20',
                       command=multifuc_sosuso)
pizza4_button.place(x=690, y=500)
pizza_list.insert(7, display_sosuso.get())

Button(frame, text='Sifarişi yekunlaşdırmaq', width=20, height=0, bg='#6F4E37', fg='white', font='ariel 10 bold',
       command=order).place(x=1185, y=60)

# count
khabab_price_count = 0
khabab_count = 0
barbacue_price_count = 0
barbacue_count = 0
sosuso_count = 0
sosuso_price_count = 0
mixed_count = 0
mixed_price_count = 0

salyami_price_count = 0
salyami_count = 0
havay_price_count = 0
havay_count = 0
rengbereng_price_count = 0
renbereng_count = 0
serq_t_price_count = 0
serq_t_count = 0

my_pic1 = Image.open('../../Desktop/pro/img/pizza1.jpg')
resized1 = my_pic1.resize((230, 230), Image.ANTIALIAS)
new_pic1 = ImageTk.PhotoImage(resized1)
pizza1_label = Label(frame, image=new_pic1, bg='white')
pizza1_label.place(x=40, y=50)

my_pic2 = Image.open('../../Desktop/pro/img/pizza4.jpg')
resized2 = my_pic2.resize((230, 230), Image.ANTIALIAS)
new_pic2 = ImageTk.PhotoImage(resized2)
pizza2_label = Label(frame, image=new_pic2, bg='white')
pizza2_label.place(x=345, y=50)

my_pic3 = Image.open('../../Desktop/pro/img/pizza5.jpg')
resized3 = my_pic3.resize((230, 230), Image.ANTIALIAS)
new_pic3 = ImageTk.PhotoImage(resized3)
pizza3_label = Label(frame, image=new_pic3, bg='white')
pizza3_label.place(x=640, y=50)

my_pic4 = Image.open('../../Desktop/pro/img/pizza0.jpg')
resized4 = my_pic4.resize((230, 230), Image.ANTIALIAS)
new_pic4 = ImageTk.PhotoImage(resized4)
pizza4_label = Label(frame, image=new_pic4, bg='white')
pizza4_label.place(x=935, y=50)

my_pic5 = Image.open('../../Desktop/pro/img/pizza3.jpg')
resized5 = my_pic5.resize((230, 230), Image.ANTIALIAS)
new_pic5 = ImageTk.PhotoImage(resized5)
pizza5_label = Label(frame, image=new_pic5, bg='white')
pizza5_label.place(x=40, y=600)

my_pic6 = Image.open('../../Desktop/pro/img/pizza2.jpg')
resized6 = my_pic6.resize((230, 230), Image.ANTIALIAS)
new_pic6 = ImageTk.PhotoImage(resized6)
pizza6_label = Label(frame, image=new_pic6, bg='white')
pizza6_label.place(x=345, y=600)

my_pic7 = Image.open('../../Desktop/pro/img/pizza7.jpg')
resized7 = my_pic7.resize((230, 230), Image.ANTIALIAS)
new_pic7 = ImageTk.PhotoImage(resized7)
pizza7_label = Label(frame, image=new_pic7, bg='white')
pizza7_label.place(x=640, y=600)

my_pic8 = Image.open('../../Desktop/pro/img/pizza6.jpg')
resized8 = my_pic8.resize((230, 230), Image.ANTIALIAS)
new_pic8 = ImageTk.PhotoImage(resized8)
pizza8_label = Label(frame, image=new_pic8, bg='white')
pizza8_label.place(x=935, y=600)


def info_pizza():
    Label(frame, text='Barbekyu', bg='white', fg='green', font='ariel 14 bold').place(x=83, y=310)
    Label(frame, text='Kabab', bg='white', fg='green', font='ariel 14 bold').place(x=415, y=310)
    Label(frame, text='Sosuso', bg='white', fg='green', font='ariel 14 bold').place(x=710, y=310)
    Label(frame, text='Qarışıq', bg='white', fg='green', font='ariel 14 bold').place(x=1005, y=310)

    Label(frame, text='Havay', bg='white', fg='green', font='ariel 14 bold').place(x=95, y=1000)
    Label(frame, text='Şərq Toyuğu', bg='white', fg='green', font='ariel 14 bold').place(x=390, y=1000)
    Label(frame, text='Salyami', bg='white', fg='green', font='ariel 14 bold').place(x=715, y=1000)
    Label(frame, text='Rəngbətəng', bg='white', fg='green', font='ariel 14 bold').place(x=995, y=1000)

    Label(frame,
          text='Toyuq filesi, "Mozerella" pendiri,bolqar\nbibər,pomidor,italyan otlari,zeytun yağı \n"Dadim" sousu , "Barbekyu" sousu\n',
          bg='white').place(x=30, y=335)
    Label(frame, text='Zeytun yağı, “Mozarella” pendiri, \nbadımcan, pomidor, bolqar bibəri, lülə \nkəbab, reyhan\n',
          bg='white').place(x=360, y=335)
    Label(frame,
          text=' "Mozerella" pendiri, sucuq sosiska \nsalyami italyan otlari zeytun yağı \n"Dadim" sousu , "Barbekyu" sousu\n',
          bg='white').place(x=650, y=335)
    Label(frame,
          text='“Mozarella” pendiri, toyuq filesi, bolqar\n bibəri, pomidor, göbələk, italyan otları, \n“Dadım” sousu, zeytun yağı',
          bg='white').place(x=940, y=335)

    # havay
    Label(frame, text='Vetçina, “Mozarella” pendiri, ananas,\n toyuq filesi, zeytun yağı, “Dadım” sousu',
          bg='white').place(x=40, y=1300)
    # serqtoyuqu
    Label(frame,
          text='“Mozarella” pendiri, toyuq filesi, zeytun,\n bolqar bibəri, pomidor, göbələk, italyan \notları, qara zeytun, “Dadım” sousu,\n zeytun yağı, ispanaq',
          bg='white').place(x=360, y=1300)
    # salyami
    Label(frame, text=' “Mozarella” pendiri, pomidor, salyami,\n ispanaq, italyan otları, zeytun yağı,\n “Dadım” sousu',
          bg='white').place(x=650, y=1300)
    # rengbereng
    Label(frame,
          text='“Mozarella” pendiri, badımcan, kartof fri,\n bildirçin yumurtası, zeytun, bolqar bibəri,\n yerkökü, pomidor, göbələk, reyhan, italyan \notları, zeytun yağı, qara zeytun,\n “Dadım” sousu, “Çedder” pendiri',
          bg='white').place(x=995, y=1300)

    Label(frame, text='28sm   12.50AZN ', bg='white', font='ariel 10 bold').place(x=400, y=450)
    Label(frame, text='28sm   12AZN ', bg='white', font='ariel 10 bold').place(x=700, y=450)
    Label(frame, text='28sm   10AZN', bg='white', font='ariel 10 bold').place(x=90, y=450)
    Label(frame, text='28sm   10AZN ', bg='white', font='ariel 10 bold').place(x=1000, y=450)

    Label(frame, text='28sm   11AZN ', bg='white', font='ariel 10 bold').place(x=400, y=1300)
    Label(frame, text='28sm   13AZN ', bg='white', font='ariel 10 bold').place(x=700, y=1300)
    Label(frame, text='28sm   10AZN', bg='white', font='ariel 10 bold').place(x=90, y=1300)
    Label(frame, text='28sm   9.50AZN ', bg='white', font='ariel 10 bold').place(x=1000, y=1300)

    welcome = Label(frame, font='ariel 14 bold', bg='white')
    welcome.pack()

    def labelconfig():
        color = '#' + ('%06x' % random.randint(0, 0xFFFFFF))
        welcome.config(text="Xoş Gəlmisiniz!", fg=str(color))
        window.after(1000, labelconfig)

    labelconfig()


info_pizza()

window.bind('<Return>', password_admin)
window.mainloop()
