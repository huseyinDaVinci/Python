import subprocess

__author__ = 'barin.huseyin'

#problem is converting string to list according to "\n"


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

def trial(stack):
    stack2=getStringFrom(stack,"Task id")
    sub=stack2.split("\n")
    for line in sub:
        print "???????",line

def trial(stack):
def convertStringToList(out):

    stack=find_between(out,"Stack #0","Stack #1")
    stack2=getStringFrom(out,"Stack #1")
    trial(stack2)
    subStackList=stack2.split("\n")
    list=out.split("\n")


    print "len of list:",len(list)
    for line in list:
        print "-------",line

    for line in subStackList:
        print "*******",line


def main():
    p = subprocess.Popen(["adb shell dumpsys activity activities"], shell=True, stdout=subprocess.PIPE)
    global out
    out, err = p.communicate()
    convertStringToList(out)
    #print out

if __name__=="__main__":main()