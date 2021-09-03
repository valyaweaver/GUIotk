import sqlite3
from tkinter import *
from datetime import datetime
from tkinter import ttk
import socket

window = Tk()
window.title("OTK")
window.geometry('1000x800')
global list
list=[]
def entr1(event):
    init()
    txt1.focus()
    # btn.bind('<Return>', clicked)

def entr2(event):
    sern()
    txt2.focus()

def entr3(event):
    defec()
    txt.focus()

def init():
    global operator
    operator = format(txt.get())
    txt1.focus()
    txt1.bind('<Return>', entr2)
   # txt1.bind('<Return>', entr2)

def sern():
    global sn
    global tistamp
    sn = format(txt1.get())
    lbl1.configure(text=sn, font='Times 25')
    txt2.focus()
    txt2.bind('<Return>', entr2)
   # txt1.bind('<Return>', entr2)
def defec():
    global defect
    defect = format(txt2.get())

    if defect != 'stop' and defect != 'reset':

        list.append(defect)
        lbl2.configure(text=list, font='Times 25')
        txt2.delete(0, END)
        txt2.focus()
    if defect == 'stop':
        tistamp = str(datetime.now())
        string = ''.join(list)
        f = open("C:/Users/hp/PycharmProjects/gui otk/otk.txt", 'a')
        f.write(str(sn + ' ' + operator + ' ' + tistamp + ' '))
        f.write(str(string+'\n'))
        f.close()
        lbl1.configure(text='', font='Times 25')
        lbl2.configure(text='', font='Times 25')
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt1.focus()
        list.clear()
    if defect == 'reset':
        lbl1.configure(text='', font='Times 25')
        lbl2.configure(text='', font='Times 25')
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt1.focus()
        list.clear()

   # txt1.bind('<Return>', entr2)



lbl = Label(window, font='Times 25', text="ОПЕРАТОР")
lbl.grid(column=3, row=1)
lbl1 = Label(window, font='Times 25', text="Serial number")
lbl1.grid(column=3, row=2)
lbl2 = Label(window, font='Times 25', text="Serial number")
lbl2.grid(column=3, row=3)

txt = Entry(window, font='Times 25', width=20)
txt.grid(column=1, row=1)
txt.focus()
txt.bind('<Return>', entr1)
txt1 = Entry(window, font='Times 25', width=20)
txt1.grid(column=1, row=2)

txt2 = Entry(window, font='Times 25', width=20)
txt2.grid(column=1, row=3)

btn = Button(window, text="go",font='Times 25', command=init)
btn.grid(column=2, row=1)
btn1 = Button(window, text="go",font='Times 25', command=sern)
btn1.grid(column=2, row=2)
btn2 = Button(window, text="go",font='Times 25', command=defec)
btn2.grid(column=2, row=3)

window.mainloop()
