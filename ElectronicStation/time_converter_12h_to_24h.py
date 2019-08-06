"""
You are the modern man who prefers the 24-hour time format. But the 12-hour format is used in some places. Your task is to 
convert the time from the 12-h format into 24-h by following the next rules:
- the output format should be 'hh:mm'
- if the output hour is less than 10 - write '0' before it. For example: '09:05'
Here you can find some useful information about the 12-hour format.


Input: Time in a 12-hour format (as a string).

Output: Time in a 24-hour format (as a string). 
"""

def time_converter(time):
    if time[-4] == 'a':
        if time[:2] == '12':
            return '00' + time[2:5]
        if time[1] == ':':
            return '0' + time[:4]
        return time[:5]
    else:
        if time[:2] == '12':
            return time[:5]
        if time[1] == ':':
            return str(int(time[0])+ 12) + time[1:4]
        return str(int(time[:2]) +pĺ 12) + time[2:5]

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
    
