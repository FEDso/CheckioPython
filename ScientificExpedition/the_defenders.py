# Taken from mission Army Battles

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
    
    def get_alive(self):
        return self.health > 0
    
    def __getattr__(self, name):
        if name == 'defense':
            return 0
            
    is_alive = property(get_alive)


class Knight(Warrior):
    def __init__(self):
        super(Knight, self).__init__()
        self.attack += 2

    def __getattr__(self, name):
        if name == 'defense':
            return 0


class Defender(Warrior):
    def __init__(self):
        self.health = 60
        self.attack = 3
        self.defense = 2


def fight(unit_1, unit_2, health=[0, 0]):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= (0 if unit_2.defense > unit_1.attack else unit_1.attack - unit_2.defense)
        if not unit_2.is_alive:
            health[0], health[1] = unit_1.health, unit_2.health
            return unit_1.is_alive
        unit_1.health -= (0 if unit_1.defense > unit_2.attack else unit_2.attack - unit_1.defense)
    health[0], health[1] = unit_1.health, unit_2.health
    return unit_1.is_alive


class Army():
    def __init__(self):
        self.army = []
        
    def add_units(self, t_unit, n):
        for _ in range(n): 
            self.army.append(t_unit())


class Battle():
    def fight(self, my_army, enemy_army):
        i, k = 0, 0
        while True:
            life = [0, 0]
            if fight(my_army.army[i], enemy_army.army[k], life):
                my_army.army[i].health = life[0]
                k += 1
            else:
                enemy_army.army[k].health = life[1]
                i += 1
            if i == len(my_army.army):
                return False
            elif k == len(enemy_army.army):
                return True

            

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)
    
    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True, 'first'
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
