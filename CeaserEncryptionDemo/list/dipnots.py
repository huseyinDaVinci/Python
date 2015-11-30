__author__ = 'barin.huseyin'
#You can hold different types in a list in Py
L=[123,"ehlem ve sehlem",1.23]

#we can print whole the list after 1:
print "The elements after the first",L[1:]

#concatination of the lists  very easy isint it
L+=[1,2,3]

#sorting the list    #in Python, if you write print M.sort()  it will return none to show this object is mutable lists are mutable in Py
M=['deron','aaron brooks','paul']
M.sort()
print M

#reversing the list
M.reverse()
print M

#comprehensive listing
Matrix=[[1.2,3],
   [8,9,7],
   [9,5,4]]
print Matrix
print Matrix[1][1]
print Matrix[1:]

c=[row[1] +1 for row in Matrix]
c1=[x for x in "Spaam" if x.islower()] #volareee
print c1
print c

#adding or removing the list elements
L.append("stay on the scene")
L.append("like a sex machine")
L.pop(len(L)-1)


#pop will the elements and the list changes so if you remove elements use it iteratively by calling L.pop
def popingElements(L):
    """This funciton will remove the elements of the list given"""
    num= len(L)
    for i in range(0,num):
        L.pop()


popingElements(L)
#help(popingElements)
print "final", L

#-------------------------------------------