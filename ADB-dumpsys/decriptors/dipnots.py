__author__ = 'barin.huseyin'


# Descriptors look weird-they're attacted to the class and methods have a funky signatue.



#self is the instance of the itself of descriptor.


class MyDescriptor(object):
    def  __get__(self, obj, type):
        print self,obj,type

    def __set__(self, obj,val):
        print  "Got %s " % val


class MyClass(object):
    x=MyDescriptor()  #Attached at class defination time




def main():
    a=MyClass()
    # print a
    a.x=4   #setting operation here.
    print a.x   #getting operation.







if __name__ == "__main__": main()