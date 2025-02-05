# Number Guessing Game

import random
ai = random.randint(1,100)
print("Welcome To Number Guessing Game[1-100]")

while True:
    hi = int(input("Enter Your Guessed Number:"))
    
    if hi>ai:
        print("Number is Smaller than your Guess",hi)
    elif hi<ai:
        print("Number is Bigger than your Guess",hi)
    elif hi==ai:
        print("Horray!! Your Guess is Correct .Thanks For Playing :)")
    else:
        while True:
            print("Something went wrong , ERROR 707")
