__author__ = 'barin.huseyin'
# genereator example


def funcExerciseSecond(kind="shout"):
    def shout(word="yes"):
        return word.capitalize() + "!!!"

    def wordWrapper(word="yes"):
        return word.lower() + "..."

    if kind == "shout":
        return shout
    else:
        return wordWrapper


def funcExercise():
    def getRange():
        for i in range(5):
            yield i ** 3

    def decoraderExample(myfunc):
        def myfunc(args):
            print "spam"


    def shout(word="hello"):
        return word.capitalize() + "!"

    scream = shout

    print "Scream", scream()
    print "Shout", shout()

    del shout
    try:
        print shout()
    except Exception as myError:
        print myError
    finally:
        print "in Finally block Shout"

    print "Shout was deleted but Scream is on its way", scream()


def checkUserLogged(name):
    if name == "jane":
        print "User ", name, " logged into system no problemo"
        return 1
    else:
        return 0


def makeJsonRequest(webService):
    print "Coming Web Service:", webService


def callWebService(webService, checkFunc, userName):
    print "May be I can perform some operations before the function is run"

    if (checkFunc(userName) is 1):
        return makeJsonRequest(webService)
    else:
        print "Login is unsuccessfull"


def myDecorator(funcM):
    def myWrapper(args1,args2):
        print "Before the function is run I got the arguments:",args1,"  ",args2
        funcM(args1,args2)
        print "After the function is run I got the arguments:",args1,"  ",args2
    return myWrapper


def mainTemp():
    talk = funcExerciseSecond()  # we get here a function as a returning object

    print talk  # output:  <function shout at 0x0221B030>

    print talk()  # output: Yes!!!

    print funcExerciseSecond("deneme")  # output: <function wordWrapper at 0x0210B3B0>

    print funcExerciseSecond("deneme")()  # output: yes...

    # one strange trial goes to

    temp = []
    temp2 = []

    for i in range(5):
        temp.append(funcExerciseSecond())
        temp2.append(funcExerciseSecond()())

    print temp  #output: <function shout at 0x0254B030>, <function shout at 0x0254B370>, <function shout at 0x0254B3B0>, <function shout at 0x0254B3F0>, <function shout at 0x0254B070>]
    print temp2  #output :  ['Yes!!!', 'Yes!!!', 'Yes!!!', 'Yes!!!', 'Yes!!!']


def mainTemp2():
    callWebService("Customer Webservice", checkUserLogged, "jane")
    # Output:  May be I can perform some operations before the function is run
    # User  jane  logged into system no problemo
    # Coming Web Service: Customer Webservice
    print "---------------------------------------------------"
    callWebService("Customer Webservice", checkUserLogged, "mahmut")
    # Output: May be I can perform some operations before the function is run
    # Login is unsuccessfull


def main():

    @myDecorator
    def sayHello(name,surname):
        print "Hello\t", name, "\t ", surname

    sayHello("jane","crawford")

    #
    # #sayHello=myDecorator(sayHello)
    #
    #
    # aDecorator=myDecorator(sayHello)
    # aDecorator()
    #
    # #print sayHello()


if __name__ == "__main__": main()