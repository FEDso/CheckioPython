"""
 Your hunch was right, in addition to the usual room stuff, such as a bookcase, wardrobe, desk and a bed, there also was a quite 
 sizeable vault. Your mood immediately improved - this trip very quickly became profitable (unless, of course, the vault wasn’t 
 empty).

A small sheet of thick paper laid on the table next to the vault. There were some kind of formulas with wiped out figures written 
on it. It’s likely that a long time ago these notes were quite easy to read, but the decades spent in the castle negatively 
affected the readability of some figures. By figuring out what figures were originally written, you’ll be able to find the correct 
combination for opening of the vault.

Your task is to create a function that as input receives an equation in a form of a string with digits, erased places ('#') and 
one of the three arithmetic operations (+, - or *), for example - "##*##=302#". As a result, your function should return a digit 
(from the interval 0-9), which when applied instead of all #, made the equation correct. Or -1 (minus one) if this isn’t possible.

Important note - none of the figures that already are in the equation cannot be in place of #. Also, if after the equal sign (=) 
there are 2 or more missing symbols, the answer cannot consist of zeros (00, 000, etc.).
Numbers in the format like #n, #nn and so on, where n - any digit, can't start with 0. For example, "#9+3=12" == -1.
In case there are several suitable digits - use the smallest of them. Еhe numbers in the formula can be both positive (for 
example, "1+1=#") and negative, with the "-" sign before them ("19--45=5#", "-1*-6=#").

Input: Cypher.

Output: Digit of the safe code. 
"""

def result(s, n):
    ops = ['+', '-', '*']
    s = s.replace('#', str(n))
    for p in ops:
        s = s.replace(p, ' ' + p + ' ')
    s = s.split()
    stack = []
    for i in range(len(s)-1, -1, -1):
        if s[i] not in ops:
            if s[i][0] == '0' and len(s[i]) > 0:
                return False
            stack.append(int(s[i]))
        else:
            if s[i] == '-' and (s[i-1] in ops or i == 0):
                stack[-1] *= -1
            else:
                op = s[i]
    if op == '-':
        return stack[1] - stack[0]
    if op == '*':
        return stack[0]*stack[1]
    return stack[0] + stack[1]
    
#------------------------------------------------------------------------------#

def safe_code(equation):
    equation = equation.split('=')
    for i in range(10):
        if str(i) not in equation[0] and str(i) not in equation[1]:
            x = result(equation[0], i)
            y = equation[1].replace('#', str(i))
            if y == '0'*len(y):
                continue
            if x == int(y):
                return i
    return -1

#------------------------------------------------------------------------------#

if __name__ == '__main__':
    print("Example:")
    print(safe_code("24-35=-##"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_code("-5#*-1=5#") == 0
    assert safe_code("##*##=302#") == 5
    assert safe_code("19--45=5#") == -1
    assert safe_code("##--11=11") == -1
    assert safe_code("#9+3=22") == 1
    assert safe_code("11*#=##") == 2
    assert safe_code("#9+3=12") == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
