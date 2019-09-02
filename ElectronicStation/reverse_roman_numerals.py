"""
You are given a Roman number as a string and your job is to convert this number into its decimal representation.

A valid Roman number, in the context of this mission, will only contain Roman numerals as per the below table and follow the 
rules of the subtractive notation.
Numeral	Value
I	1 (unus)
V	5 (quinque)
X	10 (decem)
L	50 (quinquaginta)
C	100 (centum)
D	500 (quingenti)
M	1,000 (mille)

Input: A roman number as a string.

Output: The decimal representation of the roman number as an int. 
"""

roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
              'C': 100, 'D': 500, 'M': 1000}


def reverse_roman(roman):
    arab = 0 
    for i in range(len(roman) - 1): 
        r = roman_nums[roman[i]]
        if roman_nums[roman[i+1]] > r:
           arab -= r
        else:
            arab += r
    arab += roman_nums[roman[-1]]
    return arab
         

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');
    
