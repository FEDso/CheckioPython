def clock_angle(time):
    hour, minutes = map(int, time.split(':'))
    return min(abs((hour%12 + minutes/60)*30 - minutes*6), 360 - abs((hour%12 + minutes/60)*30 - minutes*6))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"
    print('Ok')
    