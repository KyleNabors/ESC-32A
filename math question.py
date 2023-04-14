# math_question.py


#ask math question

#Operands
a = 5
b = 4



expression = str(a) + " * " + str(b)
solution = a * b

ans = input("What is" + expression + "?")

#Check user input to see if answer is correct
if ans == str(solution):
    print("Correct!")

else:
    print("Incorrect")
    print("The correct solution is", solution)
