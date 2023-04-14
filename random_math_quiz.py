# random_math_quiz.py
# ECS32A
#
# Simple math quiz with random quetions
import random

# This quiz has two operands
a = random.randint(1,10)
b = random.randint(1,10)
# The operator is chosen randomly
op = random.choice([" + "," - "," * "])
# Create a string containing the expression
expression = str(a) + op + str(b)
# Calculate the corresponding solution
solution = eval(expression)
# Ask the question and get the input
ans = input("What is " + expression + "?")
# Determine if the answer is correct
if solution == int(ans):
    print("Correct!")
else:
    print("Incorrect.")
