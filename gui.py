#! /usr/bin/env python

'''
gui.py
'''
from tkinter import *
padding_difference = 5
font_size_heading = 21
font_size = 15

class GuiBuilder:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.lblArea = Label(frame,text="Area:",
                             font=("Courier", font_size),
                             background="white",
                             fg="black")

        self.lblSkill = Label(frame,
                              text="Skill:",
                              font=("Courier", font_size),
                              fg="black",
                              background="white")

        self.lblSize = Label(frame,
                             text="Size:",
                             font=("Courier", font_size),
                             fg="black",
                             background="white")

        self.lblMessage = Label(frame,
                                text="Message:",
                                font=("Courier", font_size),
                                fg="black",
                                background="white"
                               )
        #senior = Label(root,text="Senior:",,fg="black",background="white")
        self.chkSenior = Checkbutton(frame, text="Senior:",
                                     font=("Courier", font_size),
                                     fg="black",background="white",
                                     )
        self.lblArea.pack()
        self.lblSkill.pack()
        self.lblSize.pack()
        self.lblMessage.pack()
        self.chkSenior.pack()

    def printMessage(self):
        print("Wow!")

root = Tk()
b = GuiBuilder(root)
root.mainloop()

