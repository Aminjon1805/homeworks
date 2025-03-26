from math import pi


class AbstractShape:

    def area(self):
        pass

    def perimetr(self):
        pass


class Circle(AbstractShape):

    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return f"Area = {(pi * self.radius**2):.2f}"


    def perimetr(self):
        return f"Perimetr = {(2 * pi * self.radius):.2f}"



class Rectangle(AbstractShape):

    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        return f"Area = {(self.width * self.length):.2f}"


    def perimetr(self):
        return f"Perimetr = {2*(self.length + self.width):.2f}"


class Square(AbstractShape):

    def __init__(self, side):
        self.side = side


    def area(self):
        return f"Area = {(self.side**2):.2f}"


    def perimetr(self):
        return f"Perimetr = {(self.side * 4):.2f}"


