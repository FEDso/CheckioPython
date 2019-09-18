"""
It would seem that it’s a short, brief journey, which should take less than one day - what could go wrong? And yet, when the 
island was already visible on the horizon, suddenly, a terrible storm began! It’s really hard to put into words what you and 
your men went through. Actually… You were the sole survivor who’ve made it to the island alive - the huge waves destroyed both 
ships, and what’s left from their hulls was finally shattered by the sea-cliff. Perhaps, someone else from your crew has managed 
to survive, but it was very unlikely. Now you are facing 2 tasks - to take the Hypercube from the castle and find a way off from 
this damned island.

Let's just take things one step at a time. For starters, you need to find a compass, map and spyglass to navigate the terrain. 
Hurry up! The nature is very unpredictable and if you don’t pick up those things in time, they will be absorbed by the coastal 
sand or washed away into the sea.

Your task is to count the sum of the number of steps required to pick up all 3 items - ('C' - compass), ('M' - map), 
('S' - spyglass) from your starting position. So the result will be the sum of distance from Y to C, from Y to M and from Y 
to S (not Y-C-M-S).
Note that you can walk in 8 directions - left, right, up, down and sideways (on the diagonal in any direction). Your starting 
position is 'Y'.

Input: Array with the objects placements.

Output: The length of the path. 
"""

def distantion(y, v):
    dist_v = max(abs(y[0] - v[0]), abs(y[1] - v[1]))
    return dist_v


def navigation(seaside):
    for i in range(len(seaside)):
        if 'Y' in seaside[i]:
            y = (i, seaside[i].index('Y'))
        if 'C' in seaside[i]:
            c = [i, seaside[i].index('C')]
        if 'M' in seaside[i]:
            m = [i, seaside[i].index('M')]
        if 'S' in seaside[i]:
            s = [i, seaside[i].index('S')]
    dist_c = distantion(y, c)
    dist_m = distantion(y, m)
    dist_s = distantion(y, s)
    return int(dist_c + dist_m + dist_s)
    

if __name__ == '__main__':
    print("Example:")
    print(navigation([['Y', 0, 0, 0, 'C'],
                      [ 0,  0, 0, 0,  0],
                      [ 0,  0, 0, 0,  0],
                      ['M', 0, 0, 0, 'S']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert navigation([['Y', 0, 0, 0, 'C'],
                       [ 0,  0, 0, 0,  0],
                       [ 0,  0, 0, 0,  0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[ 0,  0, 'C'],
                       [ 0, 'S', 0],
                       ['M','Y', 0]]) == 4

    assert navigation([[ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'M', 0, 'S', 0],
                       [ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'C', 0,  0,  0],
                       [ 0, 'Y',0,  0,  0,  0,  0],
                       [ 0,  0, 0,  0,  0,  0,  0]]) == 9
    print("Coding complete? Click 'Check' to earn cool rewards!")
