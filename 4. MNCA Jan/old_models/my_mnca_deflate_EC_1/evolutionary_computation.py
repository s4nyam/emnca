

import numpy as np

import random

# LIFE = "Life"
# DEATH = "Death"
# # Number of individuals in each generation
# POPULATION_SIZE = 10



def mutate_genes():

    LIFE = "Life"
    DEATH = "Death"
    # Number of individuals in each generation



    # Valid genes
    life_or_death_genes = [LIFE, DEATH]
    neighborhoods_genes = [0,1,2,3,4,5,6,7,8]
    lod_gene = random.choice(life_or_death_genes)
    nh_gene1 = random.choice(neighborhoods_genes)
    nh_gene2 = random.choice(neighborhoods_genes)
    return ([nh_gene1,nh_gene2,lod_gene])

def create_genome():

    LIFE = "Life"
    DEATH = "Death"
    # Number of individuals in each generation



    # Target string to be generated (It could be known life rule) it is GoL rule
    TARGET = [[0,1,DEATH],[3,3,LIFE],[4,8,DEATH],[2,3,LIFE]]

    return [mutate_genes() for _ in range(len(TARGET))]

def mate(chr1,chr2):
    child_chromosome = []
    chromosome1 = chr1
    chromosome2 = chr2
    for gene1, gene2 in zip(chromosome1,chromosome2):
        prob = random.random()
        if(prob<0.45):
            child_chromosome.append(gene1)
        if(prob<0.90 and prob>0.45):
            child_chromosome.append(gene2)
        else:
            child_chromosome.append(mutate_genes())
    return child_chromosome

def cal_fitness(chromosome):
    fitness_value = 0
    # chromosome = [[5,2,LIFE],[1,2,DEATH],[2,3,LIFE],[1,2,DEATH]]
    # target = [[0,1,DEATH],[3,3,LIFE],[4,8,DEATH],[2,3,LIFE]]
    LIFE = "Life"
    DEATH = "Death"
    # Target string to be generated (It could be known life rule) it is GoL rule
    CHROMO = [[0,1,DEATH],[3,3,LIFE],[4,8,DEATH],[2,3,LIFE]]
    TARGET = [[0,1,DEATH],[3,3,LIFE],[4,8,DEATH],[2,3,LIFE]]
    target = TARGET
    countloop=0
    for eachgene_c in chromosome:
        for eachgene_t in target:
            countloop=countloop+1
            # if(eachgene_c[0]-eachgene_t[0]!=0 or eachgene_c[1]-eachgene_t[1]!=0 or eachgene_t[2]!=eachgene_c[2]):
            if(countloop in [2,3,4,5,7,8,9,10,12,13,14,15]):
                continue
            
            
            if(eachgene_c[0]-eachgene_t[0]!=0 and eachgene_c[1]-eachgene_t[1]!=0 and eachgene_t[2]!=eachgene_c[2]):
                fitness_value = fitness_value+1
    return fitness_value


 


def EvolutionaryComputation(ec_list,deflate_size):
    LIFE = "Life"
    DEATH = "Death"
    POPULATION_SIZE = 5
    # Target string to be generated (It could be known life rule) it is GoL rule
    TARGET = [[0,1,DEATH],[3,3,LIFE],[4,8,DEATH],[2,3,LIFE]]


    population = []
    generation = 1
    found = False
    # create initial population
    for _ in range(POPULATION_SIZE):
        gnome = create_genome()
        population.append(gnome)
    fitness_scores = []
    while not found:
        # sort the population in increasing order of fitness score
        for i in range(len(population)):
            fitness_scores.append(cal_fitness(population[i]))
        indices = np.argsort(fitness_scores)
        population = [x for _, x in sorted(zip(indices, population))]
        # if (cal_fitness(population[0]) <=2 and deflate_size):
        if (deflate_size <= 78 and deflate_size >= 61 and cal_fitness(population[0])>=8):
            found = True
            break
        
        if(deflate_size == 60 or generation >=40):
            break

        new_gen = []
        new_gen.append(ec_list)
        s = int((10*POPULATION_SIZE)/100)
        new_gen.extend(population[:s])
        s = int((89*POPULATION_SIZE)/100)
        for _ in range(s):
            parent1 = random.choice(population[:s])
            parent2 = random.choice(population[:s])
            child = mate(parent1, parent2)
            new_gen.append(child)
        ec_list = population[0]
        population = new_gen
        generation += 1
        
        print("Generation: {}\t Fitness: {}\t Deflate: {}".format(str(generation), str(cal_fitness(population[0])), str(deflate_size)))
    print("Generation: {}\t Fitness: {}\t Deflate: {}".format(str(generation), str(cal_fitness(population[0])), str(deflate_size)))
    # ec_list = population[0]
    return population[0]
