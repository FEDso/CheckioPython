"""
 You are given a two or more digits number N. For this mission, you should find the smallest positive number of X, such that 
 the product of its digits is equal to N. If X does not exist, then return 0.

Let's examine the example. N = 20. We can factorize this number as 2*10, but 10 is not a digit. Also we can factorize it as 
4*5 or 2*2*5. The smallest number for 2*2*5 is 225, for 4*5 -- 45. So we select 45.

Hints: Remember prime numbers (numbers divisible by only one) and be careful with endless loops.

Input: A number N as an integer.

Output: The number X as an integer. 
"""

def num_to_mul(n):
    res = []
    if n == 1:
        return res
    for i in range(2, 10):
        if n%i == 0:
            tmp = num_to_mul(n//i)
            if tmp == 0:
                return 0
            if tmp != []:
                for k in tmp:
                    res.append(str(i) + k)
            else:
                res.append(str(i))
    if res == []:
        return 0
    return res
    
def checkio(number):
    res = num_to_mul(number)
    if res == 0:
        return 0
    res = list(map(lambda x: ''.join(sorted(x)), res))
    res = sorted(res)
     
    if res:
        return int(min(res, key=lambda x: int(x)))
    return 0
    
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
    
