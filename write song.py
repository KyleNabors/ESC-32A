#open the file
outfile = open("song.txt", "w")

#write a line of text to file and screen
line = "I'm a lumberjack and I'm OK"
print(line)
outfile.write(line+"\n")
            

line = "I sleep all night and I work all day"
print(line)
outfile.write(line+"\n")

#close file and flush data to hard drive
outfile.close()
