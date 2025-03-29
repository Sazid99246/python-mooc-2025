# Write your solution here
def line(n, text):
    if len(text) == 0:
        print(n * "*")
    else:
        print(text[0] * n)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")