class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    def square(self):
        pass


import math


class Circle(Figure):
    class_name = 'Circle'
    def __init__(self, point: Point, radius):
        self.point = point
        self.radius = radius

    def perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter

    def square(self):
        square = 3.14 * pow(self.radius, 2)
        return square


class Triangle(Figure):
    class_name = 'Triangle'
    def __init__(self, point_1: Point, point_2: Point, point_3: Point):
        self.point_a = point_1
        self.point_b = point_2
        self.point_c = point_3

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


class Square(Figure):
    class_name = 'Square'
    def __init__(self, point_1: Point, point_2: Point):
        self.point_a = point_1
        self.point_b = point_2

    def side_of_square(self):
        side = side_1 = math.sqrt(pow((self.point_a.x - self.point_b.x), 2) + pow((self.point_a.y - self.point_b.y), 2))
        return side

    def perimeter(self):
        return self.side_of_square()*4

    def square(self):
        return pow(self.side_of_square(), 2)
