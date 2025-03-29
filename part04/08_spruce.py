# Write your solution here
def line(n, text):
    if len(text) == 0:
        print(n * "*")
    else:
        print(text[0] * n)


def spruce(n):
    print("a spruce!")
    star_count = 1
    space_count = n - 1
    for i in range(n):
        print(space_count * " ", end="")
        line(star_count, "*")
        star_count += 2
        space_count -= 1
    print(" " * (n - 1), end="")
    line(1, "*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
