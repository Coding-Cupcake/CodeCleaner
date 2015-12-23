
YES = "Y"
NO  = "N"
QUIT = "Q"

def createTempFile():
    sourceCode = open("sourceCode.txt", "w")
    sourceCode.close()
    return "sourceCode.txt"
