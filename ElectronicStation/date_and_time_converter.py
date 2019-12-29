months = ['January', 'Febrary', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']

def del_zero(s):
    if s[0] == '0':
        return s[1:]
    return s


def date_time(time: str) -> str:
    time = time.split()
    date = time[0].split('.')
    time = time[1].split(':')
    for i in range(3):
        date[i] = del_zero(date[i])
    time[0] = del_zero(time[0])
    time[1] = del_zero(time[1])    
    date =  [date[0], months[int(date[1])-1], date[2], 'year']
    tmp =  [time[0]]
    if time[0] == '1':
        tmp.append('hour')
    else:
        tmp.append('hours')
    tmp.append(time[1])
    if time[1] == '1':
        tmp.append('minute')
    else:
        tmp.append('minutes')
    return ' '.join([*date, *tmp])


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
