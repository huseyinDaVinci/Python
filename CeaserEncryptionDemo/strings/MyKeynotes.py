__author__ = 'barin.huseyin'
#these [1:] or [:3]  is used to print   then 1 to the end of the string  or  before 3 to start of the string
s="Osvaldo"
print s[1:]
print s[:3]
print s[1:3]
#-----------------------------------------------

#Formatting the string in Python
name=raw_input("Enter your name: ")
surname=raw_input("Enter your surname: ")
answer=raw_input("Welcome Dear %s  your name should be %s right !! (Y or N):" % (surname , name))
#-----------------------------------------------

#help  function get the object and return the help related to it.
S="Hello"
help(S.replace)
#-------------------------------------------------------------

