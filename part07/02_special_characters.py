import string


def separate_characters(my_string: str):
    letters = ""
    punctuations = ""
    others = ""
    for s in my_string:
        if s in string.ascii_letters:
            letters += s
        elif s in string.punctuation:
            punctuations += s
        else:
            others += s
    return (letters, punctuations, others)


if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
