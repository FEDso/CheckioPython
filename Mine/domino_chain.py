def domino_chain_search(dominos, now, n):
    nums = 0
    if n == 1:
        if now == dominos[0][0]:
            nums += 1
        if dominos[0][1] == dominos[0][0]:
            return nums
        elif now == dominos[0][1]:
            nums += 1
        return nums
    for i in range(len(dominos)):
        if dominos[i][0] == now:
            nums += domino_chain_search(dominos[0:i] + dominos[i+1:], dominos[i][1], n - 1)
        if dominos[i][1] == dominos[i][0]:
            continue
        if dominos[i][1] == now:
            nums += domino_chain_search(dominos[0:i] + dominos[i+1:], dominos[i][0], n - 1)
    return nums


def domino_chain(tiles: str) -> int:
    dominos = tiles.split(', ')
    for i in range(len(dominos)):
        dominos[i] = dominos[i].split('-')
    nums = 0
    for i in range(len(dominos)):
        nums += domino_chain_search(dominos[0:i] + dominos[i+1:], dominos[i][1], len(dominos) - 1)
        if dominos[i][1] == dominos[i][0]:
            continue
        nums += domino_chain_search(dominos[0:i] + dominos[i+1:], dominos[i][0], len(dominos) - 1)        
    return nums//2


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert domino_chain("0-2, 0-5, 1-5, 1-3, 5-5") == 1
    assert domino_chain("1-5, 2-5, 3-5, 4-5, 3-4") == 2
    assert domino_chain("0-5, 1-5, 2-5, 3-5, 4-5, 3-4") == 0
    assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4") == 6
    assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4, 3-0, 0-4") == 0
    assert domino_chain("1-2, 2-2, 2-3, 3-3, 3-1") == 5
    assert domino_chain("1-4, 3-4, 0-4, 0-5, 4-5, 2-4, 2-5") == 0
    assert domino_chain("1-4, 1-5, 0-2, 1-6, 4-6, 4-5, 5-6") == 0
    assert domino_chain("1-2, 2-3, 2-4, 3-4, 2-5, 2-6, 5-6") == 8
    assert domino_chain("1-2, 2-3, 3-1, 4-5, 5-6, 6-4") == 0
    assert domino_chain("1-2, 1-4, 1-5, 1-6, 1-1, 2-5, 4-6") == 28
    print("Basic tests passed.")
    print(domino_chain("0-0, 4-6, 5-6, 1-4, 0-6, 0-5, 1-6, 0-4, 2-2, 0-3, 3-4"))
