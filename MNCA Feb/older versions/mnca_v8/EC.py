# Giving High Mutation

# python3 EC.py [population] [generation] [crossover] [loop]

import random
from numpy.random import randint
from numpy.random import rand
from mnca_d import cellularautomata
import sys
import os
os.system("pip install deflate")
try:
    arguments = sys.argv
except:
    print("No arguments given so taking pop=5,gen_size=5 and cross=5")
    arguments = [5,5,5]

generations = []
mean_deflate = []
best_deflate = []
lowest_deflate = []

POPULATION_SIZE = int(sys.argv[1])
mu_rate = 0.9
GENERATION_SIZE = int(sys.argv[2])
CROSSOVER_DIVERSITY = int(sys.argv[3])
# LOOP_SIZE_GENERATION = int(sys.argv[4])
# read as GENERATION_SIZE=5 generations that grow for LIMIT_GENERATION_GROWTH=10 best individuals


# Helper Functions
def randomListGenerator():
    rand_list = []
    size = random.randint(1,8)
    for i in range(size):
        rand_list.append(random.randint(1,8))
    return rand_list





# iniit population
def init_population(pop_size):
    init_pop = []
    for i in range(pop_size):
        born_rule = randomListGenerator()
        survive_rule = randomListGenerator()
        init_pop.append([born_rule]+[survive_rule])
    return init_pop





# Fitness / Objective
# Later need to edit for actual deflate value
def calculate_deflate(BSrule):
    # print("Rule Received: B - "+ str(BSrule[0])+ " S - "+ str(BSrule[1]))
    B = BSrule[0]
    S = BSrule[1]
    deflate = cellularautomata(B,S)
    
    return deflate



# Selection
def selection(pop,deflate_scores):

    # select rule that has highest deflate_score
    sorted_pop = [x for _,x in sorted(zip(deflate_scores,pop))]
    # pop = sorted_pop
    # return sorted_pop[len(sorted_pop)-1]
    return sorted_pop





def crossover(parent1,parent2):
    import time
    l_p1_b = len(parent1[0])
    l_p1_s = len(parent1[1])
    l_p2_b = len(parent2[0])
    l_p2_s = len(parent2[1])
    # And also flipping rulesets with some changes and some places
    if(l_p1_b in [0,1]):
        l_p1_b = 2
    if(l_p1_s in [0,1]):
        l_p1_s = 2
    if(l_p2_b in [0,1]):
        l_p2_b = 2
    if(l_p2_s in [0,1]):
        l_p2_s = 2

    try:
        for i in range(CROSSOVER_DIVERSITY):
            parent1[0][random.randint(1,l_p1_b-1)] = random.randint(1,8)
            parent1[1][random.randint(1,l_p1_s-1)] = random.randint(1,8)
            parent2[0][random.randint(1,l_p2_b-1)] = random.randint(1,8)
            parent2[1][random.randint(1,l_p2_s-1)] = random.randint(1,8)
        # Child will be Born rule of parent 1 and survive rule of parent 2
        # Another Child will be Born rule of parent 2 and surive rule of parent 1
    except:
        pass
    c1 = [parent1[0], parent2[1]]
    c2 = [parent2[0], parent1[1]]
    return [c1,c2]


# Born Survive ruleset is a chromosome
def mutation(ruleset,mu_rate):
    for i in range(len(ruleset)):
        if(rand()<mu_rate):
            ruleset = [randomListGenerator(),randomListGenerator()]
    return ruleset

def GA():
    pop = init_population(POPULATION_SIZE)
    best,best_evaluated = 0, calculate_deflate(pop[0])
    for generation in range(GENERATION_SIZE):
        generations.append(generation)
        # print("--------------Generation: ", generation, "--------------")
        deflate_scores = [calculate_deflate(BSrule) for BSrule in pop]
        # Checking new best and best_evaluated
        temp_deflate = []
        for i in range(POPULATION_SIZE):
            if(deflate_scores[i]>best_evaluated):
                best, best_evaluated = pop[i], deflate_scores[i]
                print("Generation >%d, new best Born and Survive f(%s) = %.3f" % (generation,  pop[i], deflate_scores[i]))
                temp_deflate.append(best_evaluated)
        mean_deflate.append(sum(temp_deflate)/len(temp_deflate))
        best_deflate.append(max(temp_deflate))
        lowest_deflate.append(min(temp_deflate))
        # Select Parents
        sortedpop = selection(pop,deflate_scores)
        # Selecting best 2 parents
        selected = [sortedpop[len(sortedpop)-1], sortedpop[len(sortedpop)-2]]
        # selecting 1 best and 1 average for diversity
        # selected = [sortedpop[len(sortedpop)-1], sortedpop[int(len(sortedpop)/2)-1]]
        # Creating next generation
        children = []
        for i in range(0, POPULATION_SIZE, 2):
            parent1,parent2 = selected[0], selected[1]
            # Crossover and mutate
            for c in crossover(parent1,parent2):
                mutation(c,mu_rate)
                children.append(c)
        #replace pop
        pop = children
    return [best, best_evaluated]

best,score = GA()
print("Final Best: ", best)
print("Best Score this rules has: ", score)

import matplotlib.pyplot as plt
x = generations
y = [lowest_deflate, mean_deflate, best_deflate]
string = ['lowest_deflate', 'mean_deflate', 'best_deflate']
print("printing generations")
print(x)
print("printing DEFLATEs")
print(y)


plt.xlabel("Generations")
plt.ylabel("Deflate Values")
plt.title("Deflate chart for 50 steps of the board at each generation")
plt.plot(x,y[0],label="Lowest Deflates")
plt.plot(x,y[1],label="Mean Deflates")
plt.plot(x,y[2],label="Best Deflates")


ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_useOffset(False)
plt.legend()
plt.savefig("output_p"+str(POPULATION_SIZE)+"g"+str(GENERATION_SIZE)+"c"+str(CROSSOVER_DIVERSITY)+".png")
# plt.show()