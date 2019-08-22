#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 00:34:41 2019

@author: kundan
"""

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("Kundan", "Singh")
x.printname()

#student class inherit property of person
class Student(Person):
  pass       #Note: Use the pass keyword when you do not want to add 
              # any other properties or methods to the class.

X=Student("Ram","Singh")
X.printname()
########################################### XXXXX

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
x = Person("Mike", "hdgdgd")
x.printname()
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()

"""
Note: The __init__() function is called automatically every time the class 
is being used to create a new object.
When you add the __init__() function, the child class will no longer inherit 
the parent's __init__() function.
To keep the inheritance of the parent's __init__() function, add a call to
 the parent's __init__() function:
  
"""
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()

"""
By using the super() function, you do not have to use the name of the parent 
element, it will automatically inherit the methods and properties from it's parent.

Add a property called graduationyear to the Student class:
"""