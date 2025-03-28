# Write your solution here
def hash_square(n):
    m = n
    while m > 0:
        print("#" * n)
        m -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)
