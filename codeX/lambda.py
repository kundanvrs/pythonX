#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 00:06:02 2019

@author: kundan
"""

x = lambda a: a + 10
print(x(5))

###############################
x = lambda a, b: a * b
print(x(5, 6))

##############################
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)e

print(mydoubler(11))

#################################
def myfunc(n):
  return lambda a : a * n

mydoutler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(tripler(11))


