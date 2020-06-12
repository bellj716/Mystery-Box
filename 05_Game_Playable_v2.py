from tkinter import *
from functools import partial   # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # Gui to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.push_mne_button = Button(text="Push Me", command=self.to_game)
        self.push_mne_button.grid(row=0, pady=10)

    def to_game(self):

        # retrieve starting blanace
        starting_balance = 50
        stakes = 2

        Game(self, stakes, starting_balance)

        # hide start up window
        root.withdraw
