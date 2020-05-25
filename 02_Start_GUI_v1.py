from tkinter import *
from functools import partial   # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Mystery Heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

        # Initial Instructions (row 1)
        self.mystery_instructions = Label(self.strat_frame, font="Arial 10 italic",
                                          text="Please enter a dollar amount "
                                          "(between $5 and $50) in the box "
                                          "below. Then choose the stakes. "
                                          "The higher the stakes, the more "
                                          "you can win!", wrap=275, justify=LEFT,
                                          padx=10, pady=10)
        self.mystery_instructions.grid(row=1)

        # Entry box... (row 2)
        self.start_amount_entry = Entry(self.start_frame, font="Arial 16 bold")
        self.start_amount_entry.grid(row=2)

        # button frame (row 3)
        self.stakes_frame = Frame(self.start_frame)
        self.stakes_frame.grid

        # buttons go here
        button_font = "Arial 12 bold"
        # Play Button (row 3)
        self.lowstakes_button = Button(text="Low ($5)",
                                       command=lambda: self.to_game(1))
        self.lowstakes_button.grid(row=3, pady=10)

    def to_game(self, stakes):
        starting_balance = self.start_amount_entry.get()
        Game(self, stakes, starting_balance)


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # disable low stakes button
        partner.lowstakes_button.config(state=DISABLED)

        # Initialize
        self.balance = IntVar()

        # set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # GUI setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading row
        self.heading_label = Label(self.game_frame, text="Heading",
                                       font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # Balance Label
        self.balance_frame = Frame(self.game_frame)
        self.balance_frame.grid(row=1)

        self.balance_label = Label(self.game_frame, text="Balnace...")
        self.balance_label.grid(row=2)

        self.play_button = Button(self.game_frame, text="Gain", padx=10,
                                  pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=3)


    def reveal_boxes(self):
        # retrieve the balanace from the initial
        current_balance = self.balance.get()

        # Adjust the balance (subtract game cost, add payout)
        # for testing purposes just add 2
        current_balance += 2

        # set balance to adjusted balance
        self.balance.set(current_balance)

        # Edit label so user can see their balance
        self.balance_label.configure(text="Balance: {}".format(current_balance))


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()