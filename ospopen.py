"""
ospopen.py

Gabrielle Chen
Homework 7
July 27, 2017
"""

import sys
import os

file = os.popen("/Library/Frameworks/Python.framework/Versions/3.6/bin/pip3 list --format=legacy")
lines = file.readlines()
status = file.close()

if status != None:
    print("/Library/Frameworks/Python.framework/Versions/3.6/bin/pip3 list produced exit status", status)
    sys.exit(1)

count = 0
for line in lines:
    count+=1

print("Number of installed packages:", count)

sys.exit(0)
