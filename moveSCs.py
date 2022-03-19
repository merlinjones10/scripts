#! /usr/local/bin/python3

import os
import shutil
import datetime

TODAY = datetime.datetime.now().strftime("%d-%b-%y")

desktopDir = os.path.join(os.path.expanduser("~"), "Desktop")
screenShotsDir = os.path.join(desktopDir, 'Screenshots')
fileList = []


def filterDirectory(dir, filterFor):
        contents = os.listdir(dir)
        iterator = filter(lambda file: (filterFor in file), contents)
        return list(iterator)


def setUp(path):
    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.exists(os.path.join(path, TODAY)): 
        os.mkdir(os.path.join(path, TODAY))
  

def newFileName(fileName, append):
    timeCreated = fileName.split('at')[1].strip()
    return f"{append}_{timeCreated}"

def moveFiles(fileList):
    todayFolder = os.path.join(screenShotsDir, TODAY)
    print("moved files:")
    for list in fileList:
        for file in list:
            source = os.path.join(desktopDir, file)
            destination = os.path.join(todayFolder, newFileName(file, ('VR' if 'Recording' in file else 'SC')))
            print(destination)
            shutil.move(source, destination)



setUp(screenShotsDir)

mySCList = filterDirectory(desktopDir, 'Screenshot ')
myVideoList = filterDirectory(desktopDir, "Screen Recording")
fileList.append(mySCList)
fileList.append(myVideoList)

moveFiles(fileList)
