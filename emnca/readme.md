
### 1. emnca (folder)

(/Users/sanyamjain/Desktop/RA/mnca/mnca/emnca/emnca)

Genetic Algorithm to evolve new rules. It takes input concatenated board array and result deflate score which works as fitness value. The hypothesis is, DEFLATE is able to capture randomness and order in input data.

This folder contains EC.py and mnca.py where EC.py works as Genetic Algorithm driver and mnca.py is a utility that takes input as rule set and results deflate score.

#### 1.1 mnca.py 
(/Users/sanyamjain/Desktop/RA/mnca/mnca/emnca/emnca/mnca.py)

The role of this function is just to take Born and Death rule as input (if-then-else rules) and returns DEFLATE value

mnca.py with fixed parameters
```python
    ###############----CONSTANTS----###############
    width = 100
    height = 100
    steps = 50
    init_state = "random cells with some probability"
    # Fixed Neighbohoods
    nh1 = extract_neighborhood_from_file('neighborhoods/mask_c1.txt')
    nh2 = extract_neighborhood_from_file('neighborhoods/mask_c2.txt')
    nh3 = extract_neighborhood_from_file('neighborhoods/mask_c3.txt')

    # neighborhoods = [nh1,nh2,nh3]
    neighborhoods = [nh1,nh2]
    board_arr = []
    board = init_board(width, height, init_state)
    ###############----CONSTANTS----###############
```
and to test fnctionality of mnca.py
```python
# Testing handlers
nh_sum1 = [(0.210,0.220,1),(0.350, 0.500, 0), (0.750, 0.850, 0)]
nh_sum2 = [(0.100,0.280,0),(0.430, 0.550, 1), (0.120, 0.150, 0)]
range_of_neighborhood_sums = [nh_sum1,nh_sum2]
print(mnca(range_of_neighborhood_sums))
# results deflate value
```

#### 1.2 EC.py 
(/Users/sanyamjain/Desktop/RA/mnca/mnca/emnca/emnca/EC.py)

This is actual driver code which evolves new rules.

EC.py fixed parameters
```python
OVERALL_PROBABILITY_ATLEAST = 1 # at least 1 rule will be chosen for mutation in each generation
POPULATION_SIZE = 10
GENERATION_SIZE = 10
NUMBER_OF_NEIGHBORHOODS = 3 # for random number of nh put random function here
NUMBER_OF_BOUNDS_IN_EACH_NEIGHBORHOOD = 3 # for random number of nh bounds put random function here
total_sum = 3*NUMBER_OF_NEIGHBORHOODS*NUMBER_OF_BOUNDS_IN_EACH_NEIGHBORHOOD
# total_sum = 3*POPULATION_SIZE*NUMBER_OF_NEIGHBORHOODS*NUMBER_OF_BOUNDS_IN_EACH_NEIGHBORHOOD
PROBABILITY_OF_INSERTING_A_NEW_RULE = OVERALL_PROBABILITY_ATLEAST/total_sum
PROBABILITY_OF_REMOVING_A_RULE = OVERALL_PROBABILITY_ATLEAST/total_sum
PROBABILITY_OF_CHANGING_A_RULE = OVERALL_PROBABILITY_ATLEAST/total_sum
# we take average as gene rather than sum because for sum we need to consider radius each time
```

Key information about EC:

Initial Population = Random Rule List of neighborhood sums with tuple as ```[(lower, upper, new_next_state)]```
<image of A pictorial explanation for a population>

Selection = Roulette Wheel Selection / Proportionate Selection

Mutation = ```insert a value in the tuple rule```, ```remove a tuple from the rule``` and ```change a tuple from the rule by adding or subtracting a small delta ```






### 2. mnca (folder)

/Users/sanyamjain/Desktop/RA/mnca/mnca/emnca/mnca

This script takes input neighborhood and rule sets which output to gif animation of that rule set.

```python
nh1 = extract_neighborhood_from_file('neighborhoods/mask_c1.txt')
nh2 = extract_neighborhood_from_file('neighborhoods/mask_c2.txt')
nh3 = extract_neighborhood_from_file('neighborhoods/mask_c3.txt')
neighborhoods = [nh1,nh2,nh3]

# Slcakermanz known rule
nh_sum1 = [(0.210,0.220,1),(0.350, 0.500, 0), (0.750, 0.850, 0)]
nh_sum2 = [(0.100,0.280,0),(0.430, 0.550, 1), (0.120, 0.150, 0)]
range_of_neighborhood_sums = [nh_sum1,nh_sum2]

filename = "cellular_automaton_"+str(range_of_neighborhood_sums)[0:10]+".mp4"
run_automaton(width, height, steps, init_state, filename, neighborhoods, range_of_neighborhood_sums)
```
