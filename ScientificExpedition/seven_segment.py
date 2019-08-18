"""
 You have a device that uses a Seven-segment display to display 2 digit numbers. However, some of the segments aren't working 
 and can't be displayed.

You will be given information on the lit and broken segments. You won't know whether the broken segment is lit or not. You have 
to count and return the total number that the device may be displaying.

The input is a set of lit segments (the first argument) and broken segments (the second argument).

    Uppercase letters represent the segments of the first out two digit number.
    Lowercase letters represent the segments of the second out two digit number.
    topmost: 'A(a)', top right: 'B(b)', bottom right: 'C(c)', bottommost: 'D(d)', bottom left: 'E(e)', top left: 'F(f)', 
    middle: 'G(g)'

Example:

seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2    #11, 71

seven_segment({'B', 'C', 'a', 'c', 'd', 'f', 'g'}, {'A', 'D', 'G', 'e'}) == 6    #15, 16, 35, 36, 75, 76

seven_segment({'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'}, {'G', 'g'}) == 4    #0, 8, 80, 88

Input: Two arguments. The first one contains the lit segments as a set of letters representing segments. The second one contains 
the broken segments as a set of letters representing segments.

Output: The total number that the device may be displaying.
"""

import re

display_nums = {('a', 'b', 'c', 'd', 'e', 'f'): 0, ('b', 'c'): 1, 
                ('a', 'b', 'd', 'e', 'g'): 2, ('a', 'b', 'c', 'd', 'g'): 3, 
                ('b', 'c', 'f', 'g'): 4, ('a', 'c', 'd', 'f', 'g'): 5, 
                ('a', 'c', 'd', 'e', 'f', 'g'): 6, ('a', 'b', 'c'): 7, 
                ('a', 'b', 'c', 'd', 'e', 'f', 'g'): 8, 
                ('a', 'b', 'c', 'd', 'f', 'g'): 9
               }

#------------------------------------------------------------------------------#

def display_seg(segment):
    first_display = []
    second_display = []
    for seg in segment:
        if re.match(r'[A-G]', seg):
            first_display.append(seg)
        else:
            second_display.append(seg)
    return (first_display, second_display)


#------------------------------------------------------------------------------#

def count_segment(display_lit, display_broken):
    count = 0
    n = len(display_broken)
    for i in range(2**n):
        mask = bin(i)[2:].zfill(n)
        display = display_lit[:]
        for k in range(n):
            if mask[k] == '1':
                display.append(display_broken[k]) 
        if tuple(sorted(display)) in display_nums:
            count += 1
    return count

#------------------------------------------------------------------------------#

def seven_segment(lit_seg, broken_seg):
    count = 0
    first_display_lit, second_display_lit = display_seg(lit_seg)
    first_display_broken, second_display_broken = display_seg(broken_seg)
    count1 = count_segment([k.lower() for k in first_display_lit], [k.lower() for k in first_display_broken])
    count2 = count_segment(second_display_lit, second_display_broken)
    return count1*count2

#------------------------------------------------------------------------------#

if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, 
                         {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, 
                         {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')
    
