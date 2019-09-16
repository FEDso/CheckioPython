"""
 Greetings, adventurer! You are now at the beginning of a dangerous but at the same time a very exciting journey, during which 
 you’ll have to solve many riddles, neutralize several traps, and outrun your pursuers… And all this for the sole purpose of 
 finding one of the most valuable artifacts in the universe, the source of the infinite energy - the Hypercube.

The Hypercube is located in the very center of the castle, built by the eccentric Lord Escher a couple of centuries ago. This 
man built his castle on the island due to his high appreciation for the solitude. Ever since he died (under the very mysterious 
circumstances), and his servants who have returned to the continent told the world about the strange things and phenomena 
happening there, many of the research expeditions and groups of treasure hunters went there. But none of them have ever 
returned...

Good luck, buddy! Perhaps you are bound to have more luck than others.

So, the things are packed, equipment gathered and it's high time to hit the road. Currently you are on the continent, 
standing in the port. Foreseeing the danger you might be facing on the island, you’ve decided not to go there alone, but 
to recruit a team and equip 2 ships. Your only goal is to get hold of a Cube, the other treasures that you are hoping to 
find will be considered the payment for the team.

And the first task is simple - you have to divide all your crew members into 2 teams (for the 2 ships).

You have to divide all your crew members into 2 teams with the next rules: those who are elder than 40 y.o. or younger than 2
0, should be on the first ship and all the others - on the second. It will helps the young sailors gain the experience of the 
elder collegues. The input data will be the dictionary where keys will be the surnames of the sailors and the values will be 
their ages. After the crew formating, you should sort all of the sailors in the alphabetical order in the each list of surnames.

Input: Dictionary with the sailors and their ages.

Output: List of the lists with 2 teams. 
"""

def two_teams(sailors):
    ship1 = []
    ship2 = []
    for key, value in sailors.items():
        if 20 <= value <= 40:
            ship2.append(key)
        else:
            ship1.append(key)
    return [
        sorted(ship1),
        sorted(ship2)
    ]


if __name__ == '__main__':
    print("Example:")
    print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert two_teams({
        'Smith': 34, 
        'Wesson': 22, 
        'Coleman': 45, 
        'Abrahams': 19}) == [
            ['Abrahams', 'Coleman'], 
            ['Smith', 'Wesson']
            ]

    assert two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
            ['Fernandes', 'Kale', 'McCortney'], 
            ['Johnson']
            ]
    print("Coding complete? Click 'Check' to earn cool rewards!")
