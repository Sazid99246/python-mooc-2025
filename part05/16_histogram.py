def histogram(string):
    letter_counts = {}
    for s in string:
        if s not in letter_counts:
            letter_counts[s] = 1
        else:
            letter_counts[s] += 1

    s = ""

    for i in letter_counts:
        print(i, letter_counts[i] * "*")


if __name__ == "__main__":
    histogram("statistically")
