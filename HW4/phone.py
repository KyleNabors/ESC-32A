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
    if number[:2].isdigit(): #checks if first 3 characters are digits
        if number[3] is '-': #checks if 4th character is a -
            if number[4-6].isdigit():#checks if 5-7 characters are digits 
                if number[7] is '-': #checks if 8th character is a -
                    if number[8:].isdigit(): #checks if 9-12 characters are digits 
                        print("Valid")
                    else:
                        print("Invalid")
                else:
                    print("Invalid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")
        
