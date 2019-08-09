"""
Sofia has had a very stressful month and decided to take a vacation for a week. To avoid any stress during her vacation she 
wants to forward emails with a stressful subject line to Stephen.

The function should recognise if a subject line is stressful. A stressful subject line means that all letters are in uppercase, 
and/or ends by at least 3 exclamation marks, and/or contains at least one of the following “red” words: "help", "asap", "urgent". 
Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong 
way "HHHEEEEEEEEELLP"

Input: Subject line as a string.

Output: Boolean. 
"""

import re
stress_words = {r'h+e+l+p+', r'a+s+a+p+', r'u+r+g+e+n+t+'}

def is_stressful(subj):
    if subj[-3:] == '!!!':
        return True
    tmp = re.compile('[^a-zA-Z ]')
    subj = tmp.sub('', subj)
    if subj == subj.upper():
        return True
    for word in stress_words:
        if re.search(word, subj.lower()):
            return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')

