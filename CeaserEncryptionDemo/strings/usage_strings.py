__author__ = 'barin.huseyin'
import math
import random

num1 = 89
print "the square root of the number", num1, " is:", math.sqrt(num1)

print "pi:", math.pi

# random.random()

#we are creating random number here between 0-5
print "random number between 0-5 is:", random.choice([0, 1, 2, 3, 4, 5])



#created a string then set it to the variable     len --> give the length of the string and s[1] returns the letter of the variable
s = "Osvaldo"
print len(s)
print s[1]

print s[-1]
print s[-3]


#these [1:] or [:3]  is used to print   then 1 to the end of the string  or  before 3 to start of the string
print s[1:]
print s[:3]


#concetanation of the strings

s = "Spam"
b = s + "xyz"
c = s * 8
print b
print s * 8
print c

print s.find("pa")
print s.replace('Sp', 'ka')
print s

line = "yes,no,maybe"
choice = line.split(",")

print choice[0]

# print choice[1].upper()
# dir(choice)
#
#
# name=raw_input("Enter your name: ")
# surname=raw_input("Enter your surname: ")
#
#
# answer=raw_input("Welcome Dear %s  your name should be %s right !! (Y or N):" % (surname , name))
# if answer=="Y" :
#     print("I got it got it")
# else:
#     print("I am not good today unfortunately")

import re

#pattern matching

nbaPlayers="Kobe is the         mamba**Jordan is the goat**Oscar is the mr triple man***mamba"

#we are looking for line should include "is the"  end space and mamba at the end

deneme="Hello Python world"

denemePattern="Hello[ \t]*(.*)world"

print re.match(denemePattern,deneme).group(1)

pattern="(.*)is the[ \t]*(.*)mamba"
who=re.match(pattern,nbaPlayers)  #returns null if the pattern is not found

print(who.group(1))
print who.groups()


directoryPath="/home/makaveli/documents"
directoryPattern="/(.*)/(.*)/(.*)"

print re.match(directoryPath,directoryPath).group(0)





