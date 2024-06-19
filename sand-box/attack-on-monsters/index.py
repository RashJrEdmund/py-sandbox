from game_intro import onBoardUser # named exports
from utils import printBoxedMsg
import start_game # default export

userResponse = onBoardUser()

printBoxedMsg("Get Ready To Battle", 2)

avatar = userResponse["avatar"]

enemy = userResponse["enemy"]

avatar.printStats()

print("\n\n________VS________")

enemy.printStats()

newGame = start_game.NewGame(avatar, enemy)

newGame.start()
