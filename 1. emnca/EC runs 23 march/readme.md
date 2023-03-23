# EC runs 23 march
The general configuration that all plots follow (from p10g25_1 to p10g25_9)

```python
population = 10
generations = 25
init_state = "random cells with some probability"
width = 100
height = 100
steps = 50
init_state = "random cells with some probability"
# Fixed Neighbohoods
nh1 = extract_neighborhood_from_file('neighborhoods/mask_c1.txt')
nh2 = extract_neighborhood_from_file('neighborhoods/mask_c2.txt')
nh3 = extract_neighborhood_from_file('neighborhoods/mask_c3.txt')
neighborhoods = [nh1,nh2,nh3]
OVERALL_PROBABILITY_ATLEAST = 3 # works as mutation rate
POPULATION_SIZE = 10 #3
GENERATION_SIZE = 25 #3
NUMBER_OF_NEIGHBORHOODS = 3 
NUMBER_OF_BOUNDS_IN_EACH_NEIGHBORHOOD = 3 
total_sum = 3*NUMBER_OF_NEIGHBORHOODS*NUMBER_OF_BOUNDS_IN_EACH_NEIGHBORHOOD
PROBABILITY_OF_INSERTING_A_NEW_RULE = OVERALL_PROBABILITY_ATLEAST/total_sum
PROBABILITY_OF_REMOVING_A_RULE = OVERALL_PROBABILITY_ATLEAST/total_sum
PROBABILITY_OF_CHANGING_A_RULE = OVERALL_PROBABILITY_ATLEAST/total_sum
```

## Some plots and visuals

### p10g25_1.ipynb

EC outputs / notebook - https://github.com/s4nyam/emnca/blob/main/1.%20emnca/EC%20runs%2023%20march/p10g25_1.ipynb

Fitness vs Generation plot









