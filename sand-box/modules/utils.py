def test_func():
    print("Printing the content of test_func")

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

def add(val1: int, val2: int):
    return val1 + val2