import random
s = 1
while s == 1:
    n = random.randint(1,9)
    score = 0

    while True:
        score+=1
        x = int(input("Guess a number between 1 to 9:- "))
        if x<n:
            print("Your Number Is Smaller Then The Number")
        elif x>n:
            print("Your Number Is Greater Then The Number")
        else:
            print("You Guessed it Right, Congrats!")
            print("You Guessed It In", score," Times")
            break
            
    s = int(input("if you want to try again enter 1 else enter 0:- "))
