nums = []
n = 1
while True:
    print(f"The list is now {nums}")
    command = input("a(d)d, (r)emove or e(x)it: ")
    if command == "d":
        nums.append(n)
        n += 1
    elif command == "r":
        nums.pop()
        n -= 1
    else:
        print("Bye!")
        break
