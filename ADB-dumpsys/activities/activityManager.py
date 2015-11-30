import subprocess

# getting activity manager stack boxes to see current table easily




def mySubProcessCallerDecorator(func):
    def wrapper(command, **kwargs):
        import time
        from time import gmtime, strftime

        t = time.clock()
        p = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE)
        out, err = p.communicate()

        if kwargs is not None:

            func(command, **kwargs)
        else:
            func(command)

        print out
        print "Log Time is:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()), "Function name:", func.__name__
        print "-------------------------------------------------------------------------------"

    return wrapper


def trial(command):
    p = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE)
    out, err = p.communicate()
    print out


@mySubProcessCallerDecorator
def showAmStackBoxes(command, **kwargs):
    print "RESULTS FOR STACK BOXES OF ACTIVITY"


@mySubProcessCallerDecorator
def showSpecificPackage(command, **kwargs):
    for key, value in kwargs.iteritems():

        print "RESULTS FOR THE PACKAGE-----",str(value).upper()


@mySubProcessCallerDecorator
def showPackageRelated(command, **kwargs):
    print "RESULTS FOR THE PACKAGE RELATED"


def menu():

    package = raw_input("Enter your package name:")
    command = "adb shell dumpsys activity package " + package

    commands["packageInfo"] = command

    showPackageRelated(commands["packageGrantedPermissions"])
    showAmStackBoxes(commands["stackBoxes"])
    showSpecificPackage(commands["packageInfo"], path=package)



# we can use a dictionary to hold commands
commands = {"stackBoxes": showAmStackBoxes("adb shell am stack boxes"),
            "packageInfo": showSpecificPackage("adb shell dumpsys activity package com.teknosa"),
            "packageGrantedPermissions": showPackageRelated("adb shell dumpsys package com.teknosa perm ")}
#
#
tempCommands = {"stackBoxes": showAmStackBoxes,
            "packageInfo": showSpecificPackage,
            "packageGrantedPermissions": showPackageRelated}
options={}
def main():

    print commands
    temp=[]
    counter=1
    for key,value in commands.iteritems():
        print counter,"-->",key
        options[str(counter)]=key

        temp.append(key)
        counter=counter+1

    print temp
    print options

    choise=raw_input("Enter your choise(1,2,3):")

    func=options[str(choise)]

    #calling function from dictionary  d['foo']()

    print tempCommands[func]
    tempCommands[func]("adb shell am stack boxes")





if __name__ == "__main__": main()

