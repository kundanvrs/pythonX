#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 23:51:28 2019

@author: kundan
"""

def my_function():
  print("Hello from a function")
  
my_function()   #function call
##############################
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

################################# DEFAULT PARAMETER
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#################################PASS LIST
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
################################# RETURN PARAMETER
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

########################## RECURSION XXXX
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

