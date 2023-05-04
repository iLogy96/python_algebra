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
        print("Person added successfully.")

    def remove_person(self, person):
        if person in self.people:
            self.people.remove(person)
            print("Person removed successfully.")
        else:
            print("Person not found in evidence.")

    def edit_person(self, person, new_name, new_age):
        if person in self.people:
            person.name = new_name
            person.age = new_age
            print("Person edited successfully.")
        else:
            print("Person not found in evidence.")

    def list_people(self):
        if len(self.people) == 0:
            print("No people in evidence.")
        else:
            for person in self.people:
                print(person)


# Create an evidency collection
evidency = Evidency()

# Main menu loop
while True:
    print("\nWhat would you like to do?")
    print("1. Add a person")
    print("2. Remove a person")
    print("3. Edit a person")
    print("4. List all people")
    print("5. Exit")

    # Get user input for menu selection
    choice = input("Enter a number: ")

    if choice == "1":
        # Get user input for new person details
        name = input("Enter the person's name: ")
        age = int(input("Enter the person's age: "))
        employee_choice = input("Is this person an employee? (y/n): ")
        if employee_choice.lower() == "y":
            employee_id = input("Enter the employee's ID: ")
            person = Employee(name, age, employee_id)
        else:
            person = Person(name, age)

        # Add the new person to the evidency
        evidency.add_person(person)

    elif choice == "2":
        # Get user input for person to remove
        name = input("Enter the person's name: ")
        age = int(input("Enter the person's age: "))
        person = None
        for p in evidency.people:
            if p.name == name and p.age == age:
                person = p
                break
        if person:
            evidency.remove_person(person)
        else:
            print("Person not found in evidence.")

    elif choice == "3":
        # Get user input for person to edit
        name = input("Enter the person's name: ")
        age = int(input("Enter the person's age: "))
        person = None
        for p in evidency.people:
            if p.name == name and p.age == age:
                person = p
                break
        if person:
            new_name = input("Enter the person's new name: ")
            new_age = int(input("Enter the person's new age: "))
            evidency.edit_person(person, new_name, new_age)
        else:
            print("Person not found in evidence.")

    elif choice == "4":
        evidency.list_people()

    elif choice == "5":
        print("Thanks for using the app")
        break
