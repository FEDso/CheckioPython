import types

def min(*args, **kwargs):
    if len(args) == 1:
        args = list(args[0])
    if not kwargs:
        kwargs = lambda x: x
    else:
        kwargs = kwargs['key']
    result = args[0]
    tmp = kwargs(args[0]) if kwargs else args[0]
    for arg in args:
        if kwargs(arg) < tmp:
            result = arg
            tmp = kwargs(arg)
    return result


def max(*args, **kwargs):
    if len(args) == 1:
        args = list(args[0])
    if not kwargs:
        kwargs = lambda x: x
    else:
        kwargs = kwargs['key']
    result = args[0]
    tmp = kwargs(args[0]) if kwargs else args[0]
    for arg in args:
        if kwargs(arg) > tmp:
            result = arg
            tmp = kwargs(arg)
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
