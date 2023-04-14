#moving_ave_csv.py

#Kyle Nabors

#Writes the moving average temp and year to a csv file

#Global Variables
min_temp = None
max_temp = None
min_date = None
max_date = None
line_count = 0
line_count2 = 0
temp_list = []
year = 0
ave = None
outfile = open("MovingAve.csv", "w")#creates the csv file to write to 
file = input("Temperature anomaly filename:")#gets the csv file from user
k = input("Enter window size:")#gets the year window from user
outfile.write("Year,Value\n")#writes the header for the new file

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
    
for line2 in range(k, len(temp_list) - k):#loops for the legnth of the temp list minus the number given for years
    if line_count2 == 0:#checks if it is the first line and if it is skips the header and adds to a counter to update for next loop
        temp_list.append(float(line[1]))
        line_count2 = line_count2 + 1
    ave = sum(temp_list[line2 - k:line2+k+1]) / (2*k+1)     
    year = 1880 + line2#adds the given number for years to the bace year
    outfile.write(str(year)+','+str( "{:.4f}\n".format(ave)))#writes the year and temp average to a .csv file
    #print(str(year)+','+str( "{:.4f}".format(ave)))

#print(line)  
#print("Min temp:", min_temp, "in", min_date)
#print("Max temp:", max_temp, "in", max_date)
#print(temp_list)
#print(str(year)+','+str( "{:.4f}".format(ave)))
##close both files 
infile.close()
outfile.close()
