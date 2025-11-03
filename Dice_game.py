#
# 
import random

def roll():
    min_val=1
    max_val=6
    roll=random.randint(min_val,max_val)

    return roll

while True:
    players=input("Enter the number of players(2-4): \n")
    if players.isdigit():
        players=int(players)
        if 1<=players<=4:
            break
        else:
            print("number must be between 2-4\n")
    else:
        print("Invalid, try again\n")

max_score=50
player_scores=[0 for _ in range(players)]


while max(player_scores)<max_score:
  
  for player_idx in range(players):
        print("\nPlayer", player_idx +1, "turn has just started!\n")
     
        current_score=0
        while True:
           should_roll=input("Would you like to roll? y\n")
           if should_roll.lower()!="y":
                break

           value=roll()
           if value==1:
               print("You rolled a 1! Turn over, no points added.\n")
               break
           else:
              current_score+=value
              print("you rolled a:", value)
        print("your score is:", current_score)
           
        player_scores[player_idx]+= current_score
        print("your total score is: ", player_scores[player_idx])

max_score=max(player_scores)
winning_idx=player_scores.index(max_score)
print("Player number ", winning_idx+1," is the winner and scored: ",max_score)
