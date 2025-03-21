value = int(input("Value of gift: "))
tax = 0.0;
if value < 5000:
    print("No tax!")
elif value <= 25000:
    tax = 100 + (value - 5000) * 0.08
    print("Amount of tax:", tax, "euros")
elif value <= 55000:
    tax = 1700 + (value - 25000) * 0.1
    print("Amount of tax:", tax, "euros")
elif value <= 200000:
    tax = 4700 + (value - 55000) * 0.12
    print("Amount of tax:", tax, "euros")
elif value <= 1000000:
    tax = 22100 + (value - 200000) * 0.15
    print("Amount of tax:", tax, "euros")
else:
    tax = 142100 + (value - 1000000) * 0.17
    print("Amount of tax:", tax, "euros")