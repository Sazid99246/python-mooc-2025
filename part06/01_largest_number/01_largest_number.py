def largest():
    largest_number = 0

    with open("numbers.txt") as numbers:
        for number in numbers:
            number = int(number)
            if number > largest_number:
                largest_number = number

    return largest_number


if __name__ == "__main__":
    print(largest())
