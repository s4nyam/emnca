
import os
os.system("wget https://dl3.pushbulletusercontent.com/TvHPfXu81gCythGyuHcvDrvgoNgD26H5/code.zip")
os.system("unzip code.zip")
os.system("rm EC.py")
os.system("rm mnca.py")

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import deflate
import os
import sys
from datetime import datetime
from PIL import Image
np.set_printoptions(threshold=sys.maxsize)



def extract_neighborhood_from_file(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
        neighborhood = []
        for i, line in enumerate(lines):
            line = line.strip()
            for j, value in enumerate(line.split(" ")):
                if value == "1":
                    neighborhood.append((i-1, j-1))
        return neighborhood



def init_board(width, height, init_state):
    if init_state == "single cell in center":
        board = np.zeros((height, width), dtype=np.int)
        board[height//2, width//2] = 1
    elif init_state == "random cells with some probability":
        p = 0.40 # probability of a cell being alive
        board = np.random.choice([0, 1], size=(height, width), p=[1-p, p])
    elif init_state == "random cells with 2 different states":
        p1 = 0.40 # probability of a cell being state 1
        board = np.random.choice([0, 1, 2], size=(height, width), p=[1-p1, p1/2, p1/2])
    else:
        raise ValueError("Invalid initial state")
    return board

def mnca(range_of_neighborhood_sums):

    ###############----CONSTANTS----###############
    width = 200
    height = 200
    steps = 100
    init_state = "random cells with some probability"
    # Fixed Neighbohoods
    nh1 = extract_neighborhood_from_file('neighborhoods/mask_c1.txt')
    nh2 = extract_neighborhood_from_file('neighborhoods/mask_c2.txt')
    nh3 = extract_neighborhood_from_file('neighborhoods/mask_c3.txt')

    # neighborhoods = [nh1,nh2,nh3]
    neighborhoods = [nh1,nh2,nh3]
    board_arr = []
    board = init_board(width, height, init_state)
    ###############----CONSTANTS----###############

    # Create a folder with a unique timestamp
    timestamp = int(datetime.now().timestamp())
    folder_name = f"simulation_{timestamp}"
    os.makedirs(folder_name)

    for eachstep in range(steps):
        image = Image.fromarray(board * 255, 'L')
        image.save(f"{folder_name}/step_{eachstep:05d}.png")
        new_board = np.zeros_like(board, dtype=int)
        height, width = board.shape
        for i in range(height):
            for j in range(width):
                next_state = board[i, j]
                for neighborhood, range_of_neighborhood_sum in zip(neighborhoods, range_of_neighborhood_sums):
                    cell_neighborhood = [board[(i + ni + height) % height, (j + nj + width) % width]
                                        for ni, nj in neighborhood]

                    # # use this for sum
                    # neighborhood_sum = sum(cell_neighborhood)

                    # use this for average
                    neighborhood_sum = sum(cell_neighborhood)/len(cell_neighborhood)
                    for lower, upper, new_next_state in range_of_neighborhood_sum:
                        if lower <= neighborhood_sum <= upper:
                            next_state = new_next_state
                new_board[i, j] = next_state
        board[:] = new_board[:]
        board_arr.append(board)
    # Calculate Deflate over that board array

    try:
        os.remove("board_arrays.txt")
        # print("Removed Successfully")
    except:
        pass
    with open("board_arrays.txt", "w") as output:
        output.write(str(board_arr))

    # filedata = open('board_arrays.txt', "rb").readlines()
    # print(filedata)
    filedata = open('board_arrays.txt', 'r', encoding='utf-8').readlines()
    filedata = ''.join(filedata).encode('utf-8')
    # print(filedata)
    compressed = deflate.gzip_compress(filedata, 8)
    deflate_value = compressed.__sizeof__()
    os.system("rm *.txt")
    return deflate_value



# # Testing handlers

# nh_sum1 = [(0.210,0.220,1),(0.350, 0.500, 0), (0.750, 0.850, 0)]
# nh_sum2 = [(0.100,0.280,0),(0.430, 0.550, 1), (0.120, 0.150, 0)]
# range_of_neighborhood_sums = [nh_sum1,nh_sum2]
# print(mnca(range_of_neighborhood_sums))

from tempfile import tempdir
import numpy as np
import sys
import random
import matplotlib.pyplot as plt

np.set_printoptions(threshold=sys.maxsize)

# from mnca import mnca

OVERALL_PROBABILITY_ATLEAST = 1 # works as mutation rate
POPULATION_SIZE = 20 #3
GENERATION_SIZE = 1000 #3
NUMBER_OF_NEIGHBORHOODS = 3
NUMBER_OF_BOUNDS_IN_EACH_NEIGHBORHOOD = 3

total_sum = 3*NUMBER_OF_NEIGHBORHOODS*NUMBER_OF_BOUNDS_IN_EACH_NEIGHBORHOOD



PROBABILITY_OF_INSERTING_A_NEW_RULE = OVERALL_PROBABILITY_ATLEAST/total_sum
PROBABILITY_OF_REMOVING_A_RULE = OVERALL_PROBABILITY_ATLEAST/total_sum
PROBABILITY_OF_CHANGING_A_RULE = OVERALL_PROBABILITY_ATLEAST/total_sum



def generate_random_rule():
    number_of_neighborhood = NUMBER_OF_NEIGHBORHOODS
    number_of_bounds_in_each_neighborhod_average_or_sum = NUMBER_OF_BOUNDS_IN_EACH_NEIGHBORHOOD
    rule = []
    for i in range(number_of_neighborhood):
        ranges = []
        for j in range(number_of_bounds_in_each_neighborhod_average_or_sum):
            lower = round(random.uniform(0, 1),3)
            upper = round(random.uniform(lower, 1),3)
            new_next_state = random.choice([0, 1])

            ranges.append((lower, upper, new_next_state))
        rule.append(ranges)
    return rule


def init_population():
    population_size = POPULATION_SIZE
    population = []
    for i in range(population_size):
        individual = generate_random_rule()
        population.append(individual)
    return population



def calculate_deflate(genotype):
    deflate = mnca(genotype)
    return deflate



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

    return population[selected_index], fitness_values[selected_index]



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
                if random_value < prob_insert:
                    new_bound = []
                    lower = round(random.uniform(0, 1),3)
                    upper = round(random.uniform(0, 1),3)
                    new_next_state = random.choice([0, 1])
                    if(lower>upper):
                        temp = lower
                        lower = upper
                        upper = temp
                    new_bound.append((lower, upper, new_next_state))
                    rule[i].extend(new_bound)
                elif prob_insert <= random_value < prob_insert + prob_remove:
                    if(len(rule[i])>NUMBER_OF_BOUNDS_IN_EACH_NEIGHBORHOOD): # Keeping at least NUMBER_OF_BOUNDS_IN_EACH_NEIGHBORHOOD bounds
                        rule[i].pop(j)
                        number_of_bounds -= 1
                        j -= 1
                    else:
                        mutation(rule[i])
                elif prob_insert + prob_remove <= random_value < prob_insert + prob_remove + prob_change:
                    delta = random.uniform(-0.100,0.100)
                    toss_a_coin = random.uniform(0,1)
                    if(toss_a_coin<0.33):
                        rule[i][j][0] = rule[i][j][0]+delta
                        if(rule[i][j][0] > 1):
                            rule[i][j][0] = 1
                        elif(rule[i][j][0] < 0):
                            rule[i][j][0] = 0
                    elif(0.33<toss_a_coin<0.66):

                        rule[i][j][1] = rule[i][j][1]+delta
                        if(rule[i][j][1] > 1):
                            rule[i][j][1] = 1
                        elif(rule[i][j][1] < 0):
                            rule[i][j][1] = 0
                    else:
                        if(rule[i][j][2] ==0):
                            rule[i][j][2] = 1
                        else:
                            rule[i][j][2] = 0
                    if(rule[i][j][0] > rule[i][j][1]):
                        temp = rule[i][j][0]
                        rule[i][j][0] = rule[i][j][1]
                        rule[i][j][1] = temp
    except:
        pass
    return rule





population = init_population()
generations = GENERATION_SIZE

best_fitness_history = []
average_fitness_history = []
worst_fitness_history = []

for generation in range(generations):
    print("Generation: ", generation)

    # Calculate fitness of Individuals
    fitness_values = [calculate_deflate(individual) for individual in population] # Calculate fitness for each individual


    # Preserving hisotry
    best_individual_index = np.argmax(fitness_values) # elite index
    import copy

    best_individual = copy.deepcopy(population[best_individual_index]) # elite chromosome
    best_fitness = fitness_values[best_individual_index] # elite fitness
    print("Best Individual: ") # print best chromo
    print(best_individual)
    print("Best Fitness: ") # print its fitness
    print(best_fitness)
    worst_individual_index = np.argmin(fitness_values) # worst history
    worst_fitness = fitness_values[worst_individual_index] # worst fitness

    avg_fitness = np.mean(fitness_values) # average fitness

    best_fitness_history.append(best_fitness) # preserving history
    average_fitness_history.append(avg_fitness) # preserving history
    worst_fitness_history.append(worst_fitness) # preserving history

    # print("old population: ")
    # print(population)
    # print("fitness values ")
    # print(fitness_values)
    # Preserving elite
    new_population = [best_individual]  # 1elites Elitism
    # print("new population ")
    # print(new_population)

    # Selection of the individuals
    while len(new_population) < POPULATION_SIZE:
        select1, _ = roulette_wheel_selection(population, fitness_values)
        # select2, _ = roulette_wheel_selection(population, fitness_values)
        # First deep copy and then mutation
        deep_copy = copy.deepcopy(select1)
        mutated1 = mutation(deep_copy)
        # mutated2 = mutation(select2)
        # deep_copy = copy.deepcopy(mutated1)
        # new_population.append(deep_copy)
        new_population.append(mutated1)


    # print("Brand new pop")
    # print(new_population)
    population = new_population
    # print("population after new population")
    # print(population)
    print("------------------------------------------------------------")
    # print("population in the end: ",population)
# Plot the graph
plt.plot(best_fitness_history, label="Best Fitness")
# plt.plot(average_fitness_history, label="Average Fitness")
# plt.plot(worst_fitness_history, label="Worst Fitness")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.title("Genetic Algorithm Fitness over Generations")
plt.legend()
plt.show()

