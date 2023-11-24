from components.city import City
from components.genetic_algorithm import GeneticAlgorithm
from components.population import Population
from components.tour_manager import TourManager
import matplotlib.pyplot as plt

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

fittest_vals = []
iterations = 200
population = 50
initial_distance = 0

for location in locations:
    city = City(location['x'], location['y'])
    TourManager.add_city(city)

pop = Population(population, True)
initial_distance = pop.get_fittest().get_distance()

pop = GeneticAlgorithm.evolve_population(pop)
for i in range(iterations):
    pop = GeneticAlgorithm.evolve_population(pop)
    fittest_vals.append(pop.get_fittest().get_distance())

# Datos para el primer gráfico
generations = [i for i in range(0, iterations)]

# Datos para el segundo gráfico
x_coords = [location['x'] for location in locations]
y_coords = [location['y'] for location in locations]

best_tour = pop.get_fittest().tour

x_lines = [location.get_x() for location in best_tour]
y_lines = [location.get_y() for location in best_tour]

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Primer gráfico: Comportamiento del algoritmo
axs[0].plot(generations, fittest_vals)
axs[0].set_title('Mejora de los individuos')
axs[0].set_xlabel('Generaciones')
axs[0].set_ylabel('Mejor valor fitness')

# Segundo gráfico: Recorrido del viajero
axs[1].plot(x_lines + [x_lines[0]], y_lines + [y_lines[0]], color='blue', linestyle='-', linewidth=2, label='Recorrido', zorder=1)
axs[1].scatter(x_coords, y_coords, color='red', marker='o', label='Ciudades', zorder=2)
axs[1].scatter(x_coords[0], y_coords[0], color='green', marker='o', label='Inicio', zorder=3)
axs[1].set_title('Recorrido del viajero')
axs[1].set_xlabel('Eje x')
axs[1].set_ylabel('Eje y')
axs[1].grid(which='both', linestyle='--', linewidth=0.5)
axs[1].xaxis.set_major_locator(plt.MultipleLocator(20))
axs[1].yaxis.set_major_locator(plt.MultipleLocator(20))
axs[1].legend()

# Información detallada
axs[0].text(0, -0.2, f'Distancia inicial: {initial_distance}', ha='left', va='center', fontsize=10, transform=axs[0].transAxes)
axs[0].text(0, -0.28, f'Distancia final: {pop.get_fittest().get_distance()}', ha='left', va='center', fontsize=10, transform=axs[0].transAxes)

""" chunks = [best_tour[i:i+4] for i in range(0, len(best_tour), 4)]
str_tour = '\n'.join([' '.join([f"[{location.get_x()}, {location.get_y()}]" for location in chunk]) for chunk in chunks]) """

""" str_tour = [{location.get_x(), location.get_y()} for location in best_tour]
axs[0].text(0, -0.5, f'Solution:\n{str_tour}', ha='left', va='center', fontsize=8, transform=axs[0].transAxes) """

plt.tight_layout()

plt.show()
