class NumberStats:
    def __init__(self):
        self.record = []

    def add_number(self, number: int):
        self.record.append(number)

    def count_numbers(self):
        return len(self.record)

    def get_sum(self):
        return sum(self.record) if len(self.record) > 0 else 0

    def average(self):
        if self.get_sum() == 0 or len(self.record) == 0:
            return 0
        return self.get_sum() / len(self.record)


print("Please type in integer numbers:")
all_numbers = NumberStats()
even_numbers = NumberStats()
odd_numbers = NumberStats()

while True:
    n = int(input())
    if n == -1:
        print(f"Sum of numbers: {all_numbers.get_sum()}")
        print(f"Mean of numbers: {all_numbers.average()}")
        print(f"Sum of even numbers: {even_numbers.get_sum()}")
        print(f"Sum of odd numbers: {odd_numbers.get_sum()}")
        break
    if n % 2 == 0:
        even_numbers.add_number(n)
    if n % 2 != 0:
        odd_numbers.add_number(n)
    all_numbers.add_number(n)
