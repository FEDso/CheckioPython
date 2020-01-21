"""
 You are given two strings, line1 and line2. Answer, what is the smallest number of operations you need to transform line1 to 
 line2?

Operations are:

    Delete one letter from one of strings
    Insert one letter into one of strings
    Replace one of letters from one of strings with another letter

Input: two arguments, two strings.

Output: int, minimum number of operations.

Example:

  steps_to_convert('line1', 'line1') == 0

  steps_to_convert('line1', 'line2') == 1

  steps_to_convert('ine', 'line2') == 2


Precondition: 0 <= len(line) < 100 
"""

def steps_to_convert(line1, line2):
    n1, n2 = len(line1), len(line2)
    NW = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for i in range (n1+1):
        NW[i][0] = 0
    for k in range(n2 + 1):
        NW[0][k] = 0
    
    for i in range(1, n1 + 1):
        for k in range(1, n2 + 1):
            if line1[i-1] == line2[k-1]:
                NW[i][k] = NW[i-1][k-1] + 1
            else:
                match = NW[i-1][k-1] + 1 
                delete = NW[i-1][k]
                insert = NW[i][k-1]
                NW[i][k] = max(insert, delete)
    return max(n1, n2) - NW[-1][-1]


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert steps_to_convert('line1', 'line1') == 0, "eq"
    assert steps_to_convert('line1', 'line2') == 1, "2"
    assert steps_to_convert('line', 'line2') == 1, "none to 2"
    assert steps_to_convert('ine', 'line2') == 2, "need two more"
    assert steps_to_convert('line1', '1enil') == 4, "everything is opposite"
    assert steps_to_convert('', '') == 0, "two empty"
    assert steps_to_convert('l', '') == 1, "one side"
    assert steps_to_convert('', 'l') == 1, "another side"
    print("You are good to go!")
