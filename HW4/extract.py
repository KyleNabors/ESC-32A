#extract.py

#Kyle Nabors

#extracts phone number from user input

#Global variables
number = input("Enter phone number:")#get phone number from user
newnum = str("")
number = number.strip()

for num in number:#loop for each number in the phone number 
    if num.isdigit():#check if the character is a number 
        newnum += num #if the character is a number add the number to the new number output

print(" Numbers:",newnum)
