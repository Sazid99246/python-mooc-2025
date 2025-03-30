def all_the_longest(strs):
    longest = 0
    result_list = []

    for i in strs:
        if len(i) > longest:
            longest = len(i)

    for i in strs:
        if len(i) == longest:
            result_list.append(i)

    return result_list


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)
    print(result)  # ['eleventh']
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result)  # ['dorothy', 'richard']
