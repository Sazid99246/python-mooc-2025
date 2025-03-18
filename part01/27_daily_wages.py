hourly_wages = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
day = input("Day of the week: ")

if day == "Sunday":
    hourly_wages *= 2

daily_wages = hourly_wages * hours_worked
print("Daily wages:", daily_wages, "euros")