# -*- coding: utf-8 -*-
"""
Created on Wed Dec 06 14:10:45 2017

@author: h.gibb
"""

import visa
from Tkinter import *

rm = visa.ResourceManager()
my_instrument = rm.open_resource("GPIB0::23::INSTR")
my_instrument.write("END 2")

class Application(Frame):
    def getID(self):
        print("Getting ID:")
        print(my_instrument.query("ID?"))

    def getV(self):
        print("Getting Voltage:")
        print(my_instrument.query("DCV"))


    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.ID = Button(self)
        self.ID["text"] = "ID",
        self.ID["command"] = self.getID

        self.ID.pack({"side": "left"})

        self.V = Button(self)
        self.V["text"] = "Voltage",
        self.V["command"] = self.getV

        self.V.pack({"side": "left"})


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()