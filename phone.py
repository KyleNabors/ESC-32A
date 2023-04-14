#Phone.py

#Kyle Nabors

#Gets phone number from user and checks if it is in the right format

#global variables
length = 0
digit = 0
special = 0

number = input("Enter number as  ###-###-####:")#gets input from user

length = len(number)#gets the length of the number to know for step one of checking input

if length == 12:#checks if the number is the correct legnth of the user input 
    for letter in number:
        if letter.isdigit():#checks how many numbers are in the phone number
            digit = digit + 1
        if letter in '-': #checks how many "-" are in the phone number
            special = special + 1
    if digit == 10: #checks if the number of digits is correct for a valid phonenumber
        if special == 2:#checks if the number of "-" is correct for a valid phone number
            print("Valid")
        else:
           print("Invalid") 
    else:
        print("Invalid")
else:
    print("Invalid")
        
