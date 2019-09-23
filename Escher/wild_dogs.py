"""
 The dust from the blast has shraded away and you entered the grounds of the estate. But what is that piercing howl you’re 
 hearing from afar? By taking a closer look you’ve realized that a small pack of huge black shaggy dogs, looking more like 
 wolves, are headed your way. These are probably the wild offsprings of the guard dogs who’ve used to protect the castle from 
 the unwanted visitors. The good news is that you have a rifle. The bad news is that you don’t have a lot of bullets. Therefore, 
 your survival depends on finding the best vantage point for shooting. Choose your location wisely and try to make each shot 
 count.

As input you’ll be given the coordinates of the dogs. Your task is to find the distance to the nearest point from which you can 
kill the maximum number of animals with one shot (any number of dogs on the same line can be killed with one shot). Your 
starting position is the point (0, 0).

If the calculated distance is an integer, return it as int, otherwise round it to 2 decimal places.
Don't worry about the situation when a few dogs on the line is behind your back (dog dog you dog) - there no such situation in 
the tests.

Input: list of coordinates (tuple of two integers/float) of the dogs.

Output: distance to the best spot. 
"""

from itertools import combinations

def comb_two_points(coords):
    nums = [i for i in range(len(coords))]
    points = []
    for coord in list(combinations(nums, 2)):
        points.append([coords[coord[0]], coords[coord[1]]])
    return points

#------------------------------------------------------------------------------#

def is_one_line(coords, points):
    for i in range(len(points)):
        if (points[i][1][0] - points[i][0][0]) != 0:
            k = (points[i][1][1] - points[i][0][1])/(points[i][1][0] - points[i][0][0])
            c = points[i][0][1] - k*points[i][0][0]
            for point in coords:                
                if point not in points[i] and point[1] == k*point[0] + c:
                    points[i].append(point)
    return points

#------------------------------------------------------------------------------#

def wild_dogs(coords):
    points = comb_two_points(coords)
    points = is_one_line(coords, points)
    m = len(max(points, key=lambda x: len(x)))
    res = 1000000
    for point in points:
        if len(point) == m:
            point.sort()
            a = (point[1][1] - point[0][1])/(point[1][0] - point[0][0])
            b = point[1][1] - a*point[1][0]
            x = -(a*b/(1 + a**2))
            y = b - (a**2*b/(1 + a**2))
            r = round((x**2 + y**2)**0.5, 2)
            if r < res:
                res = r                
    return res

#------------------------------------------------------------------------------#

if __name__ == '__main__':
    print("Example:")
    print(wild_dogs([(1, 4), (2, 6), (3, 8), (11, 0)]))
    print()
    print()
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert wild_dogs([(7, 122), (8, 139), (9, 156), 
                      (10, 173), (11, 190), (-100, 1)]) == 0.18

    assert wild_dogs([(10, 10), (13, 13), (21, 18)]) == 0
    
    assert wild_dogs([(6, -0.5), (3, -5), (1, -20)]) == 3.63


    print("Coding complete? Click 'Check' to earn cool rewards!")
