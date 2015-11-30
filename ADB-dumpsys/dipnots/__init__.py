import subprocess

__author__ = 'barin.huseyin'

import socket
#id()  --> give the user hash code in the memory of the object.
#type() --> return the type of the object.

#id is very nice since we can learn how Python use memory or mutable and immutable objects

a=5
print id(a)
print type(a)
s=set("deneme")
print "Before union reference:",id(s),"Set:",s
#--------------------------------------------
s.update("selam")
print "After union reference:",id(s)," Set:",s
print type(s)

b=set("naber")

print s.intersection(b)




