# starbucks_menu.py
# Kristian Stevens
#
# Determine the item with the min carbs and max calories from the
# Starbucks menu in TSV format

# These variables keep track of
# items with the min carbs and max calories
running_min = None
min_item = None
running_max = None 
max_item = None

# Open the menu
# There are three values on each line of the menu
# item, calories, and carbohydrates
# They are separated by the tab character
filename = "Starbucks.txt"
infile = open(filename, "r")

# ignore the first line
# which describes the columns
infile.readline()

# Loop obtaining lines from the file
for line in infile:

    # strip the whitespace
    line = line.strip()

    # split into item, cals, and arbs
    item, cals, carbs = line.split("\t")

    # convert cals and carbs to integers
    cals = int(cals)
    carbs = int(carbs)

    # update running max and the item corresponding to the max
    if running_max == None or cals > running_max:
        running_max = cals
        max_item = item

    # update running min and the item corresponding to the min
    # simplified using single condition with a guardian pattern
    if running_min == None or carbs < running_min:
        running_min = carbs
        min_item = item

# Output items
print("Minimum carbs:", min_item, running_min)
print("Maximum calories:", max_item, running_max)


    
