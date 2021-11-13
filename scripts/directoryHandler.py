import os, sys

def switchToThisDirectory():
    pathToFile = sys.path[0]
    if not os.getcwd() == pathToFile:
        os.chdir(pathToFile)