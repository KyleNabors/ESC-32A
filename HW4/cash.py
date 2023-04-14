#cash.py

#Kyle Nabors

#Takes a file from user and gives the number of items and what the total cost is

#Global Variables
item_count = 0
running_sum = 0
print("Cash register")

filename= input("Enter file of prices:")#ask user for file name

infile = open(filename)#open file

for line in infile:
    line = line.strip()#get rid of all blank space in line
    item_count = item_count + 1 #Count number of items
    line.strip("$")#get rid of the $ from the price 
    running_sum = float(line) + running_sum#sum the dollar amount for the items 

formatted_str = "${:.2f}".format(running_sum)#formats the output to standard dollars
print("File contained", item_count, "items totaling", formatted_str)#tell user how many items and how much
