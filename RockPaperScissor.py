#Rock, Paper and Scissors Game

import random

while True:
    
    X= input("Enter Choice [Rock,Paper,Scissor]:")
    Y= ['Rock', 'Paper', 'Scissor']
    Z= random.choice(Y)
    print("You Choosed",X,"and Computer Choosed",Z)
    
    if  'X'=='Y':
        print("That's A Tie!!!")
        
    elif  Z == "Rock":
        if X == "Paper":
            print(" You Won !!")
        else:
            print("Rock smashes scissor. You lose!!!")
            
    elif  Z == "Paper":
        if X == "Scissor":
            print(" You Won!!")
        else:
            print("Paper covers rock... You lose!!!")
            
    elif  Z == "Scissor":
        if X== "Rock":
            print("You Won!!")
        else:
            print("Scissor cuts paper... You lose!!")
    else:
        print("Invalid Choice , Please Retry :(")
            
    A= input("Would you like to play again?[Y/N]:")
    if A == 'N':
        break
    elif A == "Y":
        continue
    else:
        print("Invalid Choice. Thank You!!")
        break
