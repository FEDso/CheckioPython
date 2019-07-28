"""
There are four substring missions that were born all in one day and you shouldn’t be needed more than one day to solve them. 
All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to 
all of those missions yet, but they are going to be available with more opened islands on the map).

This mission is the first one of the series. Here you should find the length of the longest substring that consists of the same 
letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". The last 
substring is the longest one which makes it an answer.

Input: String.

Output: Int. 
"""

def long_repeat(line):
"""
    length the longest substring that consists of the same char
"""
    if line == "": 
        return 0
    max_counts, counts = 1, 1 
    now = line[0]
    for i in line[1:]:
        if now == i:
            counts += 1
        else:
            max_counts = counts if max_counts < counts else max_counts
            counts = 1 
            now = i 
    max_counts = counts if max_counts < counts else max_counts
    return max_counts
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
 
