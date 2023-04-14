#password.py

#Kyle Nabors

#Test the password that the user chooses 

#Global Variables
legnth = 0
uppercase = 0
lowercase = 0
digit = 0
special = 0

password = input("Enter password:")#gets password from user

for letter in password:

    legnth = legnth + 1#keeps track of the lengh of the password

    if letter.isupper():# checks if there are any uppercasse letters in password and adds counts them 
        uppercase = uppercase + 1
        
    if letter.islower:
        lowercase = lowercase + 1# checks if there are any lowercasse letters in password and adds counts them
        
    if letter.isdigit():# checks if there are any digits in password and adds counts them
        digit = digit + 1

    if letter in '@#$*!':# checks if there are any special characters in password and adds counts them
        special = special + 1
#prints out the length of the password and if it has uppercase, lowercase, digits, or special characters.     
print("Length:", legnth)
if lowercase > 0:
    print("Has lower case")
if uppercase > 0:
    print("Has upper case")
if digit > 0:
    print("Has digit")
if special > 0:
    print("Has special")
