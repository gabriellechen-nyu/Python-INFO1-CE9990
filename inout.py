"""
inout.py

Gabrielle Chen
Homework 1
June 15, 2017
"""

import sys
import math

"""
How old are you? 61
That's about 9 dog years!
"""
age = int(input("How old are you? "))
print("That's about ", round(age/7)," dog years!")

"""
How many pounds does the turkey weigh? 16
How many minutes per pound? 20
That's 320 minutes, or 5 hours and 20 minutes.
"""
weight = int(input("How many pounds does the turkey weigh? "))
minutes = int(input("How many minutes per pound? "))
print("That's ", weight * minutes, " minutes, or ", (weight * minutes)//60, " hours and ", (weight * minutes)%60, " minutes.")


"""
Distance calculator
    Input: x- and y-coordinates for two points
    Output: distance between Point 1 and Point 2

Example:
Enter the x-coordinate of Point 1: 0
Enter the y-coordinate of Point 1: 0
Enter the x-coordinate of Point 1: 3
Enter the y-coordinate of Point 1: 4
The distance between (0.0, 0.0) and (3.0, 4.0) is 5.0.
"""
try:
    x1 = float(input("Enter the x-coordinate of Point 1: "))
except (ValueError, EOFError):
    x1 = 0.0

try:    
    y1 = float(input("Enter the y-coordinate of Point 1: "))
except (ValueError, EOFError):
    y1 = 0.0

try:
    x2 = float(input("Enter the x-coordinate of Point 2: "))
except (ValueError, EOFError):
    x2 = 0.0

try:    
    y2 = float(input("Enter the y-coordinate of Point 2: "))
except (ValueError, EOFError):
    y2 = 0.0

print("The distance between (", x1, ",", y1, ") and (", x2, ",", y2, ") is ", math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2)), ". ")

sys.exit(0)
