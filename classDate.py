"""
classDate.py

Gabrielle Chen
Homework 8
August 3, 2017

Create a class named Date and call one of its class methods (monthsInYear).
Then create an object named d of class Date and call its instance methods.
"""

import sys

class Date(object):
    """
    Class Date demonstrates class and instance attributes, class and instance methods.
    It is a simple date class, containing year, month, and day integers.
    """

    january = 1
    february = 2
    march = 3
    april = 4
    may = 5
    june = 6
    july = 7
    august = 8
    september = 9
    october = 10
    november = 11
    december = 12

    lengths = [
        None,
        31, #January
        28, #February
        31, #March
        30, #April
        31, #May
        30, #June
        31, #July
        31, #August
        30, #September
        31, #October
        30, #November
        31  #December
    ]

    def __init__(self, month, day, year):
        assert isinstance(year, int)
        # assert isinstance(month, int) and 1 <= month and month <= 12
        assert isinstance(month, int) and 1 <= month and month <= Date.monthsInYear()
        assert isinstance(day, int) and 1 <= day and day <= Date.lengths[month]
        self.year = year
        self.month = month
        self.day = day

    #These three methods are getters.

    def getYear(self):
        "Return my year."
        return self.year

    def getMonth(self):
        "Return the number of my month (1 to 12 inclusive)."
        return self.month

    def getDay(self):
        "Return the number of my day (1 to the length of my month, inclusive)."
        return self.day

    def __str__(self):
        "Return a string that looks like the contents of myself."
        return "{:02}/{:02}/{:04}".format(self.month, self.day, self.year)

    def dayOfYear(self):
        "Return my day of the year: a number in the range 1 to 365 inclusive."
        return sum(Date.lengths[1:self.month]) + self.day

    def nextDay(self):
        "Move myself one day into the future."
        if self.day < Date.lengths[self.month]:
            self.day += 1
        else:
            self.day = 1       #Go to the first day of the next month.
            # if self.month < len(Date.lengths) - 1:
            if self.month < Date.monthsInYear():
                self.month += 1
            else:
                self.month = 1 #Go to the first month of the next year.
                self.year += 1

    def nextDays(self, n):
        "Move myself n days into the future."
        assert isinstance(n, int) and n >= 0
        for i in range(n):
            self.nextDay()     #Call the instance method in line 62.

    def prevDay(self):
        "Move myself one day into the past."
        if self.day > 1:
            self.day -= 1
        else:
            if self.month > 1:
                self.month -= 1
            else:
                self.month = 12
                self.year -= 1
            self.day = Date.lengths[self.month]

    def prevDays(self, n):
        "Move myself n days into the past."
        assert isinstance(n, int) and n >= 0
        for i in range(n):
            self.prevDay()

    def __sub__(self, other):
        s = 365 * self.year + self.dayOfYear()
        o = 365 * other.year + other.dayOfYear()
        return s - o

    def __lt__(self, other):
        return self - other < 0

    @staticmethod
    def monthsInYear():
        "Return the number of months in a year. This function is selfless."
        return len(Date.lengths) - 1;

    @staticmethod
    def daysInYear():
        "Return the number of days in a year. This function is selfless."
        return sum(Date.lengths[1:])

    #The definition of class Date ends here.


# print("months in year =", Date.monthsInYear())
# d = Date(12, 31, 2017)
d = Date(Date.december, 31, 2017)   #Call the instance method in line 32.
print("months in year =", d.monthsInYear())
print("days in year =", d.daysInYear())
print("type(d) =", type(d))
print()

#These three statements do the same thing:
print("d =", d)
print("d =", str(d))
print("d =", d.__str__())      #Call the instance method in line 54.
print()

print("month =", d.getMonth()) #Call the instance method in line 46.
print("day =", d.getDay())     #Call the instance method in line 50.
print("year =", d.getYear())   #Call the instance method in line 42.
print()

print("{} is day number {} of the year {}.".format(d, d.dayOfYear(), d.getYear()))
d.nextDay()                    #Call the instance method in line 62.
print(d, "is the next day.")
d.nextDays(7)                  #Call the instance method in line 74.
print(d, "is a week after that.")

print()

p = Date(Date.january, 1, 2017)
print("{} is day number {} of the year {}.".format(p, p.dayOfYear(), p.getYear()))
p.prevDay()
print(p, "is the previous day.")
p.prevDays(7)
print(p, "is a week before that.")

print()

t1 = Date(Date.december, 31, 2018)
t2 = Date(Date.december, 31, 2017)
print(t1 - t2)
if t2 < t1:
    print(t2, " is earlier than ", t1, ".", sep="")
else:
    print(t2, " is equal to or later than ", t1, ".", sep="")

sys.exit(0)
