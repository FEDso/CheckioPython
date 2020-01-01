class Lamp:
    states = ('Green', 'Red', 'Blue', 'Yellow')
    
    def __init__(self):
        self.state = 0
    
    def light(self):
        res = self.states[self.state]
        self.state = (self.state + 1)%4
        return res


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    lamp_1 = Lamp()
    lamp_2 = Lamp()

    lamp_1.light() #Green
    lamp_1.light() #Red
    lamp_2.light() #Green
    
    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"
    print("Coding complete? Let's try tests!")
