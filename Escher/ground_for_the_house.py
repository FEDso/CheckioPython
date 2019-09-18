"""
It was a long trip to the island, so you’ve decided to pass the time sitting in the captain's cabin and splitting the treasures 
remained to be found. Aside from that, a couple of weeks before you left for the expedition, you’ve managed to negotiate with 
several very wealthy people and approximately knew how much you could get by selling the Hypercube.

Purchasing land in a picturesque place have been one of your long-held wishes. You’ve dreamed of building a house there and 
breeding the rare species. All of this requires a considerable amount of money that are likely to come into your possession in 
the near future.

As the input data you will get the multiline string consists of '0' & '#'. where '0' means the empty piece of the ground and 
the '#' is the piece of your house. Your task is to count the minimal area of the rectangle ground which is enough for the 
building.

Input: The plan of the house.

Output: The total area of the rectangle piece of the ground. 
"""


def house(plan):
    if '#' not in plan:
        return 0
    plan = plan.split()
    n1, n2, m1, m2 = (1000, -1000, 1000, -1000)
    for i in range(len(plan)):
        if '#' in plan[i]:
            n1 = min(n1, i)
            n2 = max(n2, i)
        for k in range(len(plan[0])):
            if plan[i][k] == '#':
                m1 = min(m1, k)
                m2 = max(m2, k)
    return (n2 + 1 - n1)*(m2 + 1 - m1)
    

if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
