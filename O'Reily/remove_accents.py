"""
Assuming you are developing a user based system like facebook, you will want to provide the functionality to search for other 
members regardless of the presence of accents in a username. Without using 3rd party collation library, you will need to remove 
the accents from username before comparison.

é - letter with accent; e - letter without accent; ̀ and ́ - stand alone accents;

Input: A phrase as a string (unicode)

Output: An accent free Unicode string. 
"""


import unicodedata

def checkio(in_string):
    out_string = unicodedata.normalize('NFKD', in_string).encode('ASCII', 'ignore')
    if out_string == b'':
        return in_string
    return out_string.decode('utf-8')

    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print(checkio(u"完好無缺"))
    print('Done')
