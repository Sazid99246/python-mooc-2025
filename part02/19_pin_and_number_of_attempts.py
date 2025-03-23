count = 0

while True:
    pin = int(input("PIN: "))
    if pin != 4321:
        count += 1
        print("Wrong")
    else:
        count += 1
        if count == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {count} attempts")
        break
