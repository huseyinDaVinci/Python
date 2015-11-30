
__author__ = 'barin.huseyin'
# -*- coding: utf-8 -*-

a=set("deneme")
b=set("naber")

print "bir sayı girin"
print "The intersection of two sets:",a.intersection(b)
print "Upadate set a with set b:",a.update(b)
print "Union of two sets:",a.union(b)
print "The difference between of two sets:",a.difference(b)

if "e" in a:
    print "yes e is element of the set "
if "q" in b:
    print "yes q is element of the set b"
else:
    print "no q is element of the set b"
