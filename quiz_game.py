# Welcome to my short colour quiz code, it will ask bunch of colour quiz and based on
#user response evaluate the final score

print("Welcome to my colour quiz! ")

playing = input("Do you want to play? ")

if playing.lower() !="yes":
    quit()

print("Okay! Lets play")
score=0

answer=input("what is the colour of Apple? ")
if answer.lower() =="red":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("what is the colour of Sky? ")
if answer.lower() =="blue":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("what is the colour of Trees? ")
if answer.lower() =="green":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("what is the colour of Banana? ")
if answer.lower() =="yellow":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("what is the colour of Sunset? ")
if answer.lower() =="orange":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("Here is your score "+str(score))