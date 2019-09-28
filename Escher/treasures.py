"""
 The vault turned out to have a quite gratifying content, and unlike the current paper currencies, the truly valuable things 
 used to be made of gold and silver. On top of that, there were precious stones, jewelry, and many other valuable items. You 
 wanted so badly to take everything, but, unfortunately, your crew has died, and by yourself you could carry only a part of the 
 treasure. Well, let it be the most valuable part then!

As input you'll receive the information about the vault contents in the following format: {'golden coin': {'price': 100, 
'weight': 50, 'amount': 200}, 'silver coin': {'price': 10, 'weight': 20, 'amount': 1000} , 'ruby': {'price': 1000, 'weight': 
200, 'amount': 2}}, where price is measured in the standard units of your country's currency, weight is measured in grams, and 
amount is measured in pieces.
In addition, you'll also have a weight limit (in kilograms), over which you won't be able to carry.

Your task is to collect such a set of treasures so that their total weight doesn't exceed the limit, and their total cost was 
as high as possible. The answer must be returned as the list of strings, for example: ['golden coin: 150', 'silver coin: 700', 
'ruby: 2']. There always be 3 types of the treasures (golden coin, silver coin and ruby) and it should be represent in the 
answer in the same order. If some type of the treasures are out of limit (so you 'can' take it 0) - just don't include it into 
answer.

Input: Dictionary with information about treasures and weight limit.

Output: All treasures, which you take (a list of strings). 
"""

def comb_res(res1, res2, res3, i, j, k):
    res = []
    if res1 != '' and i != 0:
        res.append(res1)
    if res2 != '' and j != 0:
        res.append(res2)
    if res3 != '' and k != 0:
        res.append(res3)
    return '   '.join(res)
    
#------------------------------------------------------------------------------#

def treasures(info, limit):
    riches = ['golden coin', 'silver coin', 'ruby']
    result = {}
    for i in range(info['golden coin']['amount'] + 1):
        res1 = ''
        weight1 = i*info['golden coin']['weight']/1000
        if round(weight1, 3) <= limit:
            res1 = 'golden coin: ' + str(i)
        else:
            continue
        for j in range(info['silver coin']['amount'] + 1):
            res2 = ''
            weight2 = j*info['silver coin']['weight']/1000
            if round(weight1 + weight2, 3) <= limit:
                res2 = 'silver coin: ' + str(j)
            else:
                continue
            for k in range(info['ruby']['amount'] + 1):
                res3 = ''
                weight3 = k*info['ruby']['weight']/1000
                if round(weight1 + weight2 + weight3, 3) <= limit:
                    res3 = 'ruby: ' + str(k)
                else:
                    continue
                res = comb_res(res1, res2, res3, i, j, k)
                if res != '':
                    result[res] = (info['golden coin']['price']*i + 
                                   info['silver coin']['price']*j + 
                                   info['ruby']['price']*k)
    result = sorted(result.items(), key=lambda x: x[1])[-1][0].split('   ')
    return result


#------------------------------------------------------------------------------#

if __name__ == '__main__':
    print("Example:")
    print(treasures({'golden coin': 
                        {'price': 100, 'weight': 50, 'amount': 200}, 
                     'silver coin': 
                        {'price': 10, 'weight': 20, 'amount': 1000}, 
                     'ruby': 
                        {'price': 1000, 'weight': 200, 'amount': 2}}, 5))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert treasures({'golden coin': 
                         {'price': 100, 'weight': 50, 'amount': 200}, 
                      'silver coin': 
                         {'price': 10, 'weight': 20, 'amount': 1000}, 
                      'ruby': 
                         {'price': 1000, 'weight': 200, 'amount': 2}}, 5) == [
                          'golden coin: 92', 'ruby: 2']
    assert treasures({'golden coin': 
                         {'price': 100, 'weight': 50, 'amount': 100}, 
                      'silver coin': 
                         {'price': 10, 'weight': 20, 'amount': 100}, 
                      'ruby': 
                         {'price': 1000, 'weight': 200, 'amount': 1}}, 7.5) == [
                          'golden coin: 100', 'silver coin: 100', 'ruby: 1']
    print("Coding complete? Click 'Check' to earn cool rewards!")
