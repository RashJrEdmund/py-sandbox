# DUNDER METHODS.
"""
    These are special methods of a class that always start with a double under score
    and end with thesame.
    example:
    __init__ is run when an instance of the classs is created
    __len__ gets called when the instance is passed into the "len()" function
"""

class Employee:
    def __init__(self, role, salary):  # kinda almost like the constructor method in JS
        print("the mage class was created")
        self.role = role
        self.salary = salary

    def __len__(self):
        return self.salary

snrDev = Employee("Senior Front-end Developer", 8000); # the duncer __init__ functions immediately executes

print(len(snrDev)) # the __len__ method executes when our object instace is passed in a len function

