"""
 You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits. The sequence may 
 be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).

Input: A matrix as a list of lists with integers.

Output: Whether or not a sequence exists as a boolean.

How it is used: This concept is useful for games where you need to detect various lines of the same elements (match 3 games for 
example). This algorithm can be used for basic pattern recognition.

Precondition:
0 ≤ len(matrix) ≤ 10
all(all(0 < x < 10 for x in row) for row in matrix) 
"""

def checkio(matrix):
    for i in range(len(matrix)):
        for k in range(len(matrix[0])):
            if k < len(matrix[0]) - 3 and matrix[i][k] == matrix[i][k+1] == matrix[i][k+2] == matrix[i][k+3]:
                return True

            if i < len(matrix) - 3 and matrix[i][k] == matrix[i+1][k] == matrix[i+2][k] == matrix[i+3][k]:
                return True
            if i < len(matrix) - 3 and k < len(matrix[0]) - 3 and\
               matrix[i][k] == matrix[i+1][k+1] == matrix[i+2][k+2] == matrix[i+3][k+3]:
                    return True
            if i < len(matrix) - 3 and k > len(matrix[0]) - 3 and\
               matrix[i][k] == matrix[i+1][k-1] == matrix[i+2][k-2] == matrix[i+3][k-3]:
                    return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    
    assert checkio([[2,6,2,2,7,6,5],
                    [3,4,8,7,7,3,6],
                    [6,7,3,1,2,4,1],
                    [2,5,7,6,3,2,2],
                    [3,4,3,2,7,5,6],
                    [8,4,6,5,2,9,7],
                    [5,8,3,1,3,7,8]]) == False, 'test'
                    
    assert checkio([[6,9,1,1,6,2],
                    [5,9,7,8,2,5],
                    [2,1,1,7,9,8],
                    [1,8,1,4,7,4],
                    [7,8,5,4,5,1],
                    [6,4,8,8,1,8]]) == False, 'test2'
    print('All tests passed!')
