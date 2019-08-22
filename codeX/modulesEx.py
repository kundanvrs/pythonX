#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 00:55:50 2019

@author: kundan
"""
  
import mymodule
mymodule.greeting("Kundan")

a = mymodule.person1["age"]
print(a)

from mymodule import person1
print (person1["age"])
"""
Note: When importing using the from keyword, do not use the module name when referring to elements in 
the module. Example: person1["age"], not mymodule.person1["age"]

"""