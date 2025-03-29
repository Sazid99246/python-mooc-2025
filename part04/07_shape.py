# Copy here code of line function from previous exercise and use it in your solution
def line(n, text):
    if len(text) == 0:
        print(n * "*")
    else:
        print(text[0] * n)


def triangle(size, character):
    # You should call function line here with proper parameters
    for i in range(size + 1):
        line(i, character)


def shape(width, character, height, filler):
    triangle(width, character)

    for i in range(height):
        line(width, filler)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
