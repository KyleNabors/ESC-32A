#first_ave.py

#Kyle Nabors

#finds the avarage temprature given a variable number of years 

#Global Variables
min_temp = None
max_temp = None
min_date = None
max_date = None
line_count = 0 
temp_list = []
year = 0
ave = None

file = input("Temperature anomaly filename:")#gets file from user 
k = input("Enter window size:")#gets the window of years from the user

year = 1880 + int(k)#adds the given number to the base year to get the year range
infile = open(file)#opens the file so the program can read it 

infile.readline()#skips the first line so the header dosent get used

for line in infile: #loops for the number of lines in the file
    line_count = line_count + 1 #Keeps up a count of the how many lines have been run 
    line = line.strip()#removes all blank space from the lines
    line = line.strip('0')#removes all end zeros from the dates and temps 

    if line[-1] == '.':#checks if the value was a partical and adds back in the zero if it was 
        line = line + str(0)

    line = line.replace(',',' ')# replaces the comas in the file with just a black space 
    date, temp = line.split(' ')#Splits the two colums into there own colums
    
    temp = float(temp)

    temp_list.append(temp)#adds the value from temp to the list 
 
    if max_temp == None or temp > max_temp:#Checks if the temp is not filled yet or is higher than the max temp
        max_temp = temp#replaces max temp with temp if it was greater
        max_date = date#updates the year to match the temp 

    if min_temp == None or temp < min_temp:#Checks if the temp is not filled yet or is lower than the max temp
        min_temp = temp#replaces max temp with temp if it was lower
        min_date = date#updates the year to match the temp 
    k = int(k)
    ave = sum(temp_list[0:k+k+1]) / (2*k+1) #finds the average value of the temprature using the given tempratures 
        
#print(line)
#prints the min and max temps and dates 
#print("Min temp:", min_temp, "in", min_date)
#print("Max temp:", max_temp, "in", max_date)
#print(temp_list)
print(str(year)+','+str( "{:.4f}".format(ave)))#prints out the year and the average in a nice to read format
