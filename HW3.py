from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import csv

def writecsv (datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)

def readcsv ():
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data

GUI = Tk() 
GUI.title('อ่านหนังสือ')
GUI.geometry('500x600')

L1 = Label (GUI,text='อ่านต่อหน้าที่',font=('Angsana New',30),fg='red')
L1.place(x=80,y=20)


LF1 = ttk.LabelFrame(GUI,text='ชื่อหนังสือ')
LF1.place(x=40,y=120)

v_data = StringVar() # ตัวแปรพิเศษที่ใช้กับข้อความใน GUI
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(pady=10,padx=10)

def SaveData():

    data = v_data.get() # ดึงข้อมูลจากตัวแปร s_data มาใช้งาน
    text = [data] # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง CSV
    v_data.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก


B1 = ttk.Button(LF1,text='บันทึก',command=SaveData)
B1.pack(ipadx=20,ipady=20)

LF2 = ttk.LabelFrame(GUI,text='อ่านต่อหน้าที่')
LF2.place(x=40,y=350)

s_data = StringVar() # ตัวแปรพิเศษที่ใช้กับข้อความใน GUI
E2 = ttk.Entry(LF2,textvariable=s_data,font=('Angsana New',25))
E2.pack(pady=10,padx=10)

def SaveData():

    data = s_data.get() # ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [data] # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง CSV
    s_data.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก


B2 = ttk.Button(LF2,text='บันทึก',command=SaveData)
B2.pack(ipadx=20,ipady=20)

GUI.mainloop()
