"""
control.py

Gabrielle Chen
Homework 2
June 22, 2017
"""

import sys

def find_animal(year):
    if year%12==0:
        return "Monkey"
    elif year%12==1:
        return "Rooster"
    elif year%12==2:
        return "Dog"
    elif year%12==3:
        return "Pig"
    elif year%12==4:
        return "Rat"
    elif year%12==5:
        return "Ox"
    elif year%12==6:
        return "Tiger"
    elif year%12==7:
        return "Rabbit"
    elif year%12==8:
        return "Dragon"
    elif year%12==9:
        return "Snake"
    elif year%12==10:
        return "Horse"
    else:
        return "Goat"

err = True
while err:
    try:
        year = int(input("What is your birth year? "))
        err = False
    except (ValueError, EOFError):
        print("Please enter a valid year.")
        pass
    
print("You were born in the Year of the", find_animal(year))

sys.exit(0)
