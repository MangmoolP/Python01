from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox

###################################################
GUI = Tk() #หน้าจอหลัก
GUI.title('โปรแกรมบันทึกข้อมูล')#ชื่อโปรแกรม
GUI.geometry('500x400')# ขนาดโปรแกรม

L1 = Label (GUI,text='โปรแกรมให้ความรู้',font=('Angsana New',30),fg='red')
L1.place(x=30,y=20)
###############################################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=80,y=180)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20) #B2.pack(ipadx=20,ipady20) ความหมายเดียวกัน
#####################################################
def Button3():
    text = 'Python 101,Math'
    messagebox.showinfo('วิชาเรียนวันที่ 10-20 ก.พ.',text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=80,y=180)
B3 = ttk.Button(FB1,text='สัปดาห์นี้เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20) 
GUI.mainloop()
