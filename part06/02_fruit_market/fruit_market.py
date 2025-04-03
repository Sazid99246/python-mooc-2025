def read_fruits():
    fruits_and_prices = {}

    with open("fruits.csv") as fruits:
        for fruit in fruits:
            fruit = fruit.replace("\n", "")
            fruit = fruit.split(";")
            fruits_and_prices[fruit[0]] = float(fruit[1])

    return fruits_and_prices


if __name__ == "__main__":
    print(read_fruits())
