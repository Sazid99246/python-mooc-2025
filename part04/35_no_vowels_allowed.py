def no_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    word = ""
    for i in s:
        if i in vowels:
            i = ""
        word += i
    return word


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
