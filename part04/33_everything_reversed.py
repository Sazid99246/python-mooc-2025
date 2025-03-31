def everything_reversed(strs):
    result = []
    for s in strs:
        result.append(s[::-1])
    result.reverse()
    return result


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
