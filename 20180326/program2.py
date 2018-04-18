"""
Jezz Chrimes 2018
Date Created: 2018/03/26
Date Modified: 2018/03/26
Version: 0.1

A basic Tkinter Window

"""

import tkinter # Import the Tkinter File
from numguess import numGuess ## Import the number gueser module

class graphUI(tkinter.Tk):

    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
    def higherButtonAction(self):
        self.guesser.valueHigher()
    def lowerButtonAction(self):
        self.guesser.valueLower()
    def initialize(self):
        label1 = tkinter.Label(self, text="Number Guesser").grid(row=0)
        higherButton = tkinter.Button(self, text="Higher").grid(row=1, column=0)
        lowerButton = tkinter.Button(self, text="Higher").grid(row=1, column=1)

