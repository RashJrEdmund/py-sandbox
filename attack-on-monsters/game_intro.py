print("IN game intro")

def validateInput(stat, baseMsg, leastVal, highestVal):
    tries = 0

    data = int(input(baseMsg))

    if (data < leastVal or data > highestVal):
        newMsg = f"\n{stat} must a value between {leastVal} and {highestVal}, please try again\n"
        validateInput(stat, newMsg, leastVal, highestVal);
    else:
        return data

def onBoardUser():
    print("Hello adventurer!, welcome to my mini-game. \nWelcome to 'ATTACK ON THE MONTERS'\n\n")

    print("In this game, you'll create your avatar, set out on a quest and get attacked by monsters, you will have to fight back too. \n")

    print("First, let's create you an avatar. fill the data below to get started\n")

    name = input("Name your avatar: \n")

    health = validateInput("health", f"\nGive {name} and initial health between 20 and 100: \n", 20, 100)

    shield = validateInput("shield", f"\nGive {name} a shield strength between 0 and 50: \n", 0, 50)

    print(f"\nTime to mod {name}'s weapon\n")

    weaponName = input("Name his weapon: \n")

    weaponDamage = validateInput("weapon damage", "\nSet weapon damage. Damage is within 10 to 45 \n", 10, 45)

    print("Step Completed\n")

    print(name, health, shield, weaponName, weaponDamage)

