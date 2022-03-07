from math import pi


class Cylinder:
    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle * 2 + side, 2)

    def __init__(self, di, hi):
        self.dia = di
        self.h = hi
        self.__area = self.make_area(self.dia, self.h)

    @property
    def area(self):
        return self.__area

    def __setattr__(self, key, value):
        if key == 'dia' or key == 'h' or key == '_Cylinder__area':
            object.__setattr__(self, key, value)
            if 'dia' in self.__dict__ and 'h' in self.__dict__ and key != "_Cylinder__area":
                self.__area = self.make_area(self.dia, self.h)
        else:
            raise AttributeError("False attribute")


a = Cylinder(1, 2)
print(a.area)
a.dia = 5
print(a.area)
print(a.make_area(2, 2))

a.area = 5