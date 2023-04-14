


annual_rate = 7.0 #annual
monthly_rate = annual_rate/12
balance = 100 #usd
month = 1 #current year



while month <=(50*12):
    intrest = balance * (monthly_rate / 100)

    balance = balance + intrest
    month = month + 1

formatted = "{:.2f}".format(balance)
print("After 50 year you wull have", formatted)

