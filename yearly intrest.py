


annual_rate = 7.0 #annual 
balance = 100 #usd
year = 1 #current year



while year <=50:
    intrest = balance * (annual_rate / 100)

    balance = balance + intrest
    year = year + 1

formatted = "{:.2f}".format(balance)
print("After 50 year you wull have", formatted)

