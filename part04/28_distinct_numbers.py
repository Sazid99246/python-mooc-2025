def distinct_numbers(nums):
    res_list = []
    for i in nums:
        if i not in res_list:
            res_list.append(i)
    res_list.sort()
    return res_list


if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))  # [1, 2, 3]
