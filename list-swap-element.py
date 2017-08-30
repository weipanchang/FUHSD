#!/usr/bin/env python
def swap(l,i,j):
    l[i], l[j] = l[j], l[i]

bag=[]
for i in range(10):
    item=int(input("Enter the next item: "))
    bag.append(item)
print bag

print""
print "after swap:"
swap(bag,2,8)
print ""
print bag
