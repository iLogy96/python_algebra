# Zad 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Age: {self.age}"


class Evidency:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def remove_person(self, person):
        if person in self.people:
            self.people.remove(person)

    def edit_person(self, person, new_name, new_age):
        if person in self.people:
            person.name = new_name
            person.age = new_age

    def list_people(self):
        for person in self.people:
            print(person)


# Zad 2
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels


class WorkMachine(Vehicle):
    def __init__(self, make, model, year, weight_capacity):
        super().__init__(make, model, year)
        self.weight_capacity = weight_capacity
