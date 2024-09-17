from utils import validateInput, printBoxedMsg;
from game_data import GameCharacter;

class NewGame:
    def __init__ (self, avatar: GameCharacter, enemy: GameCharacter, isFirstGamePlay = True):
        self.avatar = avatar
        self.enemy = enemy
        self.isFirstGamePlay = isFirstGamePlay

        self.inGamePrompts = [
                    (1, "strike enemy"),
                    (2, "take some damage"),
                    (3, "view avatar status"),
                    (4, "view enemy status"),
                    (5, "exit game"),
                ]

        self.gameOverPrompts = [
                    (5, "exit game"),
                    (6, "re-start game"),
                ]
    
    def start(self):
        self.avatar.printStats()

        print("\n\n________VS________")

        self.enemy.printStats()

        if self.isFirstGamePlay: printBoxedMsg("Game Started", 1)

        self.promptActions(self.inGamePrompts)

    def exitGame(self):
        print("Thanks for playing", "\nCome back next time")

    def restart(self):
        print("Restarting game!")

        newGame = NewGame(
            avatar = GameCharacter(self.avatar.getOriginalXtics()), # using keyword arguments instead of positional arguments
            enemy = GameCharacter(self.enemy.getOriginalXtics()),
            isFirstGamePlay = False
        )

        newGame.start()

    def checkHealthStatuses(self):
        if (self.avatar.getHealth() <= 0):
            printBoxedMsg(f"OOPS!, {self.enemy.getName()} the {self.enemy.getRace()} killed you")
            
            self.promptActions(self.gameOverPrompts)
        
        elif (self.enemy.getHealth() <= 0):
            printBoxedMsg(f"Hurraay!!, Your avatar {self.avatar.getName().upper()} the {self.avatar.getRace()} has killed {self.enemy.getName()} the {self.enemy.getRace()}")

            print("A splendid victory")

            self.promptActions(self.gameOverPrompts)

        else:
            self.promptActions(self.inGamePrompts)

    def promptActions(self, prompts):
        baseMsg = "\nWhat would you like to do now\n"

        for i in range(len(prompts)):
            baseMsg += f"[{prompts[i][0]}] - {prompts[i][1]}\n" # to give the prompt and the key to the prompt

        action_id = validateInput("Decision", baseMsg, prompts[0][0], prompts[-1][0])

        self.takeAction(action_id)

    def takeAction(self, action_id):
        print("selected", action_id)

        checkHealths = True

        if (action_id == 1): # meaning strike enemy
            self.avatar.attack(self.enemy)

        elif (action_id == 2): # meaning take some damage
            self.enemy.attack(self.avatar)

        elif (action_id == 3): # meaning view avatar status
            self.avatar.printStats()

        elif (action_id == 4): # meaning view enemy status
            self.enemy.printStats()

        elif (action_id == 5): # meaning exit game
            self.exitGame()
            checkHealths = False

        elif (action_id == 6): # meaning re-start game
            self.restart()
            checkHealths = False

        else: # meaning invalid input
            print(f"\nUnknown input, reading: {action_id}\n")
            checkHealths = False
            self.promptActions(self.inGamePrompts)


        # CHECK IN ENEMY OR AVATAR IS STILL ALIVE
        if (checkHealths):
            self.checkHealthStatuses()
