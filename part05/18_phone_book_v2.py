phone_book = {}

while True:

    command = int(input("command (1 search, 2 add, 3 quit): "))

    if command == 3:
        print("quitting...")
        break
    elif command == 2:
        name = input("Name: ")
        number = input("Number: ")
        if name in phone_book.keys():
            phone_book[name].append(number)
        else:
            phone_book[name] = []
            phone_book[name].append(number)
        print("ok!")
    else:
        name = input("Name: ")

        if name in phone_book.keys():
            numbers = phone_book[name]
            for number in numbers:
                print(number)
        else:
            print("no number")
