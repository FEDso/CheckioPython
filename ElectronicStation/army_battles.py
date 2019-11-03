 In the previous mission - Warriors - you've learned how to make a duel between 2 warriors happen. Great job! But let's move to 
 something that feels a little more epic - the armies! In this mission your task is to add new classes and functions to the 
 existing ones. The new class should be the Army and have the method add_units() - for adding the chosen amount of units to the 
 army. The first unit added will be the first to go to fight, the second will be the second, ...
Also you need to create a Battle() class with a fight() function, which will determine the strongest army.
The battles occur according to the following principles:
at first, there is a duel between the first warrior of the first army and the first warrior of the second army. As soon as one 
of them dies - the next warrior from the army that lost the fighter enters the duel, and the surviving warrior continues to 
fight with his current health. This continues until all the soldiers of one of the armies die. In this case, the battle() 
function should return True, if the first army won, or False, if the second one was stronger.

Note that army 1 have the advantage to start every fight! 

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
    
    def get_alive(self):
        return self.health > 0
    
    is_alive = property(get_alive)


class Knight(Warrior):
    def __init__(self):
        super(Knight, self).__init__()
        self.attack += 2


def fight(unit_1, unit_2, health=[0, 0]):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack
        if not unit_2.is_alive:
            health[0], health[1] = unit_1.health, unit_2.health
            return unit_1.is_alive
        unit_1.health -= unit_2.attack
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
