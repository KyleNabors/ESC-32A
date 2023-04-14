running_count = 0
running_sum = 0
running_min = None
running_max = None

while True:
    in_str = input("Enter a # or done to finish:")
    if in_str == 'done':
        break
    in_num = float(in_str)
    
    running_count = running_count + 1
    running_sum = running_sum + in_num
    if running_max == None:
        running_max = in_str
    elif in_num > running_max:
        running_max = in_num

    if runnning_min == None or in_nu < running_min:
        running_min = in_num
    if in_num < running_min:
        running_min = in_num

print("Count", running_count)
print("sum", running_sum)
print("Max", running_max)
print("Min", running_min)
print("Average", running_sum / running_count)
