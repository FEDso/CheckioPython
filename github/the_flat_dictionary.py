"""
 Nikola likes to categorize everything in sight. One time Stephan gave him a label maker for his birthday, and the robots were 
 peeling labels off of every surface in the ship for weeks. He has since categorized all the reagents in his laboratory, books 
 in the library and notes on the desk. But then he learned about python dictionaries, and categorized all the possible 
 configurations for Sophia’s drones. Now the files are organized in a deep nested structure, but Sophia doesn’t like this. 
 Let's help Sophia to flatten these dictionaries.

Python dictionaries are a convenient data type to store and process configurations. They allow you to store data by keys to 
create nested structures. You are given a dictionary where the keys are strings and the values are strings or dictionaries. 
The goal is flatten the dictionary, but save the structures in the keys. The result should be the a dictionary without the 
nested dictionaries. The keys should contain paths that contain the parent keys from the original dictionary. The keys in 
the path are separated by a "/". If a value is an empty dictionary, then it should be replaced by an empty string (""). 

Let's look at an example:
{
 "name": {
          "first": "One",
          "last": "Drone"
         },
 "job": "scout",
 "recent": {},
 "additional": {
                "place": {
                          "zone": "1",
                          "cell": "2"
                         }
               }
}

The result will be:

{
 "name/first": "One",           #one parent
 "name/last": "Drone",
 "job": "scout",                #root key
 "recent": "",                  #empty dict
 "additional/place/zone": "1",  #third level
 "additional/place/cell": "2"
 }


Input: An original dictionary as a dict.

Output: The flattened dictionary as a dict. 
"""

def path_dict(dictionary):
    print(dictionary)
    res = []
    for key, value in dictionary.items():
        if type(value) == dict:
            if not value:
                res.append('/' + key + '$:$' + '')
            else:
                pathes = path_dict(value)
                for path in pathes:
                    res.append('/' + key + path)
        else: 
            res.append('/' + key + '$:$' + value)
    return res 

#------------------------------------------------------------------------------#

def flatten(dictionary):
    flat_dict = {}
    pathes = path_dict(dictionary)
    for path in pathes:
        path = path.rsplit('$:$', 1)
        flat_dict[path[0][1:]] = path[1]
    return flat_dict

#------------------------------------------------------------------------------#

if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))
    print(flatten({"glossary":{"GlossDiv":{"GlossList":{"GlossEntry":{"GlossDef":{"GlossSeeAlso":{"1":"GML","2":"XML"},
                   "para":"A meta-markup language, used to create markup languages such as DocBook."},"GlossSee":"markup",
                   "Acronym":"SGML","GlossTerm":"Standard Generalized Markup Language","Abbrev":"ISO 8879:1986",
                   "SortAs":"SGML","ID":"SGML"}},"title":"S"},"title":"example glossary"},"source":"http://json.org/example"})
)

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')
    
