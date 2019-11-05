"""
Write a function that finds the longest palindromic substring of a given string. Try to be as efficient as possible!

If you find more than one substring, you should return the one that’s closer to the beginning.

Input: A text as a string.

Output: The longest palindromic substring.

Examples:
  longest_palindromic('abc') == 'a'
  longest_palindromic('abacada') == 'aba'

Precondition: 1 < |text| ≤ 20
The text contains only ASCII characters.
"""


def longest_palindromic(a):
    if len(a) == 1:
        return a
    if len(a) == 2:
        if a[0] == a[1]:
            return a
        else:
            return a[0]
    palindrom = [0, 1, 1]
    left, right = 0, 2
    start = 1
    while start != len(a) - 1:
        if a[left] == a[right]:
            if right - left + 1 > palindrom[2]:
                palindrom[2] = right - left + 1
                palindrom[0] = left
                palindrom[1] = right + 1
            if left - 1 >= 0 and right + 1 < len(a):
                left -= 1
                right += 1
            else:
                start += 1
                left, right = start - 1, start + 1      
        else:
            start += 1
            left, right = start - 1, start + 1      
    return a[palindrom[0]:palindrom[1]]


if __name__ == '__main__':
    print("Example:")
    print(longest_palindromic('abc'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert longest_palindromic('abc') == 'a'
    assert longest_palindromic('abacada') == 'aba'
    assert longest_palindromic('artrartrt') == 'rtrartr'
    assert longest_palindromic('aaaaa') == 'aaaaa'
    print("Coding complete? Click 'Check' to earn cool rewards!")
