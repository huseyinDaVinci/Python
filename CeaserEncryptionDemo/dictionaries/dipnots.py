__author__ = 'barin.huseyin'
#most flexible built-in data type    dictionaries are unordered collections  items stored with key

#accessed by key not offset      -----  unordered collections of arbitrary objects  ---variable-length heterogeneous and arbitarily nestable

#*****mutable mapping  -THEY ARE MUTABLE MY FRIEND

D={}
Y={'spam':2,'eggs':3}

#nesting example
D={'school':{'class':4,'course':'science'}}
print D['school']


Y['spam']=5   #you see here dicti. are mutable collections

print Y.keys()
D=dict(zip(D.keys(),D.values()))
print D.keys()

print D.items()

B=D.copy()  #you can directly copy the dictionary to other
print B.items()

print len(D)

#you can delete any item by key

del D['school']
print D

list(B.keys())  # this is in Python 3.0

#D={x :x*2 for x in range(10)}  # this is in Python 3.0

print B.get('school')

#let merge two dictionaries together

A={'school':{'class':4,'course':'science'}}

B={'school':{'class':7,'course':'space'}}

A.update(B)

print "result: " ,A






