
import random


print("Waterfall animation")
input("Press enter to begin and ctrl + c to exit")

cursor = "|||||||||"
min_pos = 0
max_pos = 60
start_pos = max_pos // 2 
position = start_pos


while True:
    position = position + random.choice([1,-1])
    if position < min_pos:
        position = start_pos
    if position > max_pos:
        position = start_pos
    spaces = position * " " 
    line = spaces + cursor
    print(line)
