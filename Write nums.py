#write_nums

import random

num_lines = int(input("how many numbers?"))
largest = float(input("Largest number?"))
filename = input("Output file name:")

outfile = open(filename, "w")
for i in range(num_lines):


    n = random.random()

    n = n * largest
    
    line = "{:.4f}".format(n) + "\n"

    outfile.write(line)

outfile.close()
