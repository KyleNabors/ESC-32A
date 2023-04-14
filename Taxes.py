#Taxes.py

#caculate income tax

RATE1 = .10 #Lower tax bracket
RATE2 = .25 #Tax rate for higher tax bracket
RATE1_SINGLE_LIMIT = 32000 #Threhold for higher bracket
RATE1_MARRIED_LIMIT = 64000

#Get income
income = float(input("Enter Income"))
#Get marital status
marital_status = input("Please enter s for single, m for married:")

#Tax paid in low bracket
tax1 = 0
#Tax paid in high bracket
tax2 = 0


#Compute taxes
if marital_status == "s":
    #single taxes
    if income <= RATE1_SINGLE_LIMIT:
        tax1 = RATE1 * income
    else:
        tax1 = RATE1 * RATE1_SINGLE_LIMIT
        tax2 = RATE2 * (income - RATE1_SIGNLE_LIMIT)
else:
#married taxes
    if income<= RATE1_MARRIES_LIMIT:
        tax1 = RATE1 * RATE1_MARRIED_LIMIT
        tax2 = RATE2 * (income - RATE1_MARRIED_LIMIT)

total_tax = tax1 + tax2
print(total_tax)

