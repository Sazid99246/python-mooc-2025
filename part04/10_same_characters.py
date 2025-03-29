# Write your solution here
def same_chars(text, i1, i2):
    try:
        return text[i1] == text[i2]
    except IndexError:
        return False


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))
