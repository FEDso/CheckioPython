"""
 Going up to the door you’ve noticed the case that was standing next to it - it was piled high with the keys of all shapes and s
 izes. Yes, Lord Escher definitely loved puzzles and difficulties. When you’ve attempted to open the door, you discovered with no 
 particular surprise that it was closed. Well, let's find the right key and move on.

As input you are getting two multi-line strings - one is a schematic image of the keyhole, the second - of the key. Your task is 
to return True if the key fits the lock and False if otherwise. The key and keyhole are represented by the '#' symbols, and '0' 
shows the empty space around the key and the door material around the keyhole. Pay attention that the key and keyhole can be 
displayed both vertically and horizontally.

Input: The key and lock representation as multilines string.

Output: True or False. 
"""

import numpy as np

#------------------------------------------------------------------------------#

def del_str(s):
    for i in range(len(s)):
        if '#' in s[i]:
            break
    for k in range(len(s) - 1, -1, -1):
        if '#' in s[k]:
            break
    return s[i:k+1]
        
#------------------------------------------------------------------------------#

def del_zero(scheme):
    scheme = [[i for i in s] for s in scheme.split()]
    scheme = np.array(scheme)
    for _ in range(2):
        scheme = del_str(scheme)
        scheme = scheme.swapaxes(0, 1)
    return scheme
    
#------------------------------------------------------------------------------#

def keys_and_locks(lock, some_key):
    lock = del_zero(lock)
    some_key = del_zero(some_key)
    for _ in range(2):
        for _ in range(2):
            if np.array_equal(lock, some_key):
                return True
            some_key = some_key.swapaxes(0, 1)
        some_key = some_key[::-1]
    return False

#------------------------------------------------------------------------------#

if __name__ == '__main__':
    print("Example:")
    print(keys_and_locks('''   
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000''') == True

    assert keys_and_locks('''
###0
00#0''',
'''
00000
00000
#0000
###00
0#000
0#000''') == False

    assert keys_and_locks('''
0##0
0#00
0000''',
'''
##000
#0000
00000
00000
00000''') == True

    assert keys_and_locks('''
###0
0#00
0000''',
'''
##00
##00''') == False

    print("Coding complete? Click 'Check' to earn cool rewards!")
