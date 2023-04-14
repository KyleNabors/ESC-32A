#looping greeter

num_friends = 0
while True:
    name = input("Name of a friend to greet:")
    if name =="":
        print ("beg your pardon?")
    print("Hello", name)
    num_friends = num_friends + 1
    ans = input("Greet another friend? y/n")

    if ans != "y":
        break
print(num_friends, "friends greeted")
