class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0

    def shortest(self):
        if len(self.persons) == 0:
            return None
        shortest_person = self.persons[0]
        for person in self.persons:
            if person.height < shortest_person.height:
                shortest_person = person
        return shortest_person

    def remove_shortest(self):
        if len(self.persons) == 0:
            return None
        shortest_person = self.shortest()
        self.persons.remove(shortest_person)
        return shortest_person

    def print_contents(self):
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {sum(person.height for person in self.persons)} cm")
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")


if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
