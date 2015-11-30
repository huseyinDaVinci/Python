'''
Created on Apr 7, 2015

@author: barin.huseyin
'''
#in python some variables are immutable example "strings"  #immutable means you can change nothing in a string pointing the same variable

#STRINGS ARE IMMUTABLE------

a='this is not means Strings are mutable we are only changing the pointer and create a new variable actually'

print a

a=a.replace('is', 'the')   # here we are creating actually new variable label remains the same but old content is pointed any more. 
 
print a

c = 'abxde'
b = a.replace('x', 'c')

print c
print b

######################################################################
tup = ('physics', 'chemistry', 1997, 2000);
tup=tuple()
print "After deleting tup : "
print tup;