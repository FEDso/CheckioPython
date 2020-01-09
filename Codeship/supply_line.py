import string

def neighbors(field, k):
    neighbors_list = []
    t = k[0] + str(int(k[1])+1)
    if t[0] in string.ascii_uppercase[:12] and t[1] in string.digits[1:] and t in field:
        neighbors_list.append(t)
    t = k[0] + str(int(k[1])-1)
    if t[0] in string.ascii_uppercase[:12] and t[1] in string.digits[1:] and t in field:
        neighbors_list.append(t)
    t = chr(ord(k[0])-1) + k[1]
    if t[0] in string.ascii_uppercase[:12] and t[1] in string.digits[1:] and t in field:
        neighbors_list.append(t)
    t = chr(ord(k[0])+1) + k[1]
    if t[0] in string.ascii_uppercase[:12] and t[1] in string.digits[1:] and t in field:
        neighbors_list.append(t)
    if k[0] in string.ascii_uppercase[::2]:
        s = -1
    else:
        s = 1
    t = chr(ord(k[0])-1)+str(int(k[1])+s)
    if t[0] in string.ascii_uppercase[:12] and t[1] in string.digits[1:] and t in field:
        neighbors_list.append(t)
    t = chr(ord(k[0])+1)+str(int(k[1])+s)
    if t[0] in string.ascii_uppercase[:12] and t[1] in string.digits[1:] and t in field:
        neighbors_list.append(t)
    return neighbors_list


def supply_line(you, depots, enemies):
    if you in depots:
        return 0
    field = {i + str(k+1): 10000
             for i in {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'} 
             for k in range(9)}
    for e in enemies:
        for k in neighbors(field, e):
            del field[k]
        if e in field:
            del field[e]
    for d in set(depots):
        if d not in field:
            depots.remove(d)
    if not depots:
        return None
    field[you] = 0
    neighbor = {}
    for f in field:
        neighbor[f] = neighbors(field, f)
    active = {you}
    for _ in range(len(field)**2):
        f = False
        tmp = set()
        for a in active:
            for k in neighbor[a]:
                if field[a] + 1 < field[k]:
                    field[k] = field[a] + 1
                    f = True
                tmp.add(k)
        active |= tmp
        if not f:
            break
    steps = 10000
    for d in depots:
        if field[d] < steps:
            steps = field[d]
    if steps == 10000:
        return None
    print(steps)
    return steps


if __name__ == '__main__':
    assert supply_line("B4", {"F4"}, {"D4"}) == 6, 'simple'
    assert supply_line("A3", {"A9", "F5", "G8"}, {"B3", "G6"}) == 11, 'multiple'
    assert supply_line("C2", {"B9", "F6"}, {"B7", "E8", "E5", "H6"}) is None, 'None'
    assert supply_line("E5", {"C2", "B7", "F8"}, set()) == 4, 'no enemies'
    assert supply_line("A5", {"A2", "B9"}, {"B3", "B7", "E3", "E7"}) == 13, '2 depots'
    print('"Run" is good. How is "Check"?')
