from game_intro import onBoardUser

userResponse = onBoardUser()

print("\n-----------------------", "\n| Get Ready To Battle |", "\n-----------------------")

avatar = userResponse["avatar"]

enemy = userResponse["enemy"]

avatar.printStats()

print("\n\n________VS________")

enemy.printStats()
