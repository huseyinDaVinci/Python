__author__ = 'barin.huseyin'

from os import system
import subprocess
import sys

def runInShell(command):
    print system(command)






# "input" provides system data for input components such as touchscreens or built-in keyboards.

#print system("adb shell dumpsys input")


#print system("adb shell dumpsys battery")

def trash():
    print system("adb shell dumpsys -l")








def main():

    runInShell("adb shell dumpsys iphonesubinfo")
    #runInShell("dumpsys | grep 'com.teknosa'")

if __name__=="__main__":main()

