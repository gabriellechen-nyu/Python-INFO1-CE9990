"""
listoflists.py

Gabrielle Chen
Homework 5
July 13, 2017
"""

import sys
import csv
import urllib.request

url = "https://data.cityofnewyork.us/api/views/xx67-kt59/rows.csv?accessType=DOWNLOAD"

try:
    lines = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

restaurants = []
seen = set()

for line in lines:
    try:
        string = line.decode("utf-8")
    except UnicodeError as unicodeError:
        print(unicodeError)
        sys.exit(1)

    reader = csv.reader([string])
    fields = next(reader)

    date = fields[8].split("/")

    if fields[14] == "Not Yet Graded" and date[2] == "2017" and fields[0] not in seen:
        restaurants.append(fields)
        seen.add(fields[0])

lines.close()

def score(line):
    return line[1]

if len(restaurants)==0:
    print("All restaurants have been graded in 2017")
else:
    restaurants.sort(key=score)
    for restaurant in restaurants:
        print("{} - {} {}, {}".format(restaurant[1], restaurant[3], restaurant[4], restaurant[2]))

sys.exit(0)
