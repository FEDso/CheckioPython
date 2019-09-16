"""
 In mathematics, particularly in linear algebra, a skew-symmetric matrix (also known as an antisymmetric or antimetric) is 
 a square matrix A which is transposed and negative. This means that it satisfies the equation A = −AT. If the entry in the 
 i-th row and j-th column is aij, i.e. A = (aij) then the symmetric condition becomes aij = −aji.

You should determine whether the specified square matrix is skew-symmetric or not.

You can find more details on Skew-symmetric matrices on its Wikipedia page.

Input: A square matrix as a list of lists with integers.

Output: If the matrix is skew-symmetric or not as a boolean. 
"""

import numpy as np

def checkio(matrix):
    A = np.array(matrix)
    At = A.transpose()
    return np.array_equal(At, -A)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]))

    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
    print("Coding complete? Click 'Check' to earn cool rewards!");
