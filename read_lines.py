#read_nums.py

filename = input("Enter File Name")

infile = open(filename, "r")

#loop over each line of the input file
for line in infile:
    line = line.strip()
    print(line)
