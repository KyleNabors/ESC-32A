#tsv_to_csv.py


filename = input("Enter a TSV filename:")
infile = open(filename)
filename = input("Enter output CSV filename:")
outfile = open(filename,"w")

#loop over each line of the file
for line in infile:
    line = line.strip()
    line = line.replace("\t,",",")
    outfile.write(line + "\n")

infile.close()
outfile.close()
