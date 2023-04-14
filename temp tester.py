#cel2eng.py

#Celsius to English converter

cel = float(input("Enter degrees Celsius:"))

#Freezing cold tem is 0 or below

if cel <= 0:
    print("Freezing cold")
#cold: below 10 degrees
elif cel < 10:
    print("Cold")
#cool: temp is below 15
elif cel < 15:
    print("Cool")
#nice temp is between 15 and 25
elif cel <= 25:
    print("Nice")
#super hot temp is above 35
elif cel > 35:
    print("Super hot")
#hot temp is above 30
elif cel > 30:
    print("Hot")
#warm temp is above 25
else:
    print("warm")
