"""
ospopen.py

Gabrielle Chen
Homework 7
July 27, 2017
"""

import sys
import os

file = os.popen("ps -A -o comm")
lines = file.readlines()
status = file.close()

if status != None:
    print("\"ps -A -o comm\" produced exit status", status)
    sys.exit(1)

lines = set(lines[1:])
lines = [line.rstrip() for line in lines]
lines = [line.split("/")[-1] for line in lines]
lines = sorted(lines, key=len)

for i, line in enumerate(lines, start=1):
    print("{:3} {}".format(i, line))

sys.exit(0)
