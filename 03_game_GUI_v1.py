from tkinter import *
from functools import partial   # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):
        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.push_me_button = Button(text="Push Me", command=self.to_game)
        self.push_me_button.grid(row=0, pady=10)

    def to_game(self):

        # retrieve starting blanace
        starting_balance = 50
        stakes = 1

        Game(self, stakes, starting_balance)

class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # Initialize variables
        self.balance = IntVar()

        # set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # Get value of stakes ( use as multiplier when calculating winnings
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # GUI setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading row
        self.heading_label = Label(self.game_frame, text="Heading",
                                       font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # instructions label
        self.instructions_label = Label(self.game_frame, wrap=300, justify=LEFT,
                                        text="Press <enter> or click the 'Open "
                                             "Boxes' button to reveal the contents "
                                             "of the mystery boxes.", font="Aria 10", padx=10, pady=10)

        # boxes go here (row 2)
        box_text = "Arial 16 bold"
        box_back = "#b9ea96"
        box_width = 5
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        self.prize1_label = Label




        # Balance Label
       # self.balance_frame = Frame(self.game_frame)
       # self.balance_frame.grid(row=1)

        #self.balance_label = Label(self.game_frame, text="Balnace...")
        #self.balance_label.grid(row=2)

        #self.play_button = Button(self.game_frame, text="Gain", padx=10,
                     #             pady=10, command=self.reveal_boxes)
        #self.play_button.grid(row=3)


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