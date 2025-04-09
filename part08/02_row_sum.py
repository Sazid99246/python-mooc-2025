def row_sums(my_matrix: list):
    for my_list in my_matrix:
        sum = 0
        for n in my_list:
            sum += n
        my_list.append(sum)


if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)
