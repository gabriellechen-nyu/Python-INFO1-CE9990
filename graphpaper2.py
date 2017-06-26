"""
graphpaper2.py

Gabrielle Chen
Homework 2 - Extra Credit
June 22, 2017
"""

import sys

def print_cblanks(columns, cblanks):
    while columns > 0:
        print("+", end="")
        cb = 0
        while cb < cblanks:
            print("-", end="")
            cb+=1
        columns-=1
        if columns < 1:
            print("+", end="")
    print()

def print_rblanks(columns, rblanks, cblanks):
    while rblanks > 0:
        col = 0
        while col-1 < columns:
            print("|", end="")
            cb = 0
            while cb < cblanks:
                print(" ", end="")
                cb+=1
            col+=1
        print()
        rblanks-=1
        
try:
    rows = int(input("How many rows of boxes? "))
except(ValueError, EOFError):
    rows = 3

try: 
    columns = int(input("How many columns of boxes? "))
except(ValueError, EOFError):
    columns = 4
    
try:
    rblanks = int(input("How many rows of spaces in each box (e.g., 1)? "))
except(ValueError, EOFError):
    rblanks = 1
    
try:
    cblanks = int(input("How many columns of spaces in each box (e.g., 3)? "))
except(ValueError, EOFError):
    cblanks = 4

while rows > 0:
    print_cblanks(columns, cblanks)
    print_rblanks(columns, rblanks, cblanks)
    rows-=1
    if rows < 1:
        print_cblanks(columns, cblanks)

sys.exit(0)
