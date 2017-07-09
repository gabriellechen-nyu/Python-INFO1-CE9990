"""
fileio.py

Gabrielle Chen
Homework 4
July 6, 2017
"""

import sys
import urllib.request

url = "http://oit2.scps.nyu.edu/~meretzkm/python/string/romeo.txt"
count = 0

try:
    lines = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

for line in lines:
    ldecode = line.decode("utf-8")
    for index in range(len(ldecode)):
        if ldecode[index].lower() not in "aeiouy":
            print(ldecode[index], end="")
        else:
            count+=1

print("Number of vowels deleted:", count)

sys.exit(0)
