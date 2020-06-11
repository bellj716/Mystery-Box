# use randint to randomly generate all the numbers 1,2,3,4

import random
NUM_TRIALS = 10

for item in range(0, NUM_TRIALS):

    # randint finds numbers between given end points, including both endpoints.
    prize_num = random.randint(1,4)
    print(prize_num)