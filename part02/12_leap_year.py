y = int(input("Please type in a year"))
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print("That year is a leap year.")
        else:
            print("That year is not a leap year.")
    else:
        print("That year is a leap year.")
else:
    print("That year is not a leap year.")
