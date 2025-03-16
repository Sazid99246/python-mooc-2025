student_count = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

groups = int(student_count / group_size)
if student_count % group_size == 0:
    print("Number of groups formed:", groups)
else:
    print("Number of groups formed:", groups + 1)