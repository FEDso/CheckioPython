"""
 Your task in this mission is to truncate a sentence to a length, that does not exceed a given number of characters.

If the given sentence already is short enough you don't have to do anything to it, but if it needs to be truncated the omission 
must be indicated by concatenating an ellipsis ("...") to the end of the shortened sentence.

The shortened sentence can contain complete words and spaces.
It must neither contain truncated words nor trailing spaces.
The ellipsis has been taken into account for the allowed number of characters, so it does not count against the given length.

Input: Two arguments:

    one-line sentence as a string
    max length of the truncated sentence as an int

Output: The shortened sentence plus the ellipsis (if required) as a one-line string. 
"""

def cut_sentence(line, length):
    if len(line) > length:
        tmp = line[:length]
        if tmp[-1].isalpha() and line[length].isalpha():
            for i in range(len(tmp)-1, -1, -1):
                if not tmp[i].isalpha():
                    tmp = tmp[:i+1]
                    break
            if i == 0:
                return '...'
        if not tmp[-1].isalpha():
            for i in range(len(tmp)-1, -1, -1):
                if tmp[i].isalpha():
                    tmp = tmp[:i+1]
                    break
        return tmp + '...'
    else:
        return line
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(cut_sentence("Hi, my name is Alex", 1))
    assert cut_sentence("Hi my name is Alex", 4) == "Hi...", "First"
    assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "Second"
    assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
    assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
    print('Done! Do you like it? Go Check it!')
    
