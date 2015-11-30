import subprocess

__author__ = 'barin.huseyin'

import re

# str = 'an example word:cat!!'
# match = re.search(r'word:\w\w\w', str)
#
# if match:
# print 'found', match.group()  ## 'found word:cat'
# else:
# print 'did not find'



def splitAccordingToEndline(str):
    out = []
    buff = []
    for c in str:
        if c == '\n':
            out.append(''.join(buff))
            buff = []
        else:
            buff.append(c)
    else:
        if buff:
           out.append(''.join(buff))

    return out


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start - len(first):end]
    except ValueError:
        return ""


def getStringFrom(stack, word):
    try:
        start = stack.index(word)
        return stack[start:len(stack)]
    except ValueError as e:
        return e.message



def getHists(counter,hists):

    print "Task Counter is:", counter
    histArray=[]
    for i in range(counter):
        print "Coming i:", i
        if i is not counter - 1:
            histArray.append(find_between(out, "Hist id #" + str(i), "Hist id #" + str(i + 1)))

    if (counter > 0):
        start = "Hist id #" + str(counter - 1)
        latestHist= getStringFrom(out, start)
        histArray.append(latestHist)

    return histArray




def getTasks(counter,tasks):
    print "Task Counter is:", counter
    taskArray=[]
    for i in range(counter):
        print "Coming i:", i
        if i is not counter - 1:
            taskArray.append(find_between(out, "Task id #" + str(i), "Task id " + str(i + 1)))

    if (counter > 0):
        start = "Task id #" + str(counter - 1)
        latestTask= getStringFrom(out, start)
        taskArray.append(latestTask)

    return taskArray


def getStacks(counter, out):
    print "Stack Counter is:", counter
    stackArray=[]
    for i in range(counter):
        print "Coming i:", i
        if i is not counter - 1:
            stackArray.append(find_between(out, "Stack #" + str(i), "Stack #" + str(i + 1)))

    if (counter > 0):
        start = "Stack #" + str(counter - 1)
        latestStack= getStringFrom(out, start)
        stackArray.append(latestStack)

    return stackArray


def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


def findTaskCount(stack):
    counterTask=0
    index=1
    print "Coming stack is:",stack

    stack=stack.split("\n")

    tasks=[]
    for line in stack:
        match = re.search(r'Task id', line)

        if match is not None:
            print "Task is found:",match.group()
            counterTask=counterTask+1;

    if counterTask>0:
        print "**********************************************"

        list=splitAccordingToEndline(getStringFrom(str(stack),"Task id"))
        print "len:",len(list),list
        for i in list:
            print i


    print "Found task number in the given stack:",counterTask





def findCountsTags(out):
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

        # print searchedTagStack
        # print searchedTagHist
        # print searchedTagTask

        resStack = findWholeWord(searchedTagStack)(out)
        resTask = findWholeWord(searchedTagTask)(out)
        resHist = findWholeWord(searchedTagHist)(out)

        if (resStack is not None):
            # print searchedTagStack
            counterStack = counterStack + 1

        if (resTask is not None):
            # print searchedTagTask
            counterTask = counterTask + 1

        if (resHist is not None):
            # print searchedTagHist
            counterHistActivity = counterHistActivity + 1

        if (resStack is None and resTask is None and resHist is None):
            index = 0
        else:
            counter = counter + 1

    print "Found Stack Count:", counterStack
    # print getStacks(counterStack, out)
    print "Found Task Count:", counterTask


    for stack in getStacks(counterStack, out):
        print "---STACK---->",stack


    findTaskCount(stack)

        # for task in getTasks(counterTask,stack):
        #     print "---TASK---->",task
        #     # for i in getHists(counterHistActivity,task):
        #     #     print "---HIST---->",task

    print "Found Hist Count:", counterHistActivity


def main():
    p = subprocess.Popen(["adb shell dumpsys activity activities"], shell=True, stdout=subprocess.PIPE)
    global out
    out, err = p.communicate()
    findCountsTags(out)


if __name__ == ("__main__"): main()