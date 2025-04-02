def create_tuple(x: int, y: int, z: int):
    
    first = min(x, min(y, z))
    second = max(x, max(y, z))
    third = x + y + z

    result = (first, second, third)

    return result


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
