n = int(input("Please type in a number: "))

i = 1

while i <= n:
    if i == n:
        print(n)
    else:
        print(i)
        print(n)
    i += 1
    n -= 1
