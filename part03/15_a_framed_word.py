s = input("Word: ")
space_count = 30 - 2 - len(s)
left_space = round(space_count / 2)
right_space = space_count - left_space

print("*" * 30)
print("*", end="")
print(" " * left_space, end="")
print(s, end="")
print(" " * right_space, end="")
print("*")
print("*" * 30)
