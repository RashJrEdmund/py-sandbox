# DUNDER METHODS.
"""
    These are special methods of a class that always start with a double under score
    and end with the same.
    example:
    __init__ is run when an instance of the class is created, kinda like the Js constructor method
    __len__ gets called when the instance is passed into the "len()" function
    __repr__ gets called when the instance is passed into a print() function

    checkout more methods here
    https://www.geeksforgeeks.org/dunder-magic-methods-python/
"""

class Employee:
    def __init__(self, role, salary):  # kinda almost like the constructor method in JS
        print("the mage class was created")
        self.role = role
        self.salary = salary

    def __len__(self):
        return self.salary

snrDev = Employee("Senior Front-end Developer", 8000); # the dunder __init__ functions immediately executes

print(len(snrDev)) # the __len__ method executes when our object instance is passed in a len function
