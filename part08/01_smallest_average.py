def student_avg_result(person: dict):
    return (person["result1"] + person["result2"] + person["result3"]) / 3


def smallest_average(person1: dict, person2: dict, person3: dict):
    person1_avg_result = student_avg_result(person1)
    person2_avg_result = student_avg_result(person2)
    person3_avg_result = student_avg_result(person3)
    min_average_result = min(
        person1_avg_result, person2_avg_result, person3_avg_result)
    if min_average_result == person1_avg_result:
        return person1
    elif min_average_result == person2_avg_result:
        return person2
    else:
        return person3


if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
    print(smallest_average(person1, person2, person3))
