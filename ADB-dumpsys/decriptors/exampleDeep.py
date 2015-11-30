__author__ = 'barin.huseyin'



class Employee(object):
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname




def main():
  emp=Employee("ahmet","burcak")
  emp.name="ali"
  emp.surname="barin"

  print "Name: %s   Surname:%s" %(emp.name,emp.surname)


if __name__ == "__main__": main()