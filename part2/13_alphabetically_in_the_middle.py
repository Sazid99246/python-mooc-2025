a = input("1st letter: ")
b = input("2nd letter: ")
c = input("3rd letter: ")

if (a > b and a < c) or (a > c and a < b):
    print("The letter in the middle is", a)
elif (b > a and b < c) or (b > c and b < a):
    print("The letter in the middle is", b)
else:
    print("The letter in the middle is", c)
