"""


What’s your favourite day of the week? Check if it's the most common day of the week in a year.

You are given a year as an integer (e. g. 2001). You should return the most frequent day(s) of the week in that particular year. 
The result has to be a list of days sorted by the order of days in a week (e. g. ['Monday', 'Tuesday']). Week starts with Monday.

Input: Year as an int.

Output: The list of most common days sorted by the order of days in a week (from Monday to Sunday).

Example:

most_frequent_days(1084) == ['Tuesday', 'Wednesday']

most_frequent_days(1167) == ['Sunday']

Preconditions: Year is between 1 and 9999. Week starts with Monday.

"""

import calendar

week_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
month_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

def most_frequent_days(year):
    days_count = [0 for i in range(7)]
    for m in range(len(month_days)):
        for d in range(month_days[m]):
            days_count[calendar.weekday(year, m + 1, d + 1)] += 1
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        days_count[calendar.weekday(year, 2, 29)] += 1
    m = max(days_count)
    result = []
    for i in range(7):
        if days_count[i] == m:
            result.append(week_days[i])
    return result


if __name__ == '__main__':
    print("Example:")
    print(most_frequent_days(1084))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert most_frequent_days(1084) == ['Tuesday', 'Wednesday']
    assert most_frequent_days(1167) == ['Sunday']
    assert most_frequent_days(1216) == ['Friday', 'Saturday']
    
    assert most_frequent_days(1492) == ['Friday', 'Saturday']
    assert most_frequent_days(1770) == ['Monday']
    assert most_frequent_days(1785) == ['Saturday']
    assert most_frequent_days(212) == ['Wednesday', 'Thursday']
    assert most_frequent_days(1) == ['Monday']
    assert most_frequent_days(2135) == ['Saturday']
    assert most_frequent_days(3043) == ['Sunday']
    assert most_frequent_days(2001) == ['Monday']
    assert most_frequent_days(3150) == ['Sunday']
    assert most_frequent_days(3230) == ['Tuesday']
    assert most_frequent_days(328) == ['Monday', 'Sunday']
    assert most_frequent_days(2016) == ['Friday', 'Saturday']
    print("Coding complete? Click 'Check' to earn cool rewards!")
