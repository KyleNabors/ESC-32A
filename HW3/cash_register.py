#cash_register.py

#Kyle Nabors

#program adds up everything you bought and how much it costs

#Global variables
running_count = 0
running_sum = 0


print("Cash register")

while True:
    item = input("Enter the price of an item:")
    if item == '': #checks if there was an imput
        break
#updates all of the counters about how much has been bought and how much it costs
    item_num = float(item)
    running_count = running_count + 1
    running_sum = running_sum + item_num


formatted_str = "${:.2f}".format(running_sum)#formats the output to standard dollars
#Outputs the item number and total cost
print("You entered", running_count, "items totaling",formatted_str)

