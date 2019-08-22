#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 00:20:59 2019

@author: kundan
"""

thislist = ["apple", "banana", "cherry"]

print(thislist)
print(thislist[1])
print(len(thislist))

thislist[1] = "blackcurrant"
print(thislist)

for x in thislist:
  print(x)
  
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
thislist.append("orange")
print(thislist)

thislist.insert(1, "grapes")
print(thislist)

thislist.remove("cherry")
thislist.pop()
del thislist[0]
del thislist

thislist.clear()  #delete list item
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
mylist = list(thislist)
print(mylist)

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""