#car.py

#Kyle Nabors

#User guesses the price of the car to win

#Global variables 
goal = 42500
guess_num = 0
print("Guess the price and win the prize!")

while True:
    guess = int(input("Enter your guess:")) #user guesses 
    guess_num = guess_num + 1
#check if the guess is too high, too low, or correct
    if guess > goal: 
        print("Too high!")
    elif guess < goal:
        print("Too low!")
    elif guess == goal:
        break
#Check of the guess is less than or equal to five to be within the guess limit
if guess_num <= 5:
    print("You won the car!")
else:
    print("Too many guesses!")    
