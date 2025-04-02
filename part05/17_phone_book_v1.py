phone_book = {}

while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))

    if command == 3:
        print("quitting...")
        break
    elif command == 2:
        name = input("Name: ")
        number = input("Number: ")

        phone_book[name] = number
        print("ok!")
    else:
        name = input("Name: ")

        if name in phone_book.keys():
            print(phone_book[name])
        else:
            print("no number")
