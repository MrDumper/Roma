class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    pass


import math


class Circle(Figure, Point):
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def circle_constructor(cls):
        

    def perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter

    def square(self):
        square = 3.14 * pow(self.radius, 2)
        return square


class Triangle(Figure, Point):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.point_a = super().__init__(x1, y1)
        self.point_b = super().__init__(x2, y2)
        self.point_c = super().__init__(x3, y3)

    def sides(self):
        side_1 = math.sqrt(pow((self.point_a.x - self.point_b.x), 2) + pow((self.point_a.y - self.point_b.y), 2))
        side_2 = math.sqrt(pow((self.point_b.x - self.point_c.x), 2) + pow((self.point_b.y - self.point_c.y), 2))
        side_3 = math.sqrt(pow((self.point_c.x - self.point_a.x), 2) + pow((self.point_c.y - self.point_a.y), 2))
        return [side_1, side_2, side_3]

    def perimeter(self):
        sides_ = self.sides()
        perimeter = sum(sides_)
        return perimeter

    def square(self):
        sides_ = self.sides()
        half_perimeter = self.perimeter() / 2
        square = math.sqrt(half_perimeter*(half_perimeter-sides_[0])*(half_perimeter-sides_[1])*(half_perimeter-sides_[2]))
        return square


class Square(Figure, Point):
    def __init__(self, x1, y1, x2, y2):
        self.point_a = super().__init__(x1, y1)
        self.point_b = super().__init__(x2, y2)

    def side_of_square(self):
        side = side_1 = math.sqrt(pow((self.point_a.x - self.point_b.x), 2) + pow((self.point_a.y - self.point_b.y), 2))
        return side

    def perimeter(self):
        return self.side_of_square()*4

    def square(self):
        return pow(self.side_of_square(), 2)
