#Code ask for user input for different situtation and based on that adventure proceed further

name=input("Please enter your name\n")
print("Welcom "+ name + " to this adventure\n")
answer=input("You are at the end of a dirt road. Now which way you wanna go? Left or Right\n").lower()
if answer=="left":
    answer=input("You now have came to the river, you can choose how to cross it? swim or walk\n").lower()
    if answer=="swim":
        print("Oops you were eaten up by Aligator\n")
    elif answer=="walk":
        print("You walked for many miles and now you are dehydrated\n")
elif answer=="right":
    answer=input("You come to a bridge, do you want to cross it or head back? cross or back\n")
    if answer=="back":
       print("you go back ang and lost\n")
    elif answer=="cross":
        answer=input("You met a stranger after crossing, do you wanna talk? yes or no\n").lower()
        if answer=="yes":
            print("Stranger offered help and now you got the lift, you Won! \n")
        elif answer=="no":
            print("Stranger did not like your behaviour and gave you mis direction, You Lost!\n")
        else:
            print("Not a valid option. You lose\n")
    else:
        print("nOt a valid option. You lose\n")   

else:
    print("Ente valid direction\n")