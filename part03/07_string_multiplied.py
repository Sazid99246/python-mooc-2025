s = input("Please type in a string: ")
n = int(input("Please type in an amount: "))

result = ""
while n > 0:
    result += s
    n -= 1
print(result)