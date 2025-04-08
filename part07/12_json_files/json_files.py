import json


def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()

    persons = json.loads(data)
    for person in persons:
        person_name = person["name"]
        person_age = str(person["age"])
        person_hobbies = '(' + ', '.join(person['hobbies']) + ')'
        print(f"{person_name} {person_age} years {person_hobbies}")


if __name__ == "__main__":
    print_persons("file1.json")
