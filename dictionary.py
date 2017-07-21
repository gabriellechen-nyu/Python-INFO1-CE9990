"""
dictionary.py

Gabrielle Chen
Homework 6
July 20, 2017
"""

import sys

languages = {
    "python": ("Guido van Rossum", 1991),
    "c": ("Dennis Ritchie", 1972),
    "java": ("James Gosling", 1995),
    "c++": ("Bjarne Stroustrup", 1979),
    "c#": ("Microsoft", 2000),
    "r": ("Ross Ihaka and Robert Gentleman", 1993),
    "javascript": ("Brendan Eich", 1995),
    
    "php": ("Rasmus Lerdorf", 1994),
    "go": ("Robert Griesemer, Rob Pike, and Ken Thompson", 2009),
    "swift": ("Chris Lattner", 2014),
    "visual basic .net": ("Microsoft", 2001),
    "pascal": ("Niklaus Wirth", 1970),
    "perl": ("Larry Wall", 1987),
    "ruby": ("Yukihiro Matsumoto", 1995),

    "assembly": ("David Wheeler", 1949),
    "visual basic": ("Alan Cooper and Microsoft", 1991),
    "matlab": ("Cleve Moler", 1984),
    "sql": ("Donald Chamberlin and Raymond Boyce", 1974),
    "objective-c": ("Brad Cox and Tom Love", 1984),
    "scala": ("Martin Odersky", 2004),
    "fortran": ("John Backus", 1957)
}

while True:
    query = input("Enter a programming language (e.g., Python, Java): ")

    if query=="":
        sys.exit(0)
    
    if query.lower() in languages:
        print(query.upper(), "was created by", languages[query.lower()][0], "and was released in", languages[query.lower()][1])
    else:
        print("Query not found")

    print()
