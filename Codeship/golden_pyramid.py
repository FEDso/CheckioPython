def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    ways = [[0 for _ in i]for i in pyramid]
    ways[-1] = [i for i in pyramid[-1]]
    for i in range(len(pyramid)-2, -1, -1):
        for k in range(len(pyramid[i])):
            ways[i][k] = pyramid[i][k] + max(ways[i+1][k], ways[i+1][k+1])
    return ways[0][0]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
    assert count_gold((
        (2,),
        (7,9),
        (0,8,6),
        (4,7,6,8),
        (0,5,5,4,1),
        (9,1,0,1,6,9)
    )) == 35, "Forth example"
    print('All tests passed!')
    