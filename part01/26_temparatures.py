fahrenheit = int(input("Please type in a temperature (F): "))
celsius = (fahrenheit - 32) * 5 / 9

print(fahrenheit, "degrees Fahrenheit equals", celsius, "degrees Celsius")
if celsius < 0:
    print("Brr! It's cold in here!")