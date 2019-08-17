"""
 A very similar to the first is the second mission of the series with only one distinction is that you should look in a 
 completely different way. You need to find the first longest substring with all unique letters. For example, in substring 
 "abca" we have two substrings with unique letters "abc" and "bca", but we should take the first one, so the answer is "abc".

Input: String.

Output: String. 
"""

def non_repeat(line):
    long_str = set()
    result = ''
    for i in range(len(line)):
        if line[i] not in long_str:
            long_str.add(line[i])
        else:
            if len(result) < len(long_str):
                result = line[i - len(long_str):i]
            for k in range(i - len(long_str), i):
                if line[k] != line[i]:
                    long_str.remove(line[k])
                else:
                    break
    if len(result) < len(long_str):
        result = line[len(line) - len(long_str):len(line)]
    if len(line) > 0 and result == '':
        return line
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')
    
