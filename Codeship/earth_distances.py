from math import pi
R = 6371
dd = 1852.4*60
mm = 1852.4
ss = 1852.4/60


def d_to_km(d):
    return pi*R*d/180


def distance(first, second):
    first = first.split(' ')
    second = second.split(' ')
    d, m, s = first[0].index('°'), first[0].index('′'), first[0].index('″')
    xd1 = d_to_km(int(first[0][:d]))
    xm1, xs1 = 60*d_to_km(int(first[0][d+1:m])) + R, d_to_km(int(first[0][m+1:s]))/3600
    d, m, s = first[1].index('°'), first[1].index('′'), first[1].index('″')
    yd1 = d_to_km(int(first[1][:d]))
    ym1, ys1 = 60*d_to_km(int(first[1][d+1:m])) + R, d_to_km(int(first[1][m+1:s]))/3600
    d, m, s = second[0].index('°'), second[0].index('′'), second[0].index('″')
    xd2, xm2, xs2 = d_to_km(dd*int(second[0][:d])), d_to_km(int(second[0][d+1:m]))/60, d_to_km(int(second[0][m+1:s]))/3600
    d, m, s = second[1].index('°'), second[1].index('′'), second[1].index('″')
    yd2, ym2, ys2 = d_to_km(dd*int(second[1][:d])), d_to_km(int(second[1][d+1:m]))/60, d_to_km(int(second[1][m+1:s]))/3600
    result = ((xd1 + xm1 + xs1) - (xd2 + xm2 + xs2))**2 + ((yd1 + ym1 + ys1) - (yd2 + ym2 + ys2))**2
    print((result/1000)**(0.5))
    return result**(0.5)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(
        distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"
    assert almost_equal(
        distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
    assert almost_equal(
        distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"
