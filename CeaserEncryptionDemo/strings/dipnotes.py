__author__ = 'barin.huseyin'

#1-Strings are immutable in Python since we cannot change its content only we can create a new string like in the example#
s="Sanchez"
#s[0]='K'
#print s  #this will give an error if you compile this.
s='K'+s[1:]
print s
# Every object in Python is classified as either immutable (unchangeable) or not. In terms
# of the core types, numbers, strings, and tuples are immutable; lists and dictionaries are
# not (they can be changed in-place freely).

