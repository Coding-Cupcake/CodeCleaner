# CodeCleaner
Python script for formatting copied code such that the leading code line numbers will be removed.

When dealing with testing other's code you often have to copy such code out of e.g. pdf files. If such files contain also the code line numbers, you have to remove them manually one by one, which can be really tedious. CodeCleaner detects leading line numbers, removes them and writes the output in a new file, which you can use further for your testing purposes. 

You just have to start the script `Cleaner.py` which will open a text file with your default editor. Note that on a Windows system you only have to double click the file, whereas on Linux systems you must use the terminal and may open the created storage file by your own. Paste your copied code in there and save/close the file afterwards. The result file will be created after you confirmed it on the terminal. Finally you can decide if you want those created files to be removed. 

The script has been tested on Windows 10/Ubuntu 14.04 64-Bit both running Python 2.7. Since the project has been developed using the Eclipse plugin PyDev there are some additional files.
