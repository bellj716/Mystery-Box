from tkinter import *
from functools import partial   # To prevent unwanted windows
import random

class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # set initial balance to zero
        self.starting_funds = IntVar()
        self.starting_funds.set(0)

        self.mystery_box_label(self.start_frame, text="Mystery Box Game"
                               font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

        self.mystery_instructions = Label(self.start_frame)
