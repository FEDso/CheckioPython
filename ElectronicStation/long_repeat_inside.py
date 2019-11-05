"""
 It is the fourth and the last mission of the series. But if in the first mission you needed to find repeating letters, then in 
 this one you should find a repeating sequence inside the substring. I have an example for you: in a string "abababc" - "ab" is a 
 sequence that repeats more than once, so the answer will be "ababab"

Input: String.

Output: String.

Example:
  repeat_inside('aaaaa') == 'aaaaa'
  repeat_inside('aabbff') == 'aa'
  repeat_inside('aababcc') == 'abab'
  repeat_inside('abc') == ''
  repeat_inside('abcabcabab') == 'abcabc'
"""

import re

def repeat_inside(line):
    result = re.findall(r'(?=((\w+?)\2+))', line)
    result = max((r[0] for r in result), key=len, default='')
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')
