# statistics.py
# Kristian Stevens
#
# Calculate descriptive statistics from user entered values

# The number of values seen so far
running_count = 0

# The sum or total of values seen so far
running_sum = 0 

# minimum and maximum values seen so far
# None marks the variable empty and indicates no value seen yet
running_min = None 
running_max = None 

#Obtain filename from user
filename = input("Enter file name")

#Open the file
infile = open(filename,"r")




# Loop obtaining numbers from the user until
# they enter 'done' at the prompt
for numstr in infile:
    numstr = numstr.strip()
    
    # get user input
    # valid inputs are a number or 'done'
    in_str = input("Enter a number or 'done' to finish:")
    
    # gest to determine if we should stop the loop
    if in_str == 'done':
        break
    # convert input to float
    numstr = float(numstr)

    # increment running count
    running_count = running_count + 1

    # increment running sum
    running_sum = running_sum + in_num

    # update running max
    if running_max == None:
        running_max = in_num
    elif in_num > running_max:
        running_max = in_num

    # update running min
    # simplified using single condition with a guardian pattern
    if running_min == None or in_num < running_min:
        running_min = in_num

# Output descriptive statistics
print("Count:", running_count)
print("Sum:",running_sum)
print("Min:",running_min)
print("Max:",running_max)
# Only compute average for non-zero count
if running_count > 0:
    print("Average:", running_sum/running_count)

    
