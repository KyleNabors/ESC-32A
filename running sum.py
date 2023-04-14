

running_sum = 0
while True:
    user_input = input("Enter a # or done")
    if user_input == "done":
        break
    try:
        num = float(user_input)
    except:
        exit()
    running_sum = running_sum + num

print("sum", running_sum)
