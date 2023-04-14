#tip.py

#Kyle Nabors

#caculates tip from 15% to 25%

#gets user input
bill = float(input("Enter total bill:"))
i= 15 #the percent for the bill to be multiplied and for the loop to track

while i <= 25:
    tip= bill * (i / 100) #caculates tip
    #formats all the needed variables so they can be printed properly to user 
    formatted_str_1 = "${:.2f}".format(tip)
    percent = i
    formatted_str_2 = "{:.0f}%".format(percent)
    print(formatted_str_2, "is", formatted_str_1)
    i = i + 1 # updates percent 
