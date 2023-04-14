#change.py

#Kyle Nabors

#divides change into coins


#Global variables
quarters = 0
dimes = 0 
nickels = 0 
pennies = 0

#inputs change in a form we can work with
change = float(input("Enter change:"))
#finds out how many quarters are given
quarters = change // 25
change = change % 25
#finds out how many dimes are given
dimes = change // 10
change = change % 10
#finds out how many nickels are given
nickels = change // 5
change = change % 5
#pennies are the remaining amount so just given the remainder as pennies 
pennies = change

print("Quarters:", int(quarters))
print("Dimes:", int(dimes))
print("Nickels:", int(nickels))
print("Pennies:", int(pennies))


