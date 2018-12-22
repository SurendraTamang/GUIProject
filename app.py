#!usr/bin/env python3
"""
GUI version of crawling

"""
from tkinter import *
padding_difference = 5
font_size_heading = 21
font_size = 15
OPTIONS1 = [
    "appliedminds",
"brassring",
"carbonfive",
"divergent",
"upkeep",
"workforcenow",
"xypro"
]
OPTIONS2=["evite",
"futuredontics",
"honey",
"hrcloud",
"nativo",
"neuralanalytics",
"nextgate",
"perrknight",
"prodege",
"snapnation"
]
root = Tk()
root.configure (background="white")
variable1 = StringVar(root)
variable1.set("Category")
variable2 = StringVar(root)
variable2.set("Do Task")

root.geometry("540x600")
root.resizable(width=False, height=False)
root.title("An app")
heading = Label(root,text="Crawling app",font=("Courier", font_size_heading),background="white",fg="black" ,pady=15)
heading.grid(row=0,column=1)
area = Label(root,text="Area:",font=("Courier", font_size),background="white",fg="black")
skill = Label(root,text="Skill:",font=("Courier", font_size),fg="black",background="white")
size = Label(root,text="Size:",font=("Courier", font_size),fg="black",background="white")
message = Label(root,text="Message:",font=("Courier", font_size),fg="black",background="white")
#senior = Label(root,text="Senior:",,fg="black",background="white")
senior = Checkbutton(root,text="Senior:",font=("Courier", font_size),fg="black",background="white",state=DISABLED)
category = Label(root,text="Category:",font=("Courier", font_size),fg="black",background="white")
task = Label(root,text="Task:",font=("Courier", font_size),fg="black",background="white")
w1 = OptionMenu(root,variable1,*OPTIONS1)
w2 = OptionMenu(root,variable2,*OPTIONS2)
btn1 = Button(root, text = "GO", fg = "red" )

entry_area = Entry(root,background="white",fg="black")
entry_skill = Entry(root,background="white",fg="black")
entry_size = Entry(root,background="white",fg="black")
entry_message = Text(root,background="white",fg="black" ,width=45,height=15)

area.grid(row=1 ,pady=padding_difference,sticky=W)
skill.grid(row=2, pady=padding_difference,sticky=W)
size.grid(row=3,pady=padding_difference,sticky=W)
message.grid(row=5,pady=padding_difference,sticky=W)
senior.grid(row=4,pady=padding_difference,sticky=W)
category.grid(row=7,pady=padding_difference,sticky=W)
task.grid(row=8,pady=padding_difference,sticky=W)
entry_area.grid(row=1,column=1)
entry_skill.grid(row=2, column=1)
entry_size.grid(row=3, column=1)
entry_message.grid(row=6,column=1)
w1.config(width=20,background="white",fg="black")
w1.grid(row=7,column=1)
w2.config(width=20,background="white",fg="black")
w2.grid(row=8,column=1)
btn1.grid(row=8,column=2)
root.mainloop()
