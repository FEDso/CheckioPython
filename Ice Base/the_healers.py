'''

...the balance of power was once again not on the knights’ side.
Sir Ronald used the horn one more time to summon the last hope for his army - the healers. The temple they lived in was even 
closer than the castle from which the first wave of reinforcements arrived. If the healers get here fast enough, they’ll save 
many lives and the knights will have a chance to win.

The battle continues and each army is losing good warriors. Let's try to fix that and add a new unit type - the Healer.
Healer won't be fighting (his attack = 0, so he can't deal the damage). But his role is also very important - every time the 
allied soldier hits the enemy, the Healer will heal the allie, standing right in front of him by +2 health points with the 
heal() method. Note that the health after healing can't be greater than the maximum health of the unit. For example, if the 
Healer heals the Warrior with 49 health points, the Warrior will have 50 hp, because this is the maximum for him.
The basic parameters of the Healer:
health = 60
attack = 0

Example:

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
priest = Healer()

fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == False
fight(carl, mark) == False
carl.is_alive == False
fight(bob, mike) == False
fight(lancelot, rog) == True
fight(eric, richard) == False
fight(ogre, adam) == True
fight(freelancer, vampire) == True
freelancer.is_alive == True
freelancer.health == 14    
priest.heal(freelancer)
freelancer.health == 16

my_army = Army()
my_army.add_units(Defender, 2)
my_army.add_units(Healer, 1)
my_army.add_units(Vampire, 2)
my_army.add_units(Lancer, 2)
my_army.add_units(Healer, 1)
my_army.add_units(Warrior, 1)
    
enemy_army = Army()
enemy_army.add_units(Warrior, 2)
enemy_army.add_units(Lancer, 4)
enemy_army.add_units(Healer, 1)
enemy_army.add_units(Defender, 2)
enemy_army.add_units(Vampire, 3)
enemy_army.add_units(Healer, 1)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Lancer, 1)
army_3.add_units(Healer, 1)
army_3.add_units(Defender, 2)

army_4 = Army()
army_4.add_units(Vampire, 3)
army_4.add_units(Warrior, 1)
army_4.add_units(Healer, 1)
army_4.add_units(Lancer, 2)

battle = Battle()
battle.fight(my_army, enemy_army) == False
battle.fight(army_3, army_4) == True

Input: The warriors and armies.
Output: The result of the battle (True or False).
How it is used: For computer games development.
Precondition: 6 types of units

'''

# Taken from mission The Lancers

# Taken from mission The Vampires

# Taken from mission The Defenders

# Taken from mission Army Battles

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
    
    def get_alive(self):
        return self.health > 0
    
    def if_next_healer(self, other):
        return other.is_healer
    
    def __getattr__(self, name):
        if name in ('defense', 'vampirism', 'attack'):
            return 0
        if name in ('is_lancer', 'is_healer'):
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


class Healer(Warrior):
    is_healer = True
    def __init__(self):
        self.health = 60
        
    def heal(self, other):
        other.health = min(other.health + 2, type(other)().health)


def attack_result(attack, defense):
    return 0 if defense > attack else attack - defense


def fight(unit_1, unit_2, army1=[], army2=[]):
    next1, next2 = Warrior(), Warrior()
    while unit_1.is_alive and unit_2.is_alive:
        next1 = army1[0] if army1 else Warrior()
        next2 = army2[0] if army2 else Warrior()
        
        loss = attack_result(unit_1.attack, unit_2.defense)
        unit_2.health -= loss
        unit_1.health += loss*unit_1.vampirism
        if unit_1.is_lancer and army2:
            loss = attack_result(unit_1.attack*0.5, army2[0].defense)
            army2[0].health -= loss
        if next2.is_healer and unit_2.is_alive:
            next2.heal(unit_2)
        if not unit_2.is_alive:
            return unit_1.is_alive

        loss = attack_result(unit_2.attack, unit_1.defense)
        unit_1.health -= loss
        unit_2.health += loss*unit_2.vampirism
        if next1.is_healer and unit_1.is_alive:
            next1.heal(unit_1)
        if unit_2.is_lancer and army1:
            loss = attack_result(unit_2.attack*0.5, army1[0].defense)
            army1[0].health -= loss
        
        if not next1.is_alive:
            army1 = army1[1:] if len(army1) > 1 else Warrior()
        if not next2.is_alive:
            army2 = army1[1:] if len(army2) > 1 else Warrior()
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
            if fight(my_army.army[i], enemy_army.army[k], my_army.army[i+1:], enemy_army.army[k+1:]):
                while k != len(enemy_army.army) and not enemy_army.army[k].is_alive:
                    k += 1
            else:
                while i != len(my_army.army) and not my_army.army[i].is_alive:
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
    priest = Healer()

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
    assert freelancer.health == 14    
    priest.heal(freelancer)
    assert freelancer.health == 16

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!!!")
