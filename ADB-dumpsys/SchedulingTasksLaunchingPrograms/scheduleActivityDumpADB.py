import os

__author__ = 'barin.huseyin'
import subprocess
import time
import datetime
import thread, threading
import activities.activityDump
# subprocess.Popen('C:\\Windows\\System32\\calc.exe')


def main():
    print "I will start another py script"

    dumpResult = ""

    while True:
        # save the results to file periodacally

        # here I will start again script

        print "I will start again script"
        fo = open("C:\\Temp\\activityDump.txt", "wb")

        try:
            dumpResult = activities.activityDump.onlyPrintHierachyStackInfo()
            fo.write(dumpResult)
        except IOError as e:
            print e
        finally:
            # Close opend file
            fo.close()

        time.sleep(10)








        # subprocess.Popen('python C:\\ScheduledPythonScripts\\ActivityDump.py')
        # time.sleep(10)
        # subprocess.Popen('cls')


if __name__ == "__main__": main()