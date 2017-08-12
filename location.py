"""
location.py

Gabrielle Chen
Homework 9
August 10, 2017

This file is a Python module. You can import this module by saying
import location
at the top of your Python script.
Then in your script, you can use class location.Location
"""

import sys
import urllib.request
import json

class Location(object):
    def __init__(self, latitude, longitude):
        assert isinstance(latitude, int) or isinstance(latitude, float)
        assert isinstance(longitude, int) or isinstance(longitude, float)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        vertical = "N" if self.latitude >= 0 else "S"
        horizontal = "E" if self.longitude >= 0 else "W"
        return "{}°{} {}°{}".format(abs(self.latitude), vertical, abs(self.longitude), horizontal)

    def getLatitude(self):
        return self.latitude

    def setLatitude(self, newLat):
        self.latitude = newLat

    def getLongitude(self):
        return self.longitude

    def setLongitude(self, newLong):
        self.longitude = newLong

    def getZipcode(self):
        url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}".format(self.latitude, self.longitude)

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

        results = dictionary["results"]
        if len(results) > 0:
            address_components = results[0]["address_components"]
            for component in address_components:
                if "postal_code" in component["types"]:
                    return int(component["long_name"])
        return 0

    # The definition of class Location ends here.


if __name__ == '__main__':
    l = Location(26.074478, 119.29648199999997)
    print("The latitude of {} is {}.".format(l, l.getLatitude()))
    print("The longitude of {} is {}.".format(l, l.getLongitude()))
    print("The zipcode of {} is {}.".format(l, l.getZipcode()))

    print("\nChanging latitude and longitude...\n")
    l.setLatitude(-27.4978543)
    l.setLongitude(153.01328609999996)

    print("The latitude of {} is {}.".format(l, l.getLatitude()))
    print("The longitude of {} is {}.".format(l, l.getLongitude()))
    print("The zipcode of {} is {}.".format(l, l.getZipcode()))
    
    sys.exit(0)
