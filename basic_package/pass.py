from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk() 
GUI.title('')
GUI.geometry('500x400')

L1 = Label (GUI,text='Password',font=('Angsana New',30),fg='red')
L1.place(x=30,y=20)

def Button1():
    text = 'JamesMoriarty'
    messagebox.showinfo('mangmoolp@gmail.com',text)
FB1 = Frame(GUI) 
FB1.place(x=80,y=180)
B1 = ttk.Button(FB1,text='mangmoolp@gmail.com',command=Button1)
B1.pack(ipadx=20,ipady=20)


def Button2():
    text = ' aptx4869'
    messagebox.showinfo('mangmoolp@gmail.com',text)

FB2 = Frame(GUI)
FB2.place (x=80,y=180)
B2 = ttk.Button(FB2,text='LINE',command=Button2)
B2.pack(side=LEFT)

def Button3():
    text = ' JamesMoriarty4869'
    messagebox.showinfo('mangmoolp@gmail.com',text)

FB3 = Frame(GUI)
FB3.place(x=80,y=180)
B3 = ttk.Button(FB1,text='Skilllane',command=Button3)
B3.pack(ipadx=20,ipady=20) 

def Button4():
    text = ' SH4869jobTH'
    messagebox.showinfo('mangmoolp@gmail.com',text)

FB4 = Frame(GUI)
FB4.place(x=80,y=180)
B4 = ttk.Button(FB2,text='jobthai',command=Button4)
B4.pack(side=LEFT)

def Button5():
    text = ' Sherlock221B.'
    messagebox.showinfo('TrueID',text)

FB5 = Frame(GUI)
FB5.place(x=80,y=180)
B5 = ttk.Button(FB1,text='TrueID',command=Button5)
B5.pack(ipadx=20,ipady=20) 

def Button6():
    text = ' SherlockHolmes'
    messagebox.showinfo('Sherlock_kid@hotmail.com',text)

FB6 = Frame(GUI)
FB6.place(x=80,y=180)
B6 = ttk.Button(FB2,text='FaceBook',command=Button6)
B6.pack(side=LEFT)

def Button7():
    text = ' JamesMoriarty'
    messagebox.showinfo('nandnqualitysupply@gmail.com',text)

FB7 = Frame(GUI)
FB7.place(x=80,y=180)
B7 = ttk.Button(FB1,text='nandnqualitysupply@gmail.com',command=Button7)
B7.pack(ipadx=20,ipady=20)

GUI.mainloop()
