from libs.population import Population


class GeneticAlgorithm:
    mutation_rate = 0.015
    tournament_size = 5
    elitism = True

    def evolve_population(self, pop: Population):
        new_population = Population(pop.population_size(), False)

        elitism_offset = 0
        if self.elitism:
            new_population.save_tour(0, pop.get_fittest())
            elitism_offset = 1

        for index in range(elitism_offset, new_population.population_size()):
            parent_1 = self.tournament_selection(pop)
            parent_2 = self.tournament_selection(pop)

            child = self.crossover(parent_1, parent_2)
            new_population.save_tour(index, child)

        for index in range(elitism_offset, new_population.population_size()):
            self.mutate(new_population.get_tour(index))

        return new_population

    def tournament_selection(self):
        pass

    def crossover(self):
        pass

    def mutate(self):
        pass
