while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    n = int(input("Function: "))
    if n == 0:
        print("Bye now!")
        break
    if n == 1:
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as diary:
            diary.write(entry + "\n")
            print("Diary saved")
    if n == 2:
        print("Entries:")
        with open("diary.txt") as diary:
            for line in diary:
                line = line.replace('\n', '')
                print(line)
