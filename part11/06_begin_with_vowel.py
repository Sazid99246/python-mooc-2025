def begin_with_vowel(words: list):
    return [word for word in words if word.lower()[0] in ["a", "e", "i", "o", "u"]]


if __name__ == "__main__":
    word_list = ["automobile", "motorbike",
                 "Animal", "cat", "Dog", "APPLE", "orange"]
    for vowelled in begin_with_vowel(word_list):
        print(vowelled)
