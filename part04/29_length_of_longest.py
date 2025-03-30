def length_of_longest(strings):
    longest_length = 0
    for string in strings:
        if len(string) > longest_length:
            longest_length = len(string)
    return longest_length


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)
