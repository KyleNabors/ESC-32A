#Cash2.py

#Kyle Nabors

#Takes a file from user and gives the number of items and what the total cost is and ignores non dollar inputs

#Global Variables
item_count = 0
running_sum = 0

print("Cash register")

filename= input("Enter file of prices:")#ask user for filke

infile = open(filename)#open file

for line in infile:
    try:
        line = line.strip()#get rid of all blank space in line
        line = line.strip("$")#get rid of $ in price 
        running_sum = float(line) + running_sum #summing item price
        item_count = item_count + 1 #count to number of itemas
        
    except:
        pass

formatted_str = "${:.2f}".format(running_sum)#formats the output to standard dollars
print("File contained", item_count, "items totaling", formatted_str)#tells user how much and how many items
        
