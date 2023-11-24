import random
from components.tour_manager import TourManager


class Tour:
    def __init__(self, tour = None) -> None:
        if tour is None:
            self.tour = [None] * TourManager.number_of_cities()
        else:
            self.tour = tour

        self.fitness = 0
        self.distance = 0

    def generate_individual(self):
        for city_index in range(TourManager.number_of_cities()):
            self.set_city(city_index, TourManager.get_city(city_index))

        random.shuffle(self.tour)

    def get_city(self, tour_position):
        return self.tour[tour_position]

    def set_city(self, tour_position, city):
        self.tour[tour_position] = city
        self.fitness = 0
        self.distance = 0

    def get_fitness(self):
        if self.fitness == 0:
            fitness = 1/self.get_distance()

        return fitness

    def get_distance(self):
        if self.distance == 0:
            tour_distance = 0

            for city_index in range(self.tour_size()):
                from_city = self.get_city(city_index)
                destination_city = None

                if city_index + 1 < self.tour_size():
                    destination_city = self.get_city(city_index + 1)
                else:
                    destination_city = self.get_city(0)

                tour_distance += from_city.distance_to(destination_city)

            self.distance = tour_distance

        return self.distance

    def tour_size(self):
        return len(self.tour)

    def contains_city(self, city):
        return city in self.tour
