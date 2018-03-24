#!/usr/bin/python3
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from db import DBConnect
from listTickets import ListTicket

#Config
conn = DBConnect()
root = Tk()
root.geometry('480x440')
root.title('Ticket Reservation')
root.configure(background='#FCAF3E')

#Style
style = Style()
style.theme_use('classic')
for elem in ['TLabel', 'TButton', 'TRadioutton']:
	style.configure(elem, background='#FCAF3E')

#Grid
labels = ['Full Name', 'Gender', 'Comment']
for i in range(3):
	Label(root, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)

BuList = Button(root, text='List Res.')
BuList.grid(row=3, column=2)
BuSubmit = Button(root, text='Submit')
BuSubmit.grid(row=3, column=3)

#Entries
fullname = Entry(root, width=30, font=('Arial', 11))
fullname.grid(row=0, column=1, columnspan=2)
SpanGender = StringVar()
Radiobutton(root, text='Male', value='male', variable=SpanGender).grid(row=1, column=1)
Radiobutton(root, text='Female', value='female', variable=SpanGender).grid(row=1, column=2)
comment = Text(root, width=30, height=15, font=('Arial', 11))
comment.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

def SaveData():
	msg = conn.Add(fullname.get(), SpanGender.get(), comment.get(1.0, 'end'))
	fullname.delete(0, 'end')
	comment.delete(1.0, 'end')
	showinfo(title='Add Info', message=msg)

def ShowList():
	listrequest = ListTicket()


BuSubmit.config(command=SaveData)
BuList.config(command=ShowList)

root.mainloop()