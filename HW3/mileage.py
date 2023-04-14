#mileage.py

#Kyle Nabors

#
#Global Variables
total_miles = 0
total_gas = 0

print("Your Personal Fuel Economy")
while True:
    miles_driven = 0
    gas_used = 0
    miles_driven = input("Number of miles traveled (or enter to exit):")
    if miles_driven == '':#checks if the user is finshed and ends the loop
        break
    gas_used = input("Number of gallons needed:")
    #caculates the mpg and prints it for the user
    print("Mileage this tank:", "{:.1f}".format(int(miles_driven) / int(gas_used)))
#updates total gas and miles for every loop run
    total_miles = total_miles + int(miles_driven)
    total_gas = total_gas + int(gas_used)
#caculates total mpg for the  overall and give it to user
print("Average mileage:", "{:.1f}".format(int(total_miles) / int(total_gas)))
