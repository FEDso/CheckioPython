from math import pi, sin

class Parameters:
    def __init__(self, a):
        self.a = a

    def choose_figure(self, figure):
        self.figure = figure

    def perimeter(self):
        return self.figure.perimeter(self.a)

    def area(self):
        return self.figure.area(self.a)

    def volume(self):
        return self.figure.volume(self.a)


class Circle:
    def perimeter(self, a):
        return round(2*pi*a, 2)

    def area(self, a):
        return round(pi*a**2, 2)

    def volume(self, a):
        return 0


class Triangle:
    def perimeter(self, a):
        return round(3*a, 2)

    def area(self, a):
        return round(a*(a**2 - (a/2)**2)**(1/2)/2, 2)

    def volume(self, a):
        return 0


class Square:
    def perimeter(self, a):
       return 4*a

    def area(self, a):
        return a**2

    def volume(self, a):
        return 0


class Pentagon:
    def perimeter(self, a):
        return 5*a

    def area(self, a):
        return round(a**2*(25 + 10*5**(1/2))**(1/2)/4, 2)

    def volume(self, a):
        return 0
    

class Hexagon:
    def perimeter(self, a):
        return 6*a

    def area(self, a):
        return round((3**(3/2)*a**2)/2, 2)

    def volume(self, a):
        return 0
    

class Cube:
    def perimeter(self, a):
        return 12*a

    def area(self, a):
        return 6*a**2

    def volume(self, a):
        return a**3
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    figure = Parameters(10)
    
    figure.choose_figure(Circle())
    assert figure.area() == 314.16
    
    figure.choose_figure(Triangle())
    assert figure.perimeter() == 30

    figure.choose_figure(Square())
    assert figure.area() == 100

    figure.choose_figure(Pentagon())
    assert figure.perimeter() == 50
    print(figure.area())

    figure.choose_figure(Hexagon())
    assert figure.perimeter() == 60

    figure.choose_figure(Cube())
    assert figure.volume() == 1000

    print("Coding complete? Let's try tests!")
