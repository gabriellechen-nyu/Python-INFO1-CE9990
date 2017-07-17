"""
restaurant.py

Gabrielle Chen
Homework 5
July 13, 2017
"""

import sys
import csv

filename = "DOHMH_New_York_City_Restaurant_Inspection_Results.csv"

try:
    csvfile = open(filename, encoding="utf-8", newline="")
except FileNotFoundError:
    print("Sorry, could not find file \"", filename, "\".", sep="")
    sys.exit(1)
except PermissionError:
    print("Sorry, no permission to open file \"", filename, "\".", sep="")
    sys.exit(1)

lines = csv.reader(csvfile)

"""
Read records into a list
"""
restaurants = []
seen = set()
slength = 0
blength = 0

query = input("Enter a street name (e.g., Wall Street, 18th Ave): ")

for line in lines:
    try:
        check = int(line[3])
        if line[4] == query.upper() and line[0] not in seen and line[1]!="":
            restaurants.append(line)
            seen.add(line[0])
            if slength < len(line[3]):
                slength = len(line[3])
            if blength < len(line[2]):
                blength = len(line[2])
    except ValueError:
        pass

csvfile.close()

def score(line):
    return int(line[3])

if len(restaurants)==0:
    print("No results found")
else:
    restaurants.sort(key=score)
    for line in restaurants:
        print("{:>{}}".format(line[3], slength), line[4], ",", "{:{}}".format(line[2], blength), "-", line[1])
        
sys.exit(0)
