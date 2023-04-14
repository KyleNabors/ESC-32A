#ticket.py

#Kyle Nabors

#Program takes persons age and tells them how much tickets will cost

#gets user input
age =int(input("Enter age:"))

#checks the age at each level to see how nuch to chager
if age <= int(3):
    print("Price: FREE")
elif age <= int(12):
    print("Price: $29.95")
elif age<=int(17):
    print("Price: $39.95")
elif age <= int(64):
    #asks if student and applies discount if so 
    student = input("College ID? (y/n)")
    if student == 'y':
        print("Price: $39.95")
    else:
        print("Price: $49.95")
#assumes user is over 65 and applies senior discount 
else:
    print("Price: $39.95")
