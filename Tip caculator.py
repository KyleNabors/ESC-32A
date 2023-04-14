
amount = float(input("Total amount of bill:"))

tip_pct = float(input("tip percent %"))

tip = amount * (tip_pct / 100)

pct_str = "{:.0f}%".format(tip_pct)

tip_str = "${:.2f}".format(tip)

print("percemt","Tip", pct_str, "tip would be", tip_str)
print(pct_str, tip_str, sep="\t")
