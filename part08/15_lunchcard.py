class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def eat_lunch(self):
        if self.balance - 2.60 > 0:
            self.balance -= 2.60

    def eat_special(self):
        if self.balance - 4.60 > 0:
            self.balance -= 4.60

    def deposit_money(self, amount):
        if amount < 0:
            raise ValueError(
                "You cannot deposit an amount of money less than zero")
        self.balance += amount

    def __str__(self):
        return f"The balance is {"{:.1f}".format(self.balance)} euros"


peter = LunchCard(20)
grace = LunchCard(30)

peter.eat_special()
grace.eat_lunch()

print("Peter:", peter)
print("Grace:", grace)

peter.deposit_money(20)
grace.eat_special()

print("Peter:", peter)
print("Grace:", grace)

peter.eat_lunch()
peter.eat_lunch()

grace.deposit_money(50)

print("Peter:", peter)
print("Grace:", grace)
