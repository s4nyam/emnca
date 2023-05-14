import random
from numpy.random import randint
from numpy.random import rand
from mnca_d import cellularautomata



POPULATION_SIZE = 5
mu_rate = 0.1
GENERATION_SIZE = 10



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
    # Child will be Born rule of parent 1 and survive rule of parent 2
    # Another Child will be Born rule of parent 2 and surive rule of parent 1

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
        # print("--------------Generation: ", generation, "--------------")
        deflate_scores = [calculate_deflate(BSrule) for BSrule in pop]
        # Checking new best and best_evaluated
        for i in range(POPULATION_SIZE):
            if(deflate_scores[i]>best_evaluated):
                best, best_evaluated = pop[i], deflate_scores[i]
                print(">%d, new best Born and Survive f(%s) = %.3f" % (generation,  pop[i], deflate_scores[i]))
        # Select Parents
        sortedpop = selection(pop,deflate_scores)
        selected = [sortedpop[len(sortedpop)-1], sortedpop[len(sortedpop)-2]]
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