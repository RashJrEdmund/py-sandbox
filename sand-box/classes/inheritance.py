"""
    Inheritance in Python is similar to inheritances in other languages
"""

# BASIC-INHERITANCE:
class TestParent:
    def __init__(self):
        print("Parent inherited")

    def sayHello(self):
        print("Hello man!!")

class TestChild(TestParent):
    def sayBye(self):
        print("Bye man")

child = TestChild()

child.sayBye()

# INHERITANCE WITH ARGUMENTS
class Human:
    def __init__(self, health):
        self.health = health;

    def attack(self):
        print("Attacking")

class Warrior(Human):
    def __init__(self, health, defense):
        super().__init__(health) # calling the dunder __init__ method of the parent class with super()
        self.defense = defense

class Barbarian(Human):
    def __init__(self, health, damage):
        super().__init__(health)
        self.damage  = damage

warrior = Warrior(90, 50)
warrior.attack()

barbarian = Barbarian(100, 70)

print("Warrior health", warrior.health)
print("Barbarian Damage", barbarian.damage)
