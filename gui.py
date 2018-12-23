#! /usr/bin/env python

'''
gui.py
'''
import tkinter as tk
import csv
from function_factory import TaskFunction
padding_difference = 5
font_size_heading = 21
font_size = 12

#import pudb
#pudb.set_trace()

class GuiBuilder:
    def __init__(self, master, csv_file):
        self.config = GuiBuilder.loadConfig(csv_file)

        frame = tk.Frame(master)
        frame.pack()
        self.heading = tk.Label(frame,text="GUI App",
                           font=("Courier", 
                                 font_size_heading),
                           background="white",
                           fg="black"
                           )
        self.heading.grid(row=0, columnspan=2)
        self.lblArea = tk.Label(frame,text="Area:",
                             font=("Courier", font_size),
                             background="white",
                             fg="black")

        self.entArea = tk.Entry(frame,
                             background="white",
                             fg="black"
                            )

        self.lblSkill = tk.Label(frame,
                              text="Skill:",
                              font=("Courier", font_size),
                              fg="black",
                              background="white")

        self.entSkill = tk.Entry(frame,
                             background="white",
                             fg="black"
                            )
        self.lblSize = tk.Label(frame,
                             text="Size:",
                             font=("Courier", font_size),
                             fg="black",
                             background="white")

        self.entSize = tk.Entry(frame,
                             background="white",
                             fg="black"
                            )

        self.seniorVar = tk.IntVar()
        self.chkSenior = tk.Checkbutton(
            frame, text="Senior",
            font=("Courier", font_size),
            fg="black", background="white",
            variable=self.seniorVar
        )

        self.lblMessage = tk.Label(frame,
                                text="Message:",
                                font=("Courier", font_size),
                                fg="black",
                                background="white"
                               )
        self.txtMessage = tk.Text(frame,
                               background="white",
                               fg="black",
                               width=60,
                               height=25
                              )
        self.lblCategory = tk.Label(frame,
                                 text="Category",
                                 font=("Courier", font_size),
                                 fg="black", background="white")
        # Dropdowns
        self.catVar = tk.StringVar(frame)
        self.catVar.set("Category")
        self.drpCategory = tk.OptionMenu(frame,
                                      self.catVar,
                                      *self.getCategories(),
                                      command=self.resetDrpTask
                                     ) 

        self.lblTask = tk.Label(frame,
                             text="Tasks",
                             font=("Courier", font_size),
                             fg="black", background="white")
        self.taskVar = tk.StringVar(frame)
        self.taskVar.set("Do Task")
        self.tasks = ["Do Task"]
        self.drpTask = tk.OptionMenu(frame,
                                      self.taskVar,
                                      *self.tasks
                                     ) 
        self.lblError = tk.Label(frame,
                             text="",
                             fg="red")
        self.btnGo = tk.Button(frame, text="GO", fg="red",
                               command=self.onGoClicked)
        self.btnQuit = tk.Button(frame, text="QUIT", fg="red",
                               command=self.onQuitClicked)
        # Label Positioning
        self.lblArea.grid(row=1, pady=padding_difference, sticky=tk.EW)
        self.lblSkill.grid(row=2, pady=padding_difference, sticky=tk.EW)
        self.lblSize.grid(row=3, pady=padding_difference, sticky=tk.EW)
        self.chkSenior.grid(row=4, pady=padding_difference,
                            columnspan=2, sticky=tk.EW)
        self.lblMessage.grid(row=5, pady=padding_difference, sticky=tk.EW)
        self.lblCategory.grid(row=7, pady=padding_difference, sticky=tk.EW)
        self.lblTask.grid(row=8, pady=padding_difference, sticky=tk.EW)
        self.lblError.grid(row=9, columnspan=2, pady=padding_difference, sticky=tk.EW)



        # Entry Positions
        self.entArea.grid(row=1, column=1)
        self.entSkill.grid(row=2, column=1)
        self.entSize.grid(row=3, column=1)
        self.txtMessage.grid(row=6, columnspan=2)

        # Dropdown positions
        self.drpCategory.grid(row=7, column=1, sticky=tk.EW)
        self.drpTask.grid(row=8, column=1, sticky=tk.EW)

        # Button Position
        self.btnGo.grid(row=10, column=1, sticky=tk.EW)
        self.btnQuit.grid(row=10, column=0, sticky=tk.EW)
    

    def resetDrpTask(self, param2):
        '''
        '''
        cat = self.catVar.get()
        self.drpTask['menu'].delete(0, 'end')
        self.taskVar.set("Do Task") 
        self.tasks = self.getTasks(cat)
        for _task in self.tasks:
            self.drpTask['menu'].add_command(
            label=_task,
            command=tk._setit(self.taskVar, _task))

    def onQuitClicked(self):
        '''
        '''
        exit(0)

    def onGoClicked(self):
        '''
        '''
        _cat = self.catVar.get()
        _task = self.taskVar.get()
        _func = self.getFunctions(_cat, _task)
        if _func:
            self.lblError['text'] = ""
            _area = self.entArea.get()
            _skill = self.entSkill.get()
            _size = self.entSize.get()
            _is_senior = self.seniorVar.get()
            _msg = self.txtMessage.get("1.0","end-1c")


            obj = TaskFunction.factory(_func)
            obj.call(_area, _skill, _size, _is_senior, _msg)
        else:
            self.lblError['text'] = "Something wrong"

    def getCategories(self):
        '''
        returns categories
        '''
        return list(self.config.keys())

    def getTasks(self, category):
        '''
        returns tasks based on category
        '''
        _cat = category.strip()
        return self.config[_cat]['description']

    def getFunctions(self, _cat, task):
        '''
        returns name of functions based on category and task
        '''
        try:
            _index = self.config[_cat]['description'].index(task)
            return self.config[_cat]['functions'][_index]
        except:
            return None


    @staticmethod
    def loadConfig(csv_file):
        '''
        '''
        config = { }
        with open(csv_file) as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                _cat = row['category'].strip()
                _fun = row['functionIdentifier'].strip()
                _desc = row['description'].strip()
                if _cat in config:
                    config[_cat]['functions'].append(_fun)
                    config[_cat]['description'].append(_desc)
                else:
                    config[_cat] = {}
                    config[_cat]['functions'] = []
                    config[_cat]['functions'].append(_fun)

                    config[_cat]['description'] = []
                    config[_cat]['description'].append(_desc)
        return config

root = tk.Tk()
root.title("App")
b = GuiBuilder(root, "tkOptions.csv")
root.mainloop()

