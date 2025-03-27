s = input("Please type in a string: ")
chars_left = 20 - len(s)
s = chars_left * "*" + s
print(s)
