items = []
items_count = int(input("How many items? "))

for i in range(items_count):
    n = int(input(f"Item {i + 1}: "))
    items.append(n)

print(items)
