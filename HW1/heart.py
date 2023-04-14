
age = int(input("Enter your age:"))


max_hr = 220 - age

target_hrl = max_hr * .5
target_hru = max_hr * .85


print("Your maximum heart rate is", max_hr, "bpm")
print("Your target heart rate is", target_hrl, "-", target_hru, "bpm")
