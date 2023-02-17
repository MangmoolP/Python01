from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
GUI = Tk() 
GUI.title('อ่านหนังสือ')
GUI.geometry('500x600')

L1 = Label (GUI,text='อ่านต่อหน้าที่',font=('Angsana New',30),fg='red')
L1.place(x=30,y=20)

def Button1():
    text = 'บทที่ 3'
    messagebox.showinfo('Sherlock Holmes',text)
photo = PhotoImage(file="SH.png")
Button(root,text="Sherlock Holmes",image=photo)

def Button2():
    text = 'หน้าที่ 86'
    messagebox.showinfo('Harry Potter',text)
FB2 = Frame(GUI) 
FB2.place(x=80,y=280)
B2 = ttk.Button(FB2,text='Harry Potter',command=Button2)
B2.pack(ipadx=20,ipady=20)


def Button3():
    text = 'หน้าที่ 153'
    messagebox.showinfo('Money Mindset',text)
FB3 = Frame(GUI) 
FB3.place(x=80,y=380)
B3 = ttk.Button(FB3,text='Money Mindset',command=Button3)
B3.pack(ipadx=20,ipady=20)
root.mainloop()
GUI.mainloop()
