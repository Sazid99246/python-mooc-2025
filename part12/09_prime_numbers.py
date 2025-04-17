def is_prime(number: int):
    if number < 2:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
                break
    return True


def prime_numbers():
    number = 0
    while True:
        if is_prime(number):
            yield number
            number += 1


if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))
