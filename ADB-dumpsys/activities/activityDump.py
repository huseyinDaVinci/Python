# -*- coding: utf-8 -*-

import subprocess

__author__ = 'barin.huseyin'
import os


class ActivityDump:
    def __init__(self, packageName, activityName):
        self.packageName = packageName
        self.activityName = activityName

    def getDumpInfo(self):
        return os.system("adb shell dumpsys activity activities")


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def find_between_r(s, first, last):
    try:
        start = s.rindex(first) + len(first)
        end = s.rindex(last, start)
        return s[start:end]
    except ValueError:
        return ""


import re


def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


def getTaskPiece(stack):
    title = "tasks".upper()

    tasks = stack.split("Task id #")
    for i in range(len(tasks)):

        if i is not 0:
            print title + " " + str(i - 1)
            print tasks[i]

            # getHıstPiece(tasks[i])


# def getHıstPiece(task):
# hists = task.split("Hist id #")
# for i in range(len(hists)):
#         print hists[i]
#     print "---------------------------------------------------"
#

def getStackPiece(count):
    title = "stack".upper()

    lines = out.split("Stack #")
    for i in range(len(lines)):
        if i is not 0:
            print title + " " + str(i - 1)
            print lines[i]
            #getTaskPiece(lines[i])
        print "-------------------------------------------------------------"


def onlyPrintHierachyStackInfo():
    p = subprocess.Popen(["adb shell dumpsys activity activities"], shell=True, stdout=subprocess.PIPE)
    global out
    out, err = p.communicate()

    lines = out.split("\n")


    tags={"Stack #":"","Task id":"  ","lastActiveTime:":"   ",
          "* Hist #":"     ","realActivity=":"       ",
          "state=":"       ","Running activities":"",
          "Run #":"  ","Recent Tasks:":"","Recent #":"  ","Intent {":"       ",
          "mCurTaskId":""}


    result=""
    for line in lines:
        for tag in tags:
            if tag in line:
                result=result+ tags.get(tag)+line +"\n"

    return result
                # print tags.get(tag),line






def main():

    # dump= os.system("adb shell dumpsys activity activities")

    #
    # dump= check_output(["adb shell dumpsys activity activities"],shell=True)
    #
    # print find_between(dump,"Stack #0","Stack #1")

    p = subprocess.Popen(["adb shell dumpsys activity activities"], shell=True, stdout=subprocess.PIPE)
    global out
    out, err = p.communicate()

    lines = out.split("\n")

    counterStack = 0
    counterTask = 0
    counterHistActivity = 0
    counter = 0

    index = 1

    res = findWholeWord("Task id #" + str(1))(out)

    print res
    while index:


        searchedTagStack = "Stack #" + str(counter)
        searchedTagTask = "Task id #" + str(counter)
        searchedTagHist = "Hist #" + str(counter)

        print searchedTagStack
        print searchedTagHist
        print searchedTagTask

        resStack = findWholeWord(searchedTagStack)(out)
        resTask = findWholeWord(searchedTagTask)(out)
        resHist = findWholeWord(searchedTagHist)(out)

        if (resStack is not None):
            print searchedTagStack
            counterStack = counterStack + 1

        if (resTask is not None):
            print searchedTagTask
            counterTask = counterTask + 1

        if (resHist is not None):
            print searchedTagHist
            counterHistActivity = counterHistActivity + 1

        if (resStack is None and resTask is None and resHist is None):
            index = 0
        else:
            counter = counter + 1

    print "Found Stack Count:", counterStack
    print "Found Task Count:", counterTask
    print "Found Hist Count:", counterHistActivity

    getStackPiece(counterStack)


if __name__ == "__main__": onlyPrintHierachyStackInfo()

#if __name__ == "__main__": main()

