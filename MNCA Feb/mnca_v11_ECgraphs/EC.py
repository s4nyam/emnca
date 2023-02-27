import numpy as np
import sys
import random
np.set_printoptions(threshold=sys.maxsize)

from mnca import mnca

POPULATION_SIZE = 10
GENERATION_SIZE = 10
NUMBER_OF_NEIGHBORHOODS = 3 # for random number of nh put random function here
NUMBER_OF_BOUNDS_IN_EACH_NEIGHBORHOOD = 3 # for random number of nh bounds put random function here
PROBABILITY_OF_INSERTING_A_NEW_RULE = 0.2
PROBABILITY_OF_REMOVING_A_RULE = 0.1
PROBABILITY_OF_CHANGING_A_RULE = 0.7
# we take average as gene rather than sum because for sum we need to consider radius each time

# TO PLOT DATA

generations = []
mean_deflate = []
best_deflate = []
lowest_deflate = []


# GENERATE RANDOM RULE
def generate_random_rule():
    number_of_neighborhood = NUMBER_OF_NEIGHBORHOODS
    number_of_bounds_in_each_neighborhod_average_or_sum = NUMBER_OF_BOUNDS_IN_EACH_NEIGHBORHOOD
    rule = []
    for i in range(number_of_neighborhood):
        ranges = []
        for j in range(number_of_bounds_in_each_neighborhod_average_or_sum):
            lower = round(random.uniform(0, 1),3)
            upper = round(random.uniform(lower, 1),3)
            new_next_state = random.choice([0, 1]) # for 2 states
            # new_next_state = random.choice([0, 1, 2]) # for 3 states
            ranges.append((lower, upper, new_next_state))
        rule.append(ranges)
    return rule

# print(generate_random_rule())



# POPULATION
def init_population():
    population_size = POPULATION_SIZE
    population = []
    for i in range(population_size):
        individual = generate_random_rule()
        population.append(individual)
    return population


# print(init_population())

# FITNESS / DEFLATE
def calculate_deflate(genotype):
    deflate = mnca(genotype)
    return deflate

# poopulation = init_population()
# print(calculate_deflate(poopulation[0]))


# PROPORTIONATE SELECTION / ROULETTTE WHEEL SELECTION
def roulette_wheel_selection(population, fitness_values):

    sorted_population = [x for _,x in sorted(zip(fitness_values,population))]
    sorted_fitness_scores = [_ for _,x in sorted(zip(fitness_values,population))]
    fitness_values = sorted_fitness_scores
    population = sorted_population
    total_fitness = sum(fitness_values)
    probability_values = [fitness/total_fitness for fitness in fitness_values]
    cumulative_probability = np.cumsum(probability_values)
    selected_index = None
    random_value = random.uniform(0, 1)
    for i in range(len(population)):
        if random_value < cumulative_probability[i]:
            selected_index = i
            break

    return population[selected_index]


# population = init_population()
# print("-----Intial Pop-----")
# print(population)
# print("-----Fitness Values-----")
# fitness_values = [calculate_deflate(individual) for individual in population]
# print(fitness_values)
# print("-----Selected Individual-----")
# selected_individual = roulette_wheel_selection(population, fitness_values)
# print(selected_individual)

# MUTATION FOR ADDING COMPLETELY NEW BOUND. PROMOTEES DIVERSITY.
def mutation(rule):
    try:
        number_of_neighborhoods = len(rule)
        for i in range(number_of_neighborhoods):
            number_of_bounds = len(rule[i])
            for j in range(number_of_bounds):
                prob_insert = PROBABILITY_OF_INSERTING_A_NEW_RULE
                prob_remove = PROBABILITY_OF_REMOVING_A_RULE
                prob_change = PROBABILITY_OF_CHANGING_A_RULE
                random_value = random.uniform(0, 1)
                # insert a value in the rule
                if random_value < prob_insert:
                    new_bound = []
                    lower = round(random.uniform(0, 1),3)
                    upper = round(random.uniform(lower, 1),3)
                    new_next_state = random.choice([0, 1])
                    new_bound.append((lower, upper, new_next_state))
                    rule[i].extend(new_bound)
                # remove a value from the rule
                elif prob_insert <= random_value < prob_insert + prob_remove:
                    rule[i].pop(j)
                    number_of_bounds -= 1
                    j -= 1
                # change a value from the rule
                elif prob_insert + prob_remove <= random_value < prob_insert + prob_remove + prob_change:
                    lower = round(random.uniform(0, 1),3)
                    upper = round(random.uniform(lower, 1),3)
                    new_next_state = random.choice([0, 1])
                    rule[i][j] = (lower, upper, new_next_state)
    except:
        pass
    return rule

# pop = init_population()
# print(pop[0])
# print("------------------------")
# print(mutation(pop[0]))

# # CROSSOVER
# def crossover(parent1, parent2):
#     number_of_neighborhoods = len(parent1)
#     child = []
#     for i in range(number_of_neighborhoods):
#         number_of_bounds = len(parent1[i])
#         bounds = []
#         for j in range(number_of_bounds):
#             parent1_bound = parent1[i][j]
#             parent2_bound = parent2[i][j]
#             random_value = random.uniform(0, 1)
#             if random_value <= 0.5:
#                 bounds.append(parent1_bound)
#             else:
#                 bounds.append(parent2_bound)
#         child.append(bounds)
#     return child


# pop = init_population()
# print("------------------------parent 1--------------------------")
# print(pop[0])

# print("------------------------parent 2--------------------------")
# print(pop[1])
# print("------------------------Child--------------------------")

# print(crossover(pop[0],pop[1]))


# GENETIC ALGORITHM
pop = init_population()
for generation in range(GENERATION_SIZE):
    generations.append(generation)
    # Evaluate the fitness of each chromosome
    fitness_scores = [calculate_deflate(chromosome) for chromosome in pop]
    lowest_deflate.append(min(fitness_scores))
    mean_deflate.append(sum(fitness_scores) / len(fitness_scores))
    best_deflate.append(max(fitness_scores))
    # Select the top-performing chromosomes to form the next generation
    new_pop = []
    for i in range(POPULATION_SIZE//2):
        # Select two chromosomes using tournament selection
        selected = roulette_wheel_selection(pop, fitness_scores)
        # <scope of crossover and child here>
        mutated = mutation(selected)
        print("Generation: {}, Iteration {}, New Best Found Rule set {}".format(generation,str(i),str(mutated)))
        new_pop.extend([mutated])
    pop = new_pop

# Select the chromosome with the highest fitness score from the final generation
fitness_scores = [calculate_deflate(chromosome) for chromosome in pop]
best_chromosome = pop[fitness_scores.index(max(fitness_scores))]
print("FINAL BEST CHROMOSOME IS: {}".format(str(best_chromosome)))
# return best_chromosome


import matplotlib.pyplot as plt
x = generations
y = [lowest_deflate, mean_deflate, best_deflate]

plt.xlabel("Generations")
plt.ylabel("Deflate Values")
plt.title("Deflate chart for 50 steps of the board at each generation")
plt.plot(x,y[0],label="Lowest Deflates")
plt.plot(x,y[1],label="Mean Deflates")
plt.plot(x,y[2],label="Best Deflates")

ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_useOffset(False)
plt.legend()
plt.savefig("P{}.G{}.nh{}.png".format(POPULATION_SIZE,GENERATION_SIZE,NUMBER_OF_NEIGHBORHOODS))
# plt.show()