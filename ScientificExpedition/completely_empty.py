def completely_empty(val):
    result = True
    for v in val:
        if not v and v not in (0, None):
            continue
        try:
            _ = iter(v)
            result &= completely_empty(v)
        except TypeError as te:
            result &= False            
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert completely_empty([]) == True, "First"
    assert completely_empty([1]) == False, "Second"
    assert completely_empty([[]]) == True, "Third"
    assert completely_empty([[],[]]) == True, "Forth"
    assert completely_empty([[[]]]) == True, "Fifth"
    assert completely_empty([[],[1]]) == False, "Sixth"
    assert completely_empty([0]) == False, "[0]"
    assert completely_empty(['']) == True
    assert completely_empty([[],[{'':'No WAY'}]]) == True
    print('Done')
