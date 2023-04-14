#trycat.py

#Kyle Nabors

#prints out the lines of any text file given 

#Global Variables

filename= input("Enter a file name to open:")#ask user for file

file_test = filename[-4:]#gets the extention for the filename

while file_test != ".txt":#checks if extention is a text file
    print("Could not open", filename)
    filename= input("Enter a file name to open:")
    file_test = filename[-4:]

infile = open(filename)
for line in infile:
    line = line.strip()#gets rid of blank space in lines
    print(line)

