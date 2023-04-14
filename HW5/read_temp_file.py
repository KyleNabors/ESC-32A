#read_temp_file.py

#Kyle Nabors

#Takes the SacramentoTemps.csv file and prints out the values 

#Global Variables
file = input("Temperature anomaly filename:")#gets file from user 

infile = open(file)#Opens the file so the program can manipulate it 

infile.readline()#Skips the first line of the program so the header dosent include the header 

for line in infile: #loops for the number of lines in the file
    line = line.strip() #removes all blank space from the lines
    line = line.strip('0')#removes all end zeros from the dates and temps 
    if line[-1] == '.': #checks if the value was a partical and adds back in the zero if it was 
        line = line + str(0)
    line = line.replace(',',' ')# replaces the comas in the file with just a black space 
 
    print(line)
