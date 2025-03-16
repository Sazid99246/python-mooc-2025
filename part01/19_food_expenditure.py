days = int(input("How many times a week do you eat at the student cafeteria? "))
daily_food_cost = float(input("The price of a typical student lunch? "))
weekly_food_cost = daily_food_cost * days
weekly_grocery_cost = float(input("How much money do you spend on groceries in a week? "))

total_cost = weekly_food_cost + weekly_grocery_cost;
cost_per_day = total_cost / 7

print("Average food expenditure:")
print("Daily:", cost_per_day, "euros")
print("Weekly:", total_cost, "euros")