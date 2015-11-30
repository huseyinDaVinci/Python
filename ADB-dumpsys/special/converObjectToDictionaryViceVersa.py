__author__ = 'barin.huseyin'

import decriptors.example

# a class will be created by converting a dictionary to class

class Animal(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


class EmailDescriptorWith__Dict__(object):
    def __init__(self):
        self.email = ""

    def __get__(self, obj, type):
        print "__get__ called"
        return self.email

    def __set__(self, obj, value):
        if "@" in value:
            self.email = value
            print "Your email is  in the right %s" % self.email
        else:
            self.email = "!!!!Whopppsssss"
            print "Your email is not in the right %s" % self.email

    def __del__(self):
        del self.email
        print "Your email attribute was deleted."


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


class Person(object):
    email = EmailDescriptorWith__Dict__()

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def showPersonInfo(self):
        print "%s   %s  your mail address:%s" % (self.name, self.surname, self.email)


class MyDescriptor(object):
    def __init__(self, field=""):
        self.field = field

    def __get__(self, instance, owner):
        print "__get__  called"
        return self.__dict__.get(self.field)

    def __set__(self, instance, value):
        print "__set__  called"
        self.__dict__[self.field] = value


def trash():
    # seeing object dictionary
    tech1 = decriptors.example.Teacher("ali", "barin")
    print tech1.__dict__
    dic = tech1.__dict__  # we are getting object and convert it to the dictionary in Python
    print dic["surname"]



    # we will convert an animal dictionary to the class.

    animals = {"name": "tom", "surname": "mavis", "type": "cat"}

    a = Animal(**animals)

    print a.name, "   ", a.surname, "   ", a.type, "  "  # what a wonda... this is shittttt.


#USE CASE: THINK DATABASE FIELDS EACH HAS ITS OWN VALIDATION LOGIC BUT MIGHT BE ATTACHED TO MANY DIFFERENT CLASSES WITH MANY DIFFERENT NAMES.



class CheckIdDescriptor(object):

    def __init__(self,id=5):
        self.id=id
    def __get__(self, instance, owner):
        print "CheckIdDescriptor: __get__  called"
        return self.id

    def __set__(self, instance, value):
        if(value<5):
            print "Should be greater than"


    def __del__(self):
        del self.id




class Record(object):
    id=CheckIdDescriptor()
    email=EmailDescriptor()


class Assignment(object):
    assignmentId=CheckIdDescriptor()
    assEmail=EmailDescriptor()



















def main():
    p1 = Person("ali", "barin")
    p1.email = "ba@ba"

    print p1.email

    p2 = Person("ertan", "barin")
    p2.email = "baba"
    print p2.email

    print p2.email

    print p2.email







if __name__ == "__main__": trash()
