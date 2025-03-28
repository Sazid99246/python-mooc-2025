while True:
    n = int(input("Please type in a number: "))
    m = n
    if n <= 0:
        print("Thanks and bye!")
        break
    else:
        fact = 1
        while m > 0:
            fact *= m
            m -= 1
        print(f"The factorial of the number {n} is {fact}")
