"""
There are four substring missions that were born all in one day and you shouldn’t be needed more than one day to solve them. 
All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to 
all of those missions yet, but they are going to be available with more opened islands on the map).

This is the third mission of the series, and it’s the only one where you have to return not a substring but a substring length. 
You need to find a substring that repeats more than once in a given string. This reiteration shouldn't have overlaps. For 
example, in a string "abcab" the longest substring that repeats more than once is "ab", so the answer should 
be 2 (length of "ab")

Input: String.

Output: Int. 
"""

import re

def double_substring(line):
    n = len(line)//2
    while n > 0:
        k = 0
        while k + n <= len(line):
            pattern = line[k:k+n]
            if re.search(pattern, line[k+n:]):
                return n
            k += 1
        n -= 1
    return n

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')
    
