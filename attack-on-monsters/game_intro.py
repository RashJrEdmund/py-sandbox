from game_data import Characteristics, GameCharacter, EnemyMap, WeaponMap
from utils import validateInput, printBoxedMsg

def onBoardUser():
    printBoxedMsg("ATTACK ON MONSTERS", 1) # 1 is the number of lines

    print("Hello adventurer!, welcome to my mini-game. \nWelcome to 'ATTACK ON MONSTERS'\n\n")

    print("In this game, you'll create your avatar, set out on a quest and get attacked by monsters, you will have to fight back too. \n")

    print("First, let's create you an avatar. fill the data below to get started\n")

    name = input("Name your avatar: \n")

    health = validateInput("health", f"\nGive {name} and initial health between 20 and 100: \n", 20, 100)

    shield = validateInput("shield", f"\nGive {name} a shield strength between 0 and 50: \n", 0, 50)

    print(f"\nTime to mod {name}'s weapon\n")

    useCustomWeapon = True if (input("Enter 'C' to use a custom weapon, or hit any key to select from our inventory\n").upper() == "C") else False

    weapon = {}

    if (useCustomWeapon):
        weaponName = input(f"What weapon should {name} use: \n")

        weaponDamage = validateInput("weapon damage", "\nSet weapon damage. Damage is within 10 to 45 \n", 10, 45)
        weapon = { "name": weaponName, "damage": weaponDamage }
    else:
        print("Press the numbers in braces '[]' to make selection\n")

        baseMsg = "Inventory: \n"

        for i in range(1, 7):
            baseMsg += f"[{i}] - {WeaponMap[i]['name']}\n"

        baseMsg += "\nSelect tool "
        
        weapon_id = validateInput("Weapon", baseMsg, 1, 6)

        weapon = WeaponMap[weapon_id]


    avatarXtics = Characteristics(name, "Human", health, weapon, shield)

    print("press the number in brackets ([]) to choose your enemy\n")

    enemyBaseMsg = "What Enemy would you want to fight against\n"

    EnemyCollection = ("Orgs", "Cyborgs", "Dragons", "Aliens") # using this instead of EnemyMap since I had difficulties reference the properties I need

    for i in range(len(EnemyCollection)):
        enemyBaseMsg += f"[{i + 1}] - {EnemyCollection[i]}\n"

    enemyBaseMsg += "\nSelect and enemy "

    enemy_id = validateInput("", enemyBaseMsg, 1, 4)

    return {
            "enemy": GameCharacter(EnemyMap[enemy_id]),
            "avatar": GameCharacter(avatarXtics), # returning a newly created avatar for the user.
           }
