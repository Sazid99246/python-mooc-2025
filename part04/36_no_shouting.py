def no_shouting(strs):
    result = []
    for s in strs:
        if s.isupper():
            continue
        result.append(s)
    return result


if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER",
               "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
