#pocket.py

#Kyle Nabors

#takes the change a person has and tells them how much it is worth

#Global variables
quarters = 0
dimes = 0
nickles = 0
pennies = 0
#gets user input for the coins
print("Pocket change calculator")
quarters = float(input("How many quarters?"))
dimes = float(input("How many dimes?"))
nickles = float(input("How many nickels?"))
pennies = float(input("How many pennies?"))
#turns coins into desimal change 
quarters_d = quarters * .25
dimes_d = dimes * .1
nickles_d = nickles * .05
pennies_d = pennies * .01
#adds them all together
money = quarters_d + dimes_d + nickles_d + pennies_d
#formats the change into standard cash format 
formatted_str = "${:.2f}".format(money)

print("You have", formatted_str)
