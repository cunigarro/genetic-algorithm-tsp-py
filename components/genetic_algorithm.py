from random import randint, random
from components.population import Population
from components.tour import Tour


class GeneticAlgorithm:
    mutation_rate = 0.015
    tournament_size = 5
    elitism = True

    @staticmethod
    def evolve_population(pop: Population):
        new_population = Population(pop.population_size(), False)

        elitism_offset = 0
        if GeneticAlgorithm.elitism:
            new_population.save_tour(0, pop.get_fittest())
            elitism_offset = 1

        for index in range(elitism_offset, new_population.population_size()):
            parent_1 = GeneticAlgorithm.tournament_selection(pop)
            parent_2 = GeneticAlgorithm.tournament_selection(pop)

            child = GeneticAlgorithm.crossover(parent_1, parent_2)
            new_population.save_tour(index, child)

        for index in range(elitism_offset, new_population.population_size()):
            GeneticAlgorithm.mutate(new_population.get_tour(index))

        return new_population

    @staticmethod
    def tournament_selection(pop: Population):
        tournament = Population(GeneticAlgorithm.tournament_size, False)

        for index in range(GeneticAlgorithm.tournament_size):
            random_id = randint(0, pop.population_size() - 1)
            tournament.save_tour(index, pop.get_tour(random_id))

        fittest = tournament.get_fittest()
        return fittest

    @staticmethod
    def crossover(parent_1: Tour, parent_2: Tour):
        child = Tour()

        start_pos = randint(0, parent_1.tour_size() - 1)
        end_pos = randint(0, parent_1.tour_size() - 1)

        while start_pos == end_pos:
            end_pos = randint(0, parent_1.tour_size() - 1)

        for i in range(child.tour_size()):
            if start_pos < end_pos and i > start_pos and i < end_pos:
                child.set_city(i, parent_1.get_city(i))
            elif start_pos > end_pos:
                if not (i < start_pos and i > end_pos):
                    child.set_city(i, parent_1.get_city(i))

        for i in range(parent_2.tour_size()):
            if not child.contains_city(parent_2.get_city(i)):
                for ii in range(child.tour_size()):
                    if child.get_city(ii) is None:
                        child.set_city(ii, parent_2.get_city(i))
                        break

        return child

    @staticmethod
    def mutate(tour: Tour):
        for tour_pos_1 in range(tour.tour_size()):
            if random() < GeneticAlgorithm.mutation_rate:
                tour_pos_2 = randint(0, tour.tour_size() - 1)

                city_1 = tour.get_city(tour_pos_1)
                city_2 = tour.get_city(tour_pos_2)

                tour.set_city(tour_pos_2, city_1)
                tour.set_city(tour_pos_1, city_2)
