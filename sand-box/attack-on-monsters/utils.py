def validateInput(stat, baseMsg, leastVal, highestVal):
    data = int(input(baseMsg))

    if (data < leastVal or data > highestVal):
        newMsg = f"\n{stat} must be a value between {leastVal} and {highestVal}, please try again\n"
        validateInput(stat, newMsg, leastVal, highestVal)
    else:
        return data

def printBoxedMsg(message, lines = 0):
    length = len(message)

    dashes = ""

    newLines = "\n"
    
    if (lines > 0):
        for i in range(lines):
            newLines += "\n"

    for i in range(length + 4):
        dashes += "-"
    
    print(f"{newLines}{dashes}", f"\n| {message} |", f"\n{dashes}{newLines}")
