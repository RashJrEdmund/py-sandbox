"""
    MY MINI GAME

    calling it, "ATTACK ON MONSTERS 😅"

    Here I'm defining everything about the game
"""

class Characteristics:
    def __init__(self, name, specie, health, weapon, shield):
        self.name = name
        self.specie = specie
        self.health = health
        self.weapon = weapon
        self.shield = shield

    def getProperty(self, prpty):
        return self[prpty]

class GameCharacter:
    def __init__(self, characteristics):
            self.name = characteristics.name
            self.specie = characteristics.specie
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
        print("\n\n", f"{self.name.upper()}'s STATS \n")
        print(f"name: {self.name} ({self.specie}) \nhealth: {self.health} \nshield: {self.shield} \nweaponName: {self.weapon['name']} \nweaponDamage: {self.weapon['damage']}")

        return self

WeaponMap = {
            1: { "name": "Axe", "damage": 35 },
            2: { "name": "Barrett M82", "damage": 40 },
            3: { "name": "Laser emmitter", "damage": 45 },
            4: { "name": "M142 HIMARS (US rocket launcher)", "damage": 90 },
            5: { "name": "Challenger 2, (UK millitary Tank)", "damage": 200 },
            6: { "name": "Lockheed Martin F-22 Raptor (US Fighter Jet)", "damage": 300},
            7: { "name": "Fire and Claws", "damage": 110 },
            8: { "name": "Apocalypse", "damage": 999 }
        }

EnemyMap = {
            1: Characteristics("Mvtup", "Org", 120, WeaponMap[1], 50),
            2: Characteristics("Rage-p-13", "Cyborg", 130, WeaponMap[5], 50),
            3: Characteristics("Nanya", "Dragon", 160, WeaponMap[7], 70),
            4: Characteristics("Gibrish-Gibrish", "Alien", 50, WeaponMap[8], 1000),
        }

print(EnemyMap[1])

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
