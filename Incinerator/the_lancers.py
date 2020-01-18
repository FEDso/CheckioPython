# Taken from mission The Vampires

# Taken from mission The Defenders

# Taken from mission Army Battles

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
    
    def get_alive(self):
        return self.health > 0
    
    def __getattr__(self, name):
        if name in ('defense', 'vampirism'):
            return 0
        if name == 'is_lancer':
            return False
            
    is_alive = property(get_alive)


class Knight(Warrior):
    def __init__(self):
        super(Knight, self).__init__()
        self.attack += 2


class Defender(Warrior):
    def __init__(self):
        self.health = 60
        self.attack = 3
        self.defense = 2


class Vampire(Warrior):
    def __init__(self):
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5


class Lancer(Warrior):
    def __init__(self):
        super(Lancer, self).__init__()
        self.attack += 1
        self.is_lancer = True


def attack_result(attack, defense):
    return 0 if defense > attack else attack - defense


def fight(unit_1, unit_2, health=[0, 0], attack_count=[0, 0]):
    while unit_1.is_alive and unit_2.is_alive:
        if unit_1.is_lancer:
            attack_count[0] += 1
        loss = attack_result(unit_1.attack, unit_2.defense)
        unit_2.health -= loss
        unit_1.health += loss*unit_1.vampirism
        if not unit_2.is_alive:
            health[0], health[1] = unit_1.health, unit_2.health
            return unit_1.is_alive
        if unit_2.is_lancer:
            attack_count[1] += 1
        loss = attack_result(unit_2.attack, unit_1.defense)
        unit_1.health -= loss
        unit_2.health += loss*unit_2.vampirism
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
        ii, kk = 0, 0
        while True:
            life, count = [0, 0], [0, 0]
            if fight(my_army.army[i], enemy_army.army[k], life, count):
                my_army.army[i].health = life[0]
                kk = k
                k += 1
            else:
                enemy_army.army[k].health = life[1]
                ii = i
                i += 1
            if i == len(my_army.army):
                return False
            elif k == len(enemy_army.army):
                return True
            if kk != len(enemy_army.army) - 1:
                loss = attack_result(my_army.army[ii].health*0.5, enemy_army.army[kk+1].defense)
                enemy_army.army[kk+1].health -= loss*count[0]
            if ii != len(my_army.army) - 1:
                loss = attack_result(enemy_army.army[kk].health*0.5, my_army.army[ii+1].defense)
                my_army.army[ii+1].health -= loss*count[1]

            

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
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

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
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
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
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()

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
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
