"""
 Here you are in the castle. Despite the fact that it’s already about 200 years old, it doesn’t look like an ancient ruin at all. 
 In the great hall (of a very odd geometrical form) you’re seeing the following: - a beautiful spiral staircase leading to the 
 2nd floor; - an equally attractive staircase that leads into the dungeon; - a lot of doors of a wide variety of different shapes, 
 colors and designs. Having decided to explore the doors on this floor first, you’ve assumed that the most interesting things 
 should be in the very last room. However, finding it won’t be as easy as it seems.

Before going on this trip, you’ve gathered some information about the Lord Escher's quirks. One of them was a very unusual 
numbering of doors - he numbered them according to how the numbers go in the alphabetical order. For example, if there were five 
doors positioned from left to right, they were numbered as: five, four, one, three, two (instead of a completely logical 
numeration - 1, 2, 3, 4, 5). Thus, the very last door was actually the leftmost, not the very right one, as it might be assumed. 
Your task is to find the very last door.

As input your function will receive an integer - the total number of doors in the current room. You will need to sort the door 
numbers in the order in which these numbers, expressed in words, go in the alphabetical order. And then return the position number 
of the last door (the door with the highest number). The count starts from the 1st position (not from the 0th). The maximum number 
of doors is 1000. The numbers after 100 are written in the format like - 'one hundred twenty nine'.

Input: the door number.

Output: the 'right' door number. 
"""

nums = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', 
        '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', 
        '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', 
        '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', 
        '20': 'twenty', '30': 'thirty', '40': 'forty', '50': 'fifty', 
        '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety', 
        '1000': 'one thousand'}

#------------------------------------------------------------------------------#

def num_to_alpha(n):
    if n < 20 or n == 1000:
        return nums[str(n)]
    if n < 100 and str(n)[1] == '0':
        return nums[str(n)[0] + '0']
    if n < 100:
        return nums[str(n)[0] + '0'] + ' ' + nums[str(n)[1]]
    s = nums[str(n)[0]] + ' hundred'
    if str(n)[1] == '1':
        s += ' ' + nums[str(n)[1:]]
    else:
        if str(n)[1] != '0':
            s += ' ' + nums[str(n)[1] + '0'] 
        if str(n)[2] != '0':
            s += ' ' + nums[str(n)[2]]
    return s
    
#------------------------------------------------------------------------------#

def secret_room(number):
    nums_alpha = []
    for i in range(1, number + 1):
        nums_alpha.append(num_to_alpha(i))
    k = sorted(nums_alpha).index(num_to_alpha(number)) + 1
    return k

#------------------------------------------------------------------------------#

if __name__ == '__main__':
    print("Example:")
    print(secret_room(5))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert secret_room(5) == 1 #five, four, one, three, two
    assert secret_room(3) == 2 #one, three, two
    assert secret_room(1000) == 551
    print(secret_room(666))
    print("Coding complete? Click 'Check' to earn cool rewards!")
