#parrot.py

#Kyle Nabors

#Program repeated input in all caps 

#global varriables

echo = input(">")#gets the inital input from user

echo = echo.lower()

while echo != "hush":#loops the input and echo comand until user says hush
    
    print(echo.upper())#outputs the users input in all caps
    echo = input(">")#gets the users input within the loops
    echo = echo.lower()
