from math import sqrt
from random import randint

class City:
    x = 0
    y = 0

    """ def __init__(self) -> None:
        self.x = randint(0, 200)
        self.y = randint(0, 200) """

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_x(self):
        pass

    def get_y(self):
        pass

    def distance_to(self, city):
        x_distance = abs(self.get_x() - city.get_x())
        y_distance = abs(self.get_y() - city.get_y())

        distance = sqrt((x_distance*x_distance) + (y_distance*y_distance))

        return distance
