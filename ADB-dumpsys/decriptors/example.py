__author__ = 'barin.huseyin'


# I want to write Email descriptor to be sure before setting a value to Person's emain attribute is in the right format.

# lets do it first create descriptor easily.


class EmailDescriptor(object):
    def __init__(self):
        self.email = {}

    def __get__(self, obj, type):
        return self.email[obj]

    def __set__(self, obj, value):
        if "@" in value:
            self.email[obj] = value
            type(obj)
            print "Your email is  in the right %s" % self.email[obj]
        else:
            self.email[obj] = "!!!!Whopppsssss"
            print "Your email is not in the right %s" % self.email[obj]

    def __del__(self):
        del self.email
        print "Your email attribute was deleted."


# using by property descriptor

class Fireman(object):
    def __init__(self):
        self.email = ""
        self.name = ""
        self.surname = ""


    def fget(self):
        return self.email

    def fset(self, val):
        if "@" in val:
            self.email = val
        else:
            self.email = "!!!!Whopppsssss"

    def fdel(self):
        del self.email

    name = property(fget, fset, fdel, "I am a fireman")


class Person(object):
    email = EmailDescriptor()

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def showPersonInfo(self):
        print "%s   %s  your mail address:%s" % (self.name, self.surname, self.email)


class Student(object):  # using with property we can create getter-setter structure  of descriptors.
    def __init__(self):
        self._name = ""

    def fget(self):
        print "Getting: %s" % self._name
        return self._name

    def fset(self, value):
        print "Setting: %s" % value
        self._name = value.title()

    def fdel(self):
        print "Deleting: %s" % self._name
        del self._name

    name = property(fget, fset, fdel, "I am a name property")
    #name=property(fget,None,fdel,"I am a property")  #by using this None we can sure that this attribute can not be set.


class Employer(object):
    def __init__(self):
        self._name = ""

    @property
    def name(self):
        print "Getting: %s" % self._name
        return self._name

    @name.setter
    def name(self, value):
        print "Setting: %s" % value
        self._name = value

    @name.deleter
    def name(self):
        print "Deleting: %s" % self._name
        del self._name




class Teacher(object):
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname



def main():
    # person1 = Person("ali", "barin")
    # person1.email = "barin@a.com"
    # person1.showPersonInfo()
    #
    # person2 = Person("hasan", "kara")
    # person2.email = "baria.com"
    # person2.showPersonInfo()
    #
    # fire1 = Fireman()
    # fire1.email = "barin@a.com"
    # print fire1.email
    #
    # fire2 = Fireman()
    # fire2.email = "barina.com"
    # print fire2.email


    # stu = Student()
    # stu.name = "Hasan"
    # print stu.name
    #
    # emp=Employer()
    # emp._name="Mahmut"
    # print emp._name



    #seeing object dictionary
    tech1=Teacher("ali","barin")

    print tech1.__dict__

    dic=tech1.__dict__

    print dic["surname"]




if __name__ == "__main__": main()