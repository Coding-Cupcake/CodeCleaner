
import os
from Utils import createSourceFile, createResultFile, YES, NO, QUIT

'Create temporary source code storage file'
FilenameSource = createSourceFile()
FilenameResult= createResultFile()
os.system("start "+FilenameSource)

'Instruct the user to copy the code in there and close the file'
print("Please copy your code into the temporary sourceCode file and save/close it")

while 1:
    ready = raw_input("\n" + "Have you saved and closed the file? (y/n)")
    if ready.upper() == YES:
        print("Processing file ...")
        sourceCode = open(FilenameSource, "r")
        resultCode = open(FilenameResult, "w")
        for line in sourceCode:
            i = 0
            while line[i].isdigit():
                i = i + 1
            resultCode.write(line[i:])
        print("\n" + "Successfully created the resultCode file!")
        break
        
    elif ready.upper() == NO:
        print("Please save and close the file to proceed or type q to quit.")        
    
    else:
        if ready.upper() == QUIT:
            os.remove(FilenameSource)
            exit()
        print(ready + " is not a valid input. Type in y or n to continue, q to quit.")
        
    
sourceCode.close()
resultCode.close()

cleanup = raw_input("\n" + "Do you want to remove the created files? (y/n)")

if cleanup.upper() == "Y":
    os.remove(FilenameSource)
    os.remove(FilenameResult)

    