items = []

while True:
    n = int(input("New item: "))
    if n == 0:
        print("Bye!")
        break
    items.append(n)
    print(f"The list now: {items}")
    print(f"The list in order: {sorted(items)}")
