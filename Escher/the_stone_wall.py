"""
 Finding the castle with a map and a compass was a piece of cake. Moreover, when you’ve inspected the surroundings through the 
 spyglass, you spotted a small sailing yacht a few kilometers from the place where you were washed ashore. It has probably 
 belonged to other treasure hunters who have failed to leave the island. After checking it out you’ve came to a conclusion 
 that yacht is in a pretty good shape and with the fair-wind you’ll have no problems returning home. Well, in any case, you’ll 
 have less problems - now you just have to find the Cube.

As I’ve said before, the lord who used to live here, highly appreciated the solitude, therefore it’s not surprising that the 
estate was surrounded by a very high and thick stone wall. Fortunately, you’ve foreseen this and took some explosives with 
you (I don’t even want to know where you got it from). However, it’s unlikely that this modest reserve will suffice to blow 
up the wall just anywhere - it’d be better to act for sure and find the most vulnerable place.

As input you'll get a multiline string consists of '0' and '#' - a view of a stone wall from above. The '#' will show the stone 
part of the wall and the '0' will show the empty part. The relative location of you and the wall is as follows: you look at the 
array from the bottom of it.
Your task is to find the index of the place where the wall is the narrowest (as shown at the picture below). The width of the 
wall is the height of the columns of the array (multiline string). If there are several such places, return the index of 
leftmost. Index starts from 0.

Input: Array represents the stone wall.

Output: Index of leftmost of all weakest spots. 
"""

def stone_wall(wall):
    wall = wall.split()
    n = len(wall)
    p, k = 100, 100
    
    for i in range(len(wall[0])):
        t = 0
        for j in range(n):
            if wall[j][i] == '#':
                t += 1
        if t < p:
            p, k = t, i
    return k

if __name__ == '__main__':
    print("Example:")
    print(stone_wall('''
##########
####0##0##
00##0###00
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert stone_wall('''
##########
####0##0##
00##0###00
''') == 4

    assert stone_wall('''
#00#######
#######0##
00######00
''') == 1

    assert stone_wall('''
#####
#####
#####
''') == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")

