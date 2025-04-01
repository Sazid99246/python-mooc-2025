def double_items(nums):
    result_nums = []
    for num in nums:
        result_nums.append(num * 2)
    return result_nums    

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
