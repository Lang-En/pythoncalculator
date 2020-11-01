#!/usr/local/bin/python3
from tkinter import *

root = Tk()

# Functionsc


def btclick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def btclear():
    e.delete(0, END)


def bt_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def bt_eql():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + float(second_number))

    if math == "subtraction":
        e.insert(0, f_num - float(second_number))

    if math == "multiplication":
        e.insert(0, f_num * float(second_number))

    if math == "addition":
        e.insert(0, f_num / float(second_number))


def bt_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def bt_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


def bt_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


root.title("Simplified Calculator")

# Entry Settings
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Buttons
bt1 = Button(root, text=1, padx=40, pady=20, command=lambda: btclick(1))
bt2 = Button(root, text=2, padx=40, pady=20, command=lambda: btclick(2))
bt3 = Button(root, text=3, padx=40, pady=20, command=lambda: btclick(3))
bt4 = Button(root, text=4, padx=40, pady=20, command=lambda: btclick(4))
bt5 = Button(root, text=5, padx=40, pady=20, command=lambda: btclick(5))
bt6 = Button(root, text=6, padx=40, pady=20, command=lambda: btclick(6))
bt7 = Button(root, text=7, padx=40, pady=20, command=lambda: btclick(7))
bt8 = Button(root, text=8, padx=40, pady=20, command=lambda: btclick(8))
bt9 = Button(root, text=9, padx=40, pady=20, command=lambda: btclick(9))
bt0 = Button(root, text=0, padx=40, pady=20, command=lambda: btclick(0))

btsub = Button(root, text="-", padx=41, pady=20, command=bt_sub)
btmul = Button(root, text="x", padx=40, pady=20, command=bt_mul)
btdiv = Button(root, text="÷", padx=41, pady=20, command=bt_div)
btadd = Button(root, text="+", padx=39, pady=20, command=bt_add)

btclear = Button(root, text="Clear", padx=39, pady=20, command=btclear)
bteql = Button(root, text="=", padx=79, pady=20, command=bt_eql)
# Slap the buttons on the screen
bt1.grid(row=3, column=0)
bt2.grid(row=3, column=1)
bt3.grid(row=3, column=2)

bt4.grid(row=2, column=0)
bt5.grid(row=2, column=1)
bt6.grid(row=2, column=2)

bt7.grid(row=1, column=0)
bt8.grid(row=1, column=1)
bt9.grid(row=1, column=2)

bt0.grid(row=4, column=0)
btclear.grid(row=4, column=1, columnspan=2)
btadd.grid(row=5, column=0)
bteql.grid(row=5, column=1, columnspan=2)

btsub.grid(row=6, column=0)
btmul.grid(row=6, column=1)
btdiv.grid(row=6, column=2)
#±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±#
root.mainloop()
