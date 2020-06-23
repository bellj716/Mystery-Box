from tkinter import *
from functools import partial       # to prevent unwanted windows

import random


class Game:
    def __init__(self):

        #Formating variable
        self.game_stats_list = [50, 6]

        # in actual program this is blank and is populated with user calculations
        self.round_stats_list = ["is this printing?"]

        self.game_frame = Frame()
        self.game_frame.grid()

        # heading row
        self.heading_label = Label(self.game_frame, text = "Play...",
                                   font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # History Button (row 1)
        self.stats_button = Button(self.game_frame, text="Game Stats", font="Arial 14", padx=10, pady=10,
                                   command=lambda: self.to_stats(self.round_stats_list))
        self.stats_button.grid(row=1)

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)

class GameStats:
    def __init__(self, partner, game_history, game_stats):

        print(game_history)

        # disable stats button
        partner.stats_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12"

        # sets up child window ie stats box
        self.stats_box = Toplevle()

        # if users press cross ar top closes stats and releases stats button

        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # set up GUI Frame
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # set up stats heading
        self.stats_heading_label = Label(self.stats_frame, text="Game Statistics",
                                         font="Arial 19 bold")
        self.stats_heading_label.grid(row=0)

        # to export
        self.export_instructions = Label(self.stats_frame, text="Here are your Game Statistics. "
                                                                "Please y=use the export button to "
                                                                "access the results of each "
                                                                "round that you played", wrap=250,
                                         font="Arial 10 italic", justify=LEFT, fg="green", padx=10, pady=10)
        self.export_instructions.grid(row=1)

        # starting balance
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        self.start_balance_label = Label(self.details_frame,  text="Starting Balance:", font=heading,
                                         anchor="e")
        self.start_balance_label.grid(row=0, column=0, padx=0)

        self.start_balance_value_label = Label(self.details_frame, font=content,
                                                text="${}".format(game_stats[0]),
                                               anchor="w")
        self.start_balance_value_label.grid(row=0, column=1, padx=0)

        # current balance
        self.current_balance_label = Label(self.details_frame, text="current Balance:", font=heading,
                                         anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)

        self.current_balance_value_label = Label(self.details_frame, font=content,
                                                 text="${}".format(game_stats[1]),
                                               anchor="w")
        self.current_balance_value_label.grid(row=1, column=1, padx=0)

        if game_stats[1] > game_stats[0]:
            win_loss = "Amount Won: "
            amount = game_stats[1] - game_stats[0]
            win_loss_fg = "green"

        else:
            win_loss = "Amount Lost: "
            amount = game_stats[0] - game_stats[1]
            win_loss_fg = "#660000"

        # amount won / lost
        self. win_loss_label = Label(self.details_frame, text=win_loss, font=heading, anchor="e")
        self.win_loss_label.grid(row=2, column=0, padx=0)

        self.win_loss_value_label = Label(self.details_frame, font=content,
                                          text="${}".format(amount),
                                          fg=win_loss_fg, anchor="w")
        self.win_loss_value_label.grid(row=2, colum=1, padx=0)

        # rounds played
        self.games_played_label = Label(self.details_frame, text="Rounds Played: ",
                                        font=heading, anchor="e")
        self.games_played_label.grid(row=4, column=0, padx=0)

        self.games_played_value_label = Label(self.details_frame, font=content,
                                          text=len(game_history), anchor="w")
        self.win_loss_value_label.grid(row=4, colum=1, padx=0)

        # dismiss button (row 2)
        self.dismiss_btn = Button(self.stats_frame, text="Dismiss", width=10,
                                  bg="#660000", font="Arial 14 bold", fg="white",
                                  command=partial(self.close_stats, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_stats(self, partner):
        # put help button back to normal
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()

    # main routine
    if __name__ == "__main__":
        root = Tk()
        root.title("Stats Box")
        something = Game(root)
        root.mainloop()


























