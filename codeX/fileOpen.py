#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 01:17:39 2019

@author: kundan
"""

f = open("demofile.txt")
f = open("demofile.txt", "rt")

f = open("demofile.txt", "r")
print(f.read())

f = open("demofile.txt", "r")
print(f.read(5))
print(f.readline())
for x in f:
  print(x)

########## WRITE #########
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

"""
"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist

"""

##################### DELETE 
import os
os.rmdir("myfolder")

import os
os.remove("demofile.txt")

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")