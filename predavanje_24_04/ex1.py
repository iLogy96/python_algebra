# 8.1
# 1. What is the difference between a local variable and an object’s attribute?
# Answer: Scope i lifetime je glavna razlika, lokalna varijabla je kreirana u scopeu metode i uništena nakon return statementa, dok kod objekta je atribut kreiran unutar klase i moze bit pozvan i editan u scopeu te klase.
# Tko kod ima referencu tog objekta, može editat takav atribut.
# 2.What method is called when the object is created?
# __init__, short for initialize (constructor method)


# 8.2.1
class Address:
    def __init__(self, number, street_name):
        self.number = number
        self.street_name = street_name


new_address = Address(125, "Maksimirska")


# 8.2.2
class Clock(object):
    def __init__(self, time):
        self.time = time

    def print_time(self):
        time = "6:30"
        print(self.time)


clock = Clock("5:30")
clock.print_time()
