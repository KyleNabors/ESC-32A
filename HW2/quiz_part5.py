#quiz_part2

#Kyle Nabors

#program asks a trivial prusuit quiz

#variables
answer = ""
score = 0

#askes the question 1 to the user
print("ART AND LITERATURE: Who painted Starry Night?")
print("a. Vincent van Gogh")
print("b. Michelangelo")
print("c. Leonardo da Vinci")

#user inputs answer to q1 
answer = input("Enter your choice:")

#check if answered correctly
if answer == "a":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was a")

#asks question 2 to user
print("ENTERTAINMENT: How many oscars did Alfred Hitchcock win?")
print("a. None")
print("b. One")
print("c. Two")

#user inputs answer to q2
answer = input("Enter your choice:")

#check if answered correctly
if answer == "a":
    print("Correct!")
    score = score + 1
    
else:
    print("The correct answer was a")

#ask question 3 to user
print("GEOGRAPHY: Which is the largest ocean?")
print("a. Pacific")
print("b. Atlantic")
print("c. Indian")

#user inputs answer to q3
answer = input("Enter your choice:")

#check if answered correctly
if answer == "a":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was a")

#ask question 4 to user
print("HISTORY: Who was the first U.S. president to appear on a coin?")
print("a. Washington")
print("b. Lincoln")
print("c. Jefferson")

#user inputs answer to question 4
answer = input("Enter your choice:")

#check if answered correctly
if answer == "b":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was b")

#Ask user question 5
print("SCIENCE AND NATURE: Can pigs swim?")
print("a. Yes")
print("b. No")
print("c. Only in salt water")

#user inputs answer for question 5
answer = input("Enter your choice:")

#check if answered correctly
if answer == "a":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was a")

#Asks user question 6
print("SPORT AND LEISURE: What color is the middle Olympic ring?")
print("a. Red") 
print("b. Blue")
print("c. Black")

#user inputs answer for question 6
answer = input("Enter your choice:")

#check if answered correctly
if answer == "c":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was c")
    
#Ask question 7
print("GENIUS: What is D divided by X?")

#user inputs answer for q7
answer = input("Enter your answer:")

#check if answered correctly
if answer == "L":
    print("Correct!")
    score = score + 1
elif answer == "50":
    print("Correct!")
    score = score + 1
else:
    print("Correct answers were L or 50")
    
#tell player final score
print("Your final score is", score)

#rate the users score and give them feedback
if score <= 2:
    print ("You were unlucky!")
elif score <= 4:
    print("You did better than chance!")
elif score <=6:
    print("You are a trivia star!")
else:
    print("Genius!")








