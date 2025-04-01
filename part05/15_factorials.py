def factorial(n: int):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def factorials(n: int):
    result = {}
    for i in range(1, n + 1):
        result[i] = factorial(i)
    return result


if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
