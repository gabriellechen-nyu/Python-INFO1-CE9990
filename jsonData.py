"""
jsonData.py

Gabrielle Chen
Homework 7
July 27, 2017
"""

import sys
import urllib.request
import json

url = "https://data.cityofchicago.org/api/views/xzkq-xp2w/rows.json?accessType=DOWNLOAD"

try:
    source = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

file = source.read()
source.close()

try:
    utfFile = file.decode("utf-8")
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)

try:
    dictionary = json.loads(utfFile)
except json.JSONDecodeError as jsonDecodeError:
    print(jsonDecodeError)
    sys.exit(1)

dept = {}

for data in dictionary["data"]:
    if data[10] not in dept and data[14]!=None:
        dept[data[10]] = [data[14], data[14]]
    else:
        try:
            if float(data[14]) < float(dept[data[10]][0]):
                dept[data[10]][0] = data[14]
            if float(data[14]) > float(dept[data[10]][1]):
                dept[data[10]][1] = data[14]
        except TypeError:
            continue

for name in sorted(dept):
    print(name)
    print("Minimum annual salary: ", dept[name][0])
    print("Maximum annual salary: ", dept[name][1])
    print()

sys.exit(0)
