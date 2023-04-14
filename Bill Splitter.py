#Split.py

#Split the bill evenly

#Get the amount of the bill
user_input = input("Total bill:")
#Total Contains the total cost
total=float(user_input)
#Get the num of people
user_input = input("Number of people:")
num_people = int(user_input)
#Split the bill by the num of people
share = total / num_people
#Output the result
print ("Each person owes", share)
