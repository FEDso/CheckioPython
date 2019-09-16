"""
To start the game they put several black and white pearls in one of the boxes. Each robot has N moves, after which the initial 
set is being restored for the next game. Each turn, the robot takes a pearl out of the box and puts one of the opposite color 
back. The winner is the one who takes the white pearl on the Nth move.

Our robots don't like uncertainty, that's why they want to know the probability of drawing a white pearl on the Nth move. The 
probability is a value between 0 (0% chance or will not happen) and 1 (100% chance or will happen). The result is a float 
from 0 to 1 with two decimal digits of precision (±0.01).

You are given a start set of pearls as a string that contains "b" (black) and "w" (white) and the number of the move (N). 
The order of the pearls does not matter.

Input: The start sequence of the pearls as a string and the move number as an integer.

Output: The probability for a white pearl as a float. 
"""

def pearls(black, white, step):
    if step == 1:
        return white/(black + white)
    res1 = pearls(black - 1, white + 1, step - 1)*black/(black + white)
    res2 = pearls(black + 1, white - 1, step - 1)*white/(black + white)
    return res1 + res2


def checkio(marbles: str, step: int) -> float:
    black = marbles.count('b')
    white = len(marbles) - black
    return round(pearls(black, white, step), 2)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio('bbw', 3))

    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
