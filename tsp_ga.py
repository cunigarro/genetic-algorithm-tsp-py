from libs.city import City
from libs.genetic_algorithm import GeneticAlgorithm
from libs.population import Population
from libs.tour_manager import TourManager

locations = [
    {
        'x': 60,
        'y': 200
    },
    {
        'x': 180,
        'y': 200
    },
    {
        'x': 80,
        'y': 180
    },
    {
        'x': 140,
        'y': 180
    },
    {
        'x': 20,
        'y': 160
    },
    {
        'x': 100,
        'y': 160
    },
    {
        'x': 200,
        'y': 160
    },
    {
        'x': 140,
        'y': 140
    },
    {
        'x': 40,
        'y': 120
    },
    {
        'x': 100,
        'y': 120
    },
    {
        'x': 180,
        'y': 100
    },
    {
        'x': 60,
        'y': 80
    },
    {
        'x': 120,
        'y': 80
    },
    {
        'x': 180,
        'y': 60
    },
    {
        'x': 20,
        'y': 40
    },
    {
        'x': 100,
        'y': 40
    },
    {
        'x': 200,
        'y': 40
    },
    {
        'x': 20,
        'y': 20
    },
    {
        'x': 60,
        'y': 20
    },
    {
        'x': 160,
        'y': 20
    },
]

for location in locations:
    city = City(location['x'], location['y'])
    TourManager.add_city(city)

pop = Population(50, True)
print(f'Initial distance: {pop.get_fittest().get_distance()}')

pop = GeneticAlgorithm.evolve_population(pop)
for i in range(100):
    pop = GeneticAlgorithm.evolve_population(pop)

print(TourManager.number_of_cities())
