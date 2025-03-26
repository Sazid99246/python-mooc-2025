width = int(input("Width: "))
height = int(input("Height: "))

result = ""
for i in range(height):
    for j in range(width):
        result += "#"
    result += "\n"
print(result)