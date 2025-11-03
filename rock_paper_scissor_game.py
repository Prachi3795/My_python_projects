#It takes iput from user as rock, paper or scissor and then compares to the computer
#choice, 

import random

user_wins =0
computer_wins=0
options=["rock","paper","scissor"]

while True:
    user_input=input("Rock/Paper/Scisors or Q to quit\n").lower()
    if user_input =="q":
        break
    if user_input not in options:
        print("Please enter a valid option\n")
        continue
    if user_input in options:
     
     random_number=random.randint(0,2)
    #rock: 0, paper: 1, scissor: 2
    computer_pick=options[random_number]
    print("computer picked: ", computer_pick)
    if user_input=="rock" and computer_pick=="scissor":
        print("You won!")
        user_wins+=1
    elif user_input=="paper" and computer_pick=="rock":
        print("You won!")
        user_wins+=1
    elif user_input=="scissor" and computer_pick=="paper":
        print("You won!")
        user_wins+=1
    else:
        print("You Lost!")
        computer_wins+=1
    



print("you won "+str(user_wins)+" times")
print("Good bye!")