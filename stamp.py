#stamps.py
STAMP_PRICE = 55
#sim stamp vending machine
#Calculate num of tamps to vend

#Get dollars from user
dollars = int(input("Enter number of dollars"))

#Caculate the num of stamps
pennies = 100 * dollars
num_stamps = pennies // STAMP PRICE
#change = pennies - (stamps * STAMP_PRICE)
change = pennies % STAMP PRICE
#Output the result
print("First class stamps:",stamps)
print("Change:", change,"cents")
