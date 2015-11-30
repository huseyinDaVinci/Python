import os
import subprocess
import subprocess
import time
import datetime
import thread, threading

__author__ = 'barin.huseyin'

# subprocess.Popen('C:\\Windows\\System32\\calc.exe')


paths = set()

global pathDictionary
pathDictionary={}

def fillThePathSet():
    pathDictionary = {
    "eclipsePath": "C:\\Users\\barin.huseyin\\Downloads\\Compressed\\eclipse-standard-luna-R-win32-x86_64\\eclipse",
    "pycharmPath": "C:\\Program Files (x86)\\JetBrains\\PyCharm Community Edition 4.0.6\\bin\\pycharm.exe",
    "mozillaPath": "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe",
    "evernotePath": "C:\\Program Files (x86)\\Evernote\\Evernote\\Evernote.exe",
    "spotifyPath": "C:\\Users\\barin.huseyin\\AppData\\Roaming\\Spotify\\Spotify.exe"}

    eclipsePath = "C:\\Users\\barin.huseyin\\Downloads\\Compressed\\eclipse-standard-luna-R-win32-x86_64\\eclipse"
    pycharmPath = "C:\\Program Files (x86)\\JetBrains\\PyCharm Community Edition 4.0.6\\bin\\pycharm.exe"
    mozillaPath = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
    evernotePath = "C:\\Program Files (x86)\\Evernote\\Evernote\\Evernote.exe"
    spotifyPath = "C:\\Users\\barin.huseyin\\AppData\\Roaming\\Spotify\\Spotify.exe"

    paths.add(pycharmPath)
    paths.add(eclipsePath)
    paths.add(mozillaPath)
    paths.add(spotifyPath)


def openRelatedApps():
    # C:\Users\barin.huseyin\Downloads\Compressed\eclipse-standard-luna-R-win32-x86_64\eclipse





    for path in paths:
        try:
            subprocess.Popen(path)
            time.sleep(2)
        except Exception as e:
            print e

            # fileName = "C:\\Temp\\" + str(datetime.date.today())+".txt"
            #
            # if not os.path.exists(fileName):
            # os.mkdir(fileName)
            #
            # fo = open(fileName, "wb")


def trial():
    print str(datetime.date.today()) + ".txt"
    fileName = "C:\\Temp\\" + str(datetime.date.today()) + ".txt"

    if not os.path.exists(fileName):
        os.mkdir(fileName)

    print os.listdir("C:\\Temp\\")
    fo = open(fileName, 'r+')


def trash():
    for a in pathDictionary:
        print a


def main():
    fillThePathSet()

    trash()
    # trial()
    # openRelatedApps()


if __name__ == "__main__": main()



# checkList

# start eclipse
# pycharm
# mozilla --nba.com/gameline  --dev.android.com
# evernote
# plan.txt daily plan
# spotify







