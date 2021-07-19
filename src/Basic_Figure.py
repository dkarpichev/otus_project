from decimal import Decimal
from math import sqrt, pi


def decimal_integer(integer):
    return Decimal(f"{integer}")


class Figure:
    @classmethod
    def pre_init(cls):
        if cls.__name__ == "Figure":
            raise Exception('Unable to create class "Figure"')
        else:
            return cls.__name__

    @classmethod
    def is_it_string(cls, sides):
        for i in sides:
            try:
                decimal_integer(i)
            except:
                raise ValueError("Use integer or float for the sides parameter")

    def __init__(self, sides=None):
        self.name = self.pre_init()
        self.sides = sides

    @property
    def area(self):
        if self.name == "Triangle":
            p = decimal_integer(self.perimeter / 2)
            side_a = decimal_integer(self.sides[0])
            side_b = decimal_integer(self.sides[1])
            side_c = decimal_integer(self.sides[2])
            return decimal_integer(sqrt(p * (p - side_c) * (p - side_b) * (p - side_a)))
        elif self.name == "Rectangle":
            side_a = decimal_integer(self.sides[0])
            side_b = decimal_integer(self.sides[1])
            return decimal_integer(side_b * side_a)
        elif self.name == "Square":
            side_a = decimal_integer(self.sides[0])
            return side_a ** 2
        elif self.name == "Circle":
            radius = decimal_integer(self.sides[0])
            return decimal_integer(pi) * (radius * radius)
        else:
            raise Exception("This is not a figure")

    @property
    def perimeter(self):
        try:
            if self.name != "Circle":
                perim = 0
                for i in self.sides:
                    perim += decimal_integer(i)
            else:
                perim = decimal_integer(pi) * (decimal_integer(self.sides[0]) * 2)
            return perim
        except:
            raise ("Something went wrong")

    def add_area(self, figure):
        try:
            return self.area + figure.area
        except ValueError:
            raise ("Wrong class passed")
