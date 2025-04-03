def matrix_sum():
    sum = 0
    with open("matrix.txt") as matrix:
        for i in matrix:
            i = i.replace("\n", "")
            i = i.split(",")
            for j in i:
                sum += int(j)
    return sum


def matrix_max():
    max = 0
    with open("matrix.txt") as matrix:
        for i in matrix:
            i = i.replace("\n", "")
            i = i.split(",")
            for j in i:
                if int(j) > max:
                    max = int(j)
    return max


def row_sums():
    sums = []
    with open("matrix.txt") as matrix:
        for i in matrix:
            sum = 0
            i = i.replace("\n", "")
            i = i.split(",")
            for j in i:
                sum += int(j)
            sums.append(sum)
    return sums


if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())
