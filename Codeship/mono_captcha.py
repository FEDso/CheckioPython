from typing import List

FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--"
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-"
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-"
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-"
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")

segment = {0: (37,40), 1: (1, 4), 2: (5, 8), 3: (9, 12), 4: (13, 16), 
           5: (17, 20), 6: (21, 24), 7: (25, 28), 8: (29, 32), 9: (33, 36)}


def hamming(s1, s2):
    return sum([1 if s1[i] != s2[i] else 0 for i in range(len(s1))])


def checkio(image: List[List[int]]) -> int:
    n = len(image[0])
    m = (n - 1)//4
    result = 0
    for i in range(len(image)):
        image[i] = list(map(str, image[i]))
        image[i] = ''.join(image[i]).replace('1', 'X')
        image[i] = image[i].replace('0', '-')
    image = ''.join(image)
    for i in range(m):
        for k in range(10):
            font_num = ''.join([FONT[segment[k][0]+j*41:segment[k][1]+j*41] for j in range(5)])
            num = ''.join([image[j*n+1+4*i:j*n+1+4*i+3] for j in range(5)])
            if hamming(num, font_num) < 2:
                result += k*10**(m-i-1)
                break

    return result


if __name__ == '__main__':
    print("Example:")
    print(checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                   [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                   [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                   [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"
    print("Coding complete? Click 'Check' to earn cool rewards!")
