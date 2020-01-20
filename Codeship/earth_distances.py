'''
To describe a specific position on the surface of the Earth, we must rely on the geographic coordinate system. The geographic 
coordinate system is a method used to give every possible location on Earth to be specified by a set of numbers or letters. A 
common choice of coordinates is latitude and longitude. With this information we can calculate a distance between two points 
along a surface.

For simplicity’s sake, we will suppose that the Earth is a perfect sphere with a radius of 6,371 kilometers (it gives a mistake 
no more than 0.3%). You are given two point coordinates and you must find the shortest distance between these points on the 
surface of the Earth, measured along the surface of the Earth.

Coordinates are given as a string with the latitude and longitude separated by comma and/or whitespace. Latitude and longitude 
are represented in the follow format:

    d°m′s″X


In this example, "d" is degrees, "m" is minutes, "s" is seconds as integers, while "X" is "N" (north) or "S" (south) for a 
latitude and "W" (west) or "E" (east) for a longitude.

The result should be given as a number in kilometers with a precision of ±0.1 (100 metres).

Input: Two arguments. Coordinates as strings (unicode).

Output: The distance as a number (int or float).

Example:

1. distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E") == 739.2

2. distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W") == 20015.1

How it is used: The concepts presented in this mission are the exact sorts of concepts used in navigational software, enabling 
a ship or plane to understand where it is, where it must go and how far it has gone. Along the same vein, Global Positioning 
Satellites use similar principles to provide pinpoint accurate locations to GPS receivers for use in navigation.

Precondition: Correct Coordinates.
'''


from math import pi, sin, cos, sqrt, atan2
import re
R = 6371


def to_coord(d, m, s):
    L = pi*(float(d) + float(m)/60 + float(s)/3600)/180
    return L
    
def distance(first, second):
    first = first.split(' ')
    if len(first) == 1:
        first = first[0].split(',')
    second = second.split(' ')
    if len(second) == 1:
        second = second[0].split(',')
    d1, m1, s1, g1 = re.search('(\d+)\D(\d+)\D(\d+)\D(\w+)', first[0]).groups()
    d2, m2, s2, g2 = re.search('(\d+)\D(\d+)\D(\d+)\D(\w+)', first[1]).groups()
    x1 = round(to_coord(d1, m1, s1), 6)
    y1 = round(to_coord(d2, m2, s2), 6)
    if g1 == 'S':
        x1 = -x1
    if g2 == 'W':
        y1 = -y1
    d1, m1, s1, g1 = re.search('(\d+)\D(\d+)\D(\d+)\D(\w+)', second[0]).groups()
    d2, m2, s2, g2 = re.search('(\d+)\D(\d+)\D(\d+)\D(\w+)', second[1]).groups()
    x2 = round(to_coord(d1, m1, s1), 6)
    y2 = round(to_coord(d2, m2, s2), 6)
    if g1 == 'S':
        x2 = -x2
    if g2 == 'W':
        y2 = -y2
    y = abs(y1 - y2)
    z1 = (cos(x2)*sin(y))**2 + (cos(x1)*sin(x2) - sin(x1)*cos(x2)*cos(y))**2
    z2 = sin(x1)*sin(x2) + cos(x1)*cos(x2)*cos(y)
    result = atan2(sqrt(z1), z2)*R
    if result == 0.0:
        return pi*R
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(
        distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"
    assert almost_equal(
        distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
    assert almost_equal(
        distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"
        
