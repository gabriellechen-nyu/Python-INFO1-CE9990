"""
forif.py

Gabrielle Chen
Homework 3
June 29, 2017
"""

import sys

word = input("Enter a word: ")
for i in range(0, len(word)):
    if word[i] not in "aeiouy":
        print(word[i].upper(), end="")
    else:
        print(word[i].lower(), end="")
print()

sys.exit(0)
