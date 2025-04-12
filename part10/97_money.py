class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __get_money(self):
        return self.__euros + (self.__cents / 100)

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another):
        return self.__get_money() == another.__get_money()

    def __ne__(self, another):
        return self.__get_money() != another.__get_money()

    def __gt__(self, another):
        return self.__get_money() > another.__get_money()

    def __lt__(self, another):
        return self.__get_money() < another.__get_money()

    def __add__(self, another: 'Money'):
        total_euros = self.__euros + another.__euros
        total_cents = self.__cents + another.__cents
        total_euros += total_cents // 100
        total_cents = total_cents % 100
        return Money(total_euros, total_cents)

    def __sub__(self, another: 'Money'):
        if self.__get_money() < another.__get_money():
            raise ValueError("a negative result is not allowed")

        euro_diff = self.__euros - another.__euros
        if self.__cents >= another.__cents:
            cent_diff = self.__cents - another.__cents
        else:
            euro_diff -= 1
            cent_diff = self.__cents + 100 - another.__cents

        return Money(euro_diff, cent_diff)


if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)
    e3 = e1 + e2
    e4 = e1 - e2

    print(e1)  # 4.05 eur
    print(e2)  # 2.95 eur
    print(e3)  # 7.00 eur
    print(e4)  # 1.10 eur

    try:
        e5 = e2 - e1
    except ValueError as ve:
        print("Error:", ve)

    # Comparison tests
    e6 = Money(4, 5)
    print(e1 == e6)  # True
    print(e1 == e2)  # False
    print(e1 != e2)  # True
    print(e1 > e2)   # True
    print(e1 < e2)   # False

    # Attempt to cheat (should fail silently)
    # e1.__euros = 9999  # Won't affect actual values
    print(e1)  # Still prints original value
