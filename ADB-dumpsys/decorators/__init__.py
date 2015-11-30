__author__ = 'barin.huseyin'




def myDecoratorWithArbitaryArguments(myFunc):
    def wrapper(*args,**kwargs):
        print "Do I have any args,kwargs"
        print args
        print kwargs
        myFunc(*args,**kwargs)

    return wrapper

@myDecoratorWithArbitaryArguments
def function1(a,b,c):
    print "A:",a,"B:",b,"C:",c

@myDecoratorWithArbitaryArguments
def function2():
    print " I do not take any arguments"

@myDecoratorWithArbitaryArguments
def function_with_named_arguments(a, b, c, platypus="Why not ?"):
    print "Do %s, %s and %s like platypus? %s" %\
    (a, b, c, platypus)

def myDecorator(methodToDecorate):
    def wrapper(self,lie):
        lie=lie-3
        return methodToDecorate(self,lie)

    return wrapper


class Person(object):
    def __init__(self):
        self.age=32

    @myDecorator
    def sayYourAge(self,lie):
        print "I am %s years old what do you think" % (self.age+lie)

def main():
    # person=Person()
    # person.sayYourAge(-3)
    function1(1,2,3)
    function2()
    function_with_named_arguments("Bill", "Linus", "Steve", platypus="Indeed!")


if __name__=="__main__":main()

