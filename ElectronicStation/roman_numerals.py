"""
 Roman numerals come from the ancient Roman numbering system. They are based on specific letters of the alphabet which are 
 combined to signify the sum (or, in some cases, the difference) of their values. The first ten Roman numerals are:

I, II, III, IV, V, VI, VII, VIII, IX, and X.

The Roman numeral system is decimal based but not directly positional and does not include a zero. Roman numerals are based 
on combinations of these seven symbols:
Numeral	Value
I	1 (unus)
V	5 (quinque)
X	10 (decem)
L	50 (quinquaginta)
C	100 (centum)
D	500 (quingenti)
M	1,000 (mille)

More additional information about roman numerals can be found on the Wikipedia article.

For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.

Input: A number as an integer.

Output: The Roman numeral as a string. 
"""

roman_nums = {'1': 'I', '5': 'V', '10': 'X', '50': 'L', 
              '100': 'C', '500': 'D', '1000': 'M'}

def checkio(data):
    roman_num = ''
    data = str(data)
    for i in range(len(data)):
        if data[-1-i] == 0:
            continue
        n = int(str(data[-1-i]))
        if n < 4:
            roman_num += roman_nums[str(10**i)]*n
        elif n >= 5 and n < 9:
            roman_num += roman_nums[str(10**i)]*(n-5)
            roman_num += roman_nums[str(5*10**i)]
        elif n == 9:
            roman_num += roman_nums[str(10**(i+1))]
            roman_num += roman_nums[str(10**i)]
        elif n == 4:
            roman_num += roman_nums[str(5*10**i)]
            roman_num += roman_nums[str(10**i)]
    return roman_num[::-1]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
    
    
