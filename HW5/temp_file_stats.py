#temp_file_stats.py

#Kyle Nabors

#Takes the temps from the SacramentoTemps.csv file and finds the min and max temps 

#Global Variables
min_temp = None
max_temp = None
min_date = None
max_date = None

file = input("Temperature anomaly filename:")#gets file from user 

infile = open(file)#Opens the file so the program can manipulate it 

infile.readline()#Skips the first line of the program so the header dosent include the header 

for line in infile: #loops for the number of lines in the file
    line = line.strip()#removes all blank space from the lines
    line = line.strip('0')#removes all end zeros from the dates and temps 
    if line[-1] == '.':#checks if the value was a partical and adds back in the zero if it was 
        line = line + str(0)
    line = line.replace(',',' ')# replaces the comas in the file with just a black space 
    date, temp = line.split(' ')#Splits the two colums into there own colums
    temp = float(temp)
 
    if max_temp == None or temp > max_temp:#Checks if the temp is not filled yet or is higher than the max temp
        max_temp = temp#replaces max temp with temp if it was greater
        max_date = date#updates the year to match the temp 

    if min_temp == None or temp < min_temp:#Checks if the temp is not filled yet or is lower than the max temp
        min_temp = temp#replaces max temp with temp if it was lower
        min_date = date#updates the year to match the temp 
        
#print(line)
#prints the min and max temps and dates 
print("Min temp:", min_temp, "in", min_date)
print("Max temp:", max_temp, "in", max_date)
    

    
