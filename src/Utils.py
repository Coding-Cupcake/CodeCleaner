
from datetime import datetime

YES = "Y"
NO  = "N"
QUIT = "Q"
SOURCE = "sourceCode"
RESULT = "resultCode"

'Create a file storing the copied source code'
def createSourceFile():
    FILENAME = SOURCE + datetime.now().strftime('%Y-%m-%d-%I-%M-%S') + ".txt"
    sourceCode = open(FILENAME, "w")
    sourceCode.close()
    return FILENAME

'Create the name of the file storing the formatted result'
def createResultFile():
    FILENAME = RESULT + datetime.now().strftime('%Y-%m-%d-%I-%M-%S') + ".txt"
    return FILENAME