import tkinter
from tkinter import *
from tkinter.ttk import *
from mbot import *
#establish system
m = tkinter.Tk()
m.title("Mbot")
m.geometry("400x250")

#blank column for padding
blank1 = Label(m,text="",width=7)
blank1.grid(column=0,row=0)

#line with introduction and will have response
introductions = Label(m,text="Hello World I am Mbot, your mushroom loving companion",width=60,wraplength=350 )
introductions.grid(column=1,row=0,rowspan=2)

#line with prompt
asking = Label(m, text="Please ask a question below and I will do my best to answer:", width=60)
asking.grid(column=1,row=2)

#gets user input
userinput = Entry(m, width=60)
userinput.grid(column=0,columnspan=2,row=3)

#what happens when user submits
def clicked():
    input = userinput.get()
    introductions.configure(text = mushroom(input))

#submit button
Submit = Button(m, text="Submit",command=clicked,width=10)
Submit.grid(column=1,row=4)

m.mainloop()