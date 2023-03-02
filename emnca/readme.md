
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


### Found New rules (March 3rd)

1. [[(0.054, 0.55, 1), (0.152, 0.411, 0), (0.747, 0.978, 0), (0.179, 0.27, 1), (0.544, 0.589, 1), (0.646, 0.856, 0), (0.23, 0.923, 0), (0.008, 0.342, 1), (0.136, 0.462, 1), (0.413, 0.955, 0), (0.09, 0.253, 0), (0.236, 0.526, 1), (0.324, 0.372, 0), (0.765, 0.818, 0)], [(0.438, 0.773, 1), (0.367, 0.69, 0), (0.302, 0.872, 1), (0.424, 0.49, 0)], [(0.373, 0.39, 0), (0.788, 0.827, 1)]]	with fitness 119698

![cellular_automaton_ (0 054, ](https://user-images.githubusercontent.com/13884479/222593047-7edb49d6-767e-44e1-b375-ef0c15f9e7db.gif)


2. [[(0.054, 0.55, 1), (0.152, 0.411, 0), (0.747, 0.978, 0), (0.179, 0.27, 1), (0.544, 0.589, 1), (0.646, 0.856, 0), (0.23, 0.923, 0), (0.008, 0.342, 1), (0.136, 0.462, 1), (0.413, 0.955, 0), (0.09, 0.253, 0), (0.236, 0.526, 1), (0.324, 0.372, 0), (0.765, 0.818, 0)], [(0.438, 0.773, 1), (0.367, 0.69, 0), (0.302, 0.872, 1), (0.424, 0.49, 0)], [(0.373, 0.39, 0), (0.788, 0.827, 1), (0.173, 0.452, 0)]]	with fitess 115286

![cellular_automaton_ (0 054,  copy](https://user-images.githubusercontent.com/13884479/222593065-069e704f-6e57-4d21-9e0a-fcf1f389d872.gif)


3. [[(0.329, 0.827, 0), (0.19, 0.996, 0), (0.393, 0.725, 1), (0.486, 0.978, 1), (0.091, 0.905, 0), (0.518, 0.539, 0), (0.908, 0.975, 0)], [(0.13, 0.734, 1), (0.317, 0.917, 0), (0.426, 0.963, 0), (0.46, 0.508, 1), (0.809, 0.814, 1)], [(0.268, 0.483, 1), (0.066, 0.211, 0)]]	with fitness 131456

![cellular_automaton_ (0 329, ](https://user-images.githubusercontent.com/13884479/222593087-829711fc-53e4-4b45-8b90-ccd729532309.gif)


4. [[(0.853, 0.973, 0), (0.411, 0.774, 0), (0.186, 0.928, 0)], [(0.535, 0.848, 0), (0.093, 0.124, 0)], [(0.063, 0.54, 0), (0.536, 0.704, 0), (0.184, 0.333, 1), (0.313, 0.547, 1), (0.27, 0.285, 1)]]	with fitness 141086

![cellular_automaton_ (0 853, ](https://user-images.githubusercontent.com/13884479/222593122-578d5993-07fd-46cd-bd4c-97127c9a3927.gif)



