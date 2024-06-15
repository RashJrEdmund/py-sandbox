"""
    MY MINI GAME

    calling it, "ATTACK ON MONSTERS 😅"

    Here I'm defining everything about the game
"""

class Characteristics:
    def __init__(self, name, health, weapon, shield):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.shield = shield

class GameCharacter:
    def __init__(self, characteristics):
            self.name = characteristics.name
            self.health = characteristics.health
            self.weapon = characteristics.weapon
            self.shield = characteristics.shield

    def attack(self, target):
        newShieldStrength = target.shield - self.weapon["damage"]

        target.shield = 0 if (newShieldStrength <= 0) else newShieldStrength

        resultantAttack = abs(newShieldStrength) if (newShieldStrength < 0) else 0

        resultantHealth = target.health - resultantAttack if (resultantAttack > 0) else target.health

        target.health = 0 if (resultantHealth <= 0) else resultantHealth
    
    def printStats(self):
        print("\n\n", f"{self.name.upper()}'s STATS \n");
        print(f"name: {self.name} \nhealth: {self.health} \nshield: {self.shield} \nweaponName: {self.weapon['name']} \nweaponDamage: {self.weapon['damage']}")

        return self

## TESTING
"""
# My Avatar
avatarXtics = Characteristics("Rash", 100, { "name": "AK47", "damage": 30 }, 50)

myAvatar = GameCharacter(avatarXtics)

'''
    print(avatarXtics.weapon)
    myAvatar.printStats()
'''

# MONSTER
monsterXtics = Characteristics("Org", 200, { "name": "Axe", "damage": 50 }, 0)

org = GameCharacter(monsterXtics)

#
# GAME PLAY()
#
'''
    org.attack(myAvatar)
    org.attack(myAvatar)

    myAvatar.printStats()

    myAvatar.attack(org)

    org.printStats()
'''
"""