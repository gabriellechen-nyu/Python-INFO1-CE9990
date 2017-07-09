"""
christmas.py

Gabrielle Chen
Homework 4
July 6, 2017

Output the lyrics to "The Twelve Days of Christmas"
"""

import sys

ordinal = ["first", "second", "third", "fourth", "fifth", "sixth",
           "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

items = ["Partridge in a Pear Tree", "Two Turtle Doves", "Three French Hens",
         "Four Calling Birds", "Five Golden Rings", "Six Geese a Laying",
         "Seven Swans a Swimming", "Eight Maids a Milking", "Nine Ladies Dancing",
         "Ten Lords a Leaping", "Eleven Pipers Piping", "12 Drummers Drumming"]

for index in range(len(ordinal)):
    print("On the", ordinal[index], "day of Christmas")
    print("my true love sent to me:")
    rlist = items[index::-1]
    for item in rlist:
        if item==items[0]:
            if ordinal[index]=="first":
                print("a ", end="")
            else:
                print("and a ", end="")
        print(item)
    print()

sys.exit(0)
