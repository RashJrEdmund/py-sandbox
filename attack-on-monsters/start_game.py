from utils import validateInput, printBoxedMsg

class NewGame:
    def __init__ (self, avatar, enemy):
        self.avatar = avatar
        self.enemy = enemy

        self.prompts = [
                    "strike enemy",
                    "take some damage",
                    "view avatar state",
                    "view enemy state",
                ]
    
    def start(self):
        printBoxedMsg("Game Started", 1)
        self.promptDefaultActions()

    def promptDefaultActions(self):
        baseMsg = "\nWhat would you like to do now\n"

        for i in range(len(self.prompts)):
            baseMsg += f"[{i + 1}] - {self.prompts[i]}\n"

        action_id = validateInput("Decision", baseMsg, 1, 4)

        self.takeAction(action_id)

    def takeAction(self, action_id):
        print(f"you choose - {action_id}")

