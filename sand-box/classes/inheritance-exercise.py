#
# EXERCISE
#
"""
    [1] - Create a monster class where you can set a health and damage attribute on creation.

    [2] - It should also inherit from an entity class to get an attack method (That prints "attack" & the damage amount)

    [3] - Do some research so that when an instance of the class is printed it returns "a monster with {health} hp"
"""

# SOLUTION
class Entity:
    def __init__(self, damage):
        self.damage = damage

    def attack(self):
        print(f"The attack damage is {self.damage}")

class Monster(Entity): # [2] - COMPLETED
    def __init__(self, health, damage): # [1] - COMPLETED
        super().__init__(damage)
        self.health = health

    def __repr__(self): # [3] - COMPLETED   
        return f"a monster with {self.health} hp"


monster = Monster(80, 50)

monster.attack()

print(monster) # causes the dunder __repr__ method to execute and prints it's return value instead of just printing the default object form

#
# BETTER SOLUTION.
"""
    Instead of defining the __init__ method on the Entity class, and having more lines of code,
    we could, "since the class does nothing else but print the damage, just use assign the damage
    to self in the "Monster" class, and then reference it directly in the Entity class, since
    when the "Monster" class inherits from the "Entity" class, the "self" in the "Entity" class
    will reference the self in the "Monster" class"
"""
# BS_** // where BS stands for better-solution (to avoid naming conflicts)

class BS_Entity:
    def attack(self):
        print(f"The attack damage is {self.damage}")

class BS_Monster(BS_Entity):
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def __repr__(self):
        return f"a bs_monster with {self.health} hp"

bs_monster = BS_Monster(50, 90)

bs_monster.attack()

print(bs_monster)
