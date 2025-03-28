n = int(input("Please type in a number: "))
i = 1
j = 1

while i <= n:
    while j <= n:
        print(f"{i} x {j} = {i * j}")
        j += 1
    j = 1
    i += 1
