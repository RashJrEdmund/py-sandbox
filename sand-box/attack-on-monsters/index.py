from game_intro import onBoardUser # named exports
from utils import printBoxedMsg
import start_game # default export hence default import

userResponse = onBoardUser()

printBoxedMsg("Get Ready To Battle", 2)

avatar = userResponse["avatar"]

enemy = userResponse["enemy"]

newGame = start_game.NewGame(avatar, enemy)

newGame.start()
