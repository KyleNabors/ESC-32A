

montly_savings = float(input("Monthly savings:"))
annual_rate = float(input("Annual intrest rate:"))
monthly_rate = annual_rate/12
balance = 0 #usd
month = 1 #current year



while balance < 1000000:
    intrest = balance * (monthly_rate / 100)

    balance = balance + intrest + monthly-savings
    month = month + 1 

formatted = "{:.2f}".format(balance)
print("After", month // 12, "year you wull have", formatted)

