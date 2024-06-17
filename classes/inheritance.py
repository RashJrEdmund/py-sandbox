"""
    Inheritance in Python is similar to inheritances in other langauges
"""

# BASIC-INHERITANCE:
class Human:
    def __init__(self, health):
        self.health = health;

    def attack(self):
        print("Attacking")

class Warrior(Human):
    def __init_(self, health, defence):
        super().__init_(health) # calling the dunder __init__ method of the parent class with Super()
        self.defence = defence

class Barbarian(Human):
    def __init__(self, health, damage):
        super().__init__(health)
        self.damage  = damage

warrior = Warrior(90, 50)
warrior.attack();

print("Warrior health", warrior.health)
