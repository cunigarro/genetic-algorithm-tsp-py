from libs.tour import Tour


class Population:

    tours = []

    def __init__(self, population_size, initialise) -> None:
        self.tours = [None] * population_size

        if initialise:
            for index in range(self.population_size()):
                new_tour = Tour()
                new_tour.generate_individual()
                self.save_tour(index, new_tour)

    def save_tour(self, index, tour):
        self.tours[index] = tour

    def get_tour(self, index) -> Tour:
        return self.tours[index]

    def get_fittest(self) -> Tour:
        fittest: Tour = self.tours[0]
        for index in range(self.population_size()-1):
            if fittest.get_fitness() <= self.get_tour(index).get_fitness():
                fittest = self.get_tour(index)

        return fittest

    def population_size(self):
        return len(self.tours)
