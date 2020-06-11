# use randint to randomly generate all the numbers 1,2,3,4

import random

NUM_TRIALS = 100
winnings = 0

cost = NUM_TRIALS * 5

for item in range(0, NUM_TRIALS):
    #prize = ""
    round_winnings = 0

    for thing in range(0, 3):

        # randint finds numbers between given end points, including both endpoints.
        prize_num = random.randint(1,10)
        #prize += " "
        if prize_num == 1:
            #one in ten chance of getting gold
            #prize += "Gold"
            round_winnings += 5
        elif 1 < prize_num <= 3:
            #get silver if its a 2 or a 3
            #prize += "Silver"
            round_winnings += 2
        elif 3 < prize_num <= 7:
            #copper if its 4-7 40% chance
            #prize += "Copper"
            round_winnings += 1
        else:
            #prize += "Lead"

    print("You won {} which is worth {}".format(prize, round_winnings))
    winnings += round_winnings

print("Paid In: ${}".format(cost))
print("Paid Out: ${}".format(winnings))

if winnings > cost:
    print("You came out ${} ahead".format(winnings - cost))
else:
    print("Sorry, you lost ${}".format(cost - winnings))