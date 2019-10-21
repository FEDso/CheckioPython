"""
Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.

Find the number of Friday 13th in the given year.

Input: Year as an integer.

Output: Number of Black Fridays in the year as an integer.

Example:

checkio(2015) == 3

checkio(1986) == 1


Precondition: 1000 < |year| < 3000

"""

import calendar

def checkio(year: int) -> int:
    count = 0
    for month in range(12):
        if calendar.weekday(year, month + 1, 13) == 4:
            count += 1
    return count


if __name__ == '__main__':
    print("Example:")
    print(checkio(2015))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
    print("Coding complete? Click 'Check' to earn cool rewards!")
