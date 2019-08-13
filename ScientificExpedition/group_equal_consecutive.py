"""
 Given a list of elements, create and return a list whose elements are lists that contain the consecutive runs of equal elements 
 of the original list. Note that elements that aren’t duplicated in the original list should become singleton lists in the result, 
 so that every element gets included in the resulting list of lists.

Input: List of str and int.

Output: List of lists of str and int 
"""

def group_equal(els):
    if els == []:
        return els
    result = []
    tmp = []
    now = els[0]
    for e in els: 
        if e == now:
            tmp.append(now)
        else:
            result.append(tmp)
            tmp = [e,]
            now = e
    result.append(tmp)
    return result


if __name__ == '__main__':
    print("Example:")
    print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1,1],[4,4,4],["hello","hello"],[4]]
    assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    assert group_equal([1]) == [[1]]
    assert group_equal([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")

