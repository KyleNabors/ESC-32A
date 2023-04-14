#cat.py

#Kyle Nabors

#prints the text of the file given by user

#Global Variables

filename=input("Enter a file name to open:")#ask user for file

infile = open(filename)#open file

for line in infile:
    line = line.strip()#get rid of blank space in line
    print(line)
