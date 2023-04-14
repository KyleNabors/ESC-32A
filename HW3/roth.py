#roth.py

#Kyle Nabors

#Caculates how many months it takes to double an investment

#Global variables
balance = float(input("Enter an initial Roth IRA deposit amount:"))
apr = float(input("Enter an annual percent rate of return:"))
goal = balance * 2 
month_count = 0

while balance < goal:
    #caculates how much intrest was gained in one month
    intrest = (balance * (apr / 100) / 12)
    balance = balance + intrest #adds to total 
    month_count = month_count + 1
    #tells user the value after each month
    print("Value after month", "{:.0f}:".format(month_count), "${:.2f}".format(balance))
#tells user final value
print("It will take", month_count, "months to double your investment with a", "{:.0f}%".format(apr), "return.")


