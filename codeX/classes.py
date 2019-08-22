#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 23:31:57 2019

@author: kundan
"""
class MyClass:
  x = 5

print(MyClass)
##############################
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)
################################

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
P1=Person("Kundan",23)
print(P1.name)
print(P1.age)

###############################################
class Person:
  name="Ram"
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " +self.name)

p1 = Person("Kundan", 23)
p1.myfunc()

#############################################
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#It does not have to be named self , you can call it whatever 
#you like, but it has to be the first parameter of any function in the class:

############################################MODIFY PROPERTY
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40
print(p1.age)

del p1.age    ###DELETE PROPERTY
print(p1.age)

del p1  ##DELETE OBJECT
print(p1)     
#####################################################