"""
Stephen's speech module is broken. This module is responsible for his number pronunciation. He has to click to input all of 
the numerical digits in a figure, so when there are big numbers it can take him a long time. Help the robot to speak properly 
and increase his number processing speed by writing a new speech module for him. All the words in the string must be separated 
by exactly one space character. Be careful with spaces -- it's hard to see if you place two spaces instead one.

Input: A number as an integer.

Output: The string representation of the number as a string.
"""

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    number = str(number)
    if len(number) == 1:
        return FIRST_TEN[int(number)-1]
    if len(number) == 2:
        if number[0] == '1':
            return SECOND_TEN[int(number)-10]
        elif number[1] == '0':
            return OTHER_TENS[int(number[0])-2]
        else:
            return (OTHER_TENS[int(number[0])-2] + ' ' + 
                                  FIRST_TEN[int(number[1])-1])
    hundr = FIRST_TEN[int(number[0])-1] + ' ' + HUNDRED
    if number[1:] == '00':
        return hundr
    if number[1] == '0':
        return hundr + ' ' + FIRST_TEN[int(number[2])-1]
    if number[1] == '1':
        return hundr + ' ' + SECOND_TEN[int(number[1:])-10]
    if number[2] == '0':
        return hundr + ' ' + OTHER_TENS[int(number[1])-2]
    return (hundr + ' ' + OTHER_TENS[int(number[1])-2] + ' ' + 
            FIRST_TEN[int(number[2])-1])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(12) == 'twelve', "2nd example"
    assert checkio(133) == 'one hundred thirty three', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
    
