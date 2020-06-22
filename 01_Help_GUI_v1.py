from tkinter import *
from functools import partial # To prevent unwanted windows

import random

if __name__ == '__main__':
    class Converter:
        def __init__(self, parent):

            # Gui to get starting balance and stakes
            self.start_frame = Frame(padx=10,  pady=10)
            self.start_frame.grid()

            # Mystery Heading heading row 1
            self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game", font="Arial 20 bold")
            self.mystery_box_label.grid(row=1)

            #help button (row 2)
            self.help_button = Button(self.start_frame, text="help", command=self.help)
            self.help_button.grid(row=2, pady=10)

        def help(self):
            get_help = Help(self)

class Help:
    def __init__(self, partner):

        #disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (ie: help box)
        self.help_box = Toplevel()

        #if user press cross instead of dismiss, close help and release help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up gui frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        #set up help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help and Instructions",
                                 font="Arial 14 bold")
        self.how_heading.grid(row=0)

        help_text="Choose an amount to play with and then choose the stakes. " \
                  "higher stakes cost more per round but you can win more as " \
                  "well. \n\n" \
                  "When you enter the play area, you will see three mystery " \
                  "boxes. To reveal the contents of the boxes, click the " \
                  "'Open Boxes' button. If you don't have enough money to play, " \
                  "the button will turn red an tou will need to quit the game. \n\n" \
                  "the contents of the boxes will be added to you balance. " \
                  "the boxes could contain...\n\n" \
                  "Low: Lead ($0) | Copper ($1) | Silver ($2) | Gold ($10)\n" \
                  "Medium: Lead ($0) | Copper ($2) | Silver ($4) | Gold ($25)\n" \
                  "Low: Lead ($0) | Copper ($5) | Silver ($10) | Gold ($50)\n\n" \
                  "If each box contains gold, you earn #30 (low stakes). If " \
                  "the contained copper, silver and gold, you would recieve " \
                  "$13 ($1 + $2 + $10) and so on."

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        #dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10,
                                  bg="#660000", font="Arial 14 bold", fg="white",
                                  command=partial(self.close_help,partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
