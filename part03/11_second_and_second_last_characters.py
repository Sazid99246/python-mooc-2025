s = input("Please type in a string: ")
second_character = s[1]
last_second_character = s[-2]

if second_character == last_second_character:
    print("The second and the second to last characters are", second_character)
else:
    print("The second and the second to last characters are different")
