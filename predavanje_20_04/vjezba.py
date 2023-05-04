class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person's name is {self.name} and his age is {self.age}"


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Age: {self.age}"


person = Person("Ratkec", 25)
employee = Employee("glupan", 25, 123454)

print(person, employee)
