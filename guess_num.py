# guess_num.py
# ECS32A
#
# Number guessing game
import random
#keep track of games played
games = 0
score = 0


#loop game until pleyer enters q 
while True:
    # "Think" of a random number 1, 2 or 3 
    pick = random.randint(1,3)
    print("I'm thinking of a number between 1 and 3.")

    # Ask the question and get the input
    guess = input("Enter your guess or 'q' to quit:")
    #exit loop if user enters q 
    if guess == 'q':
        break
    #convert guess to integer
    guess = int(guess)


    games = games + 1 
    # Check the answer
    if guess == pick:
        print("You're right!")
        score = score + 1 
    elif guess < pick:
        print("Too low!")
    else:
        print("Too high!")

    # Print the number the computer was thinking of   
    print("I was thinking of "+ str(pick) + ".")
print(score)
print(gmaes)
