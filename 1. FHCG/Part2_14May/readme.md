# This folder contains answers to the questions below:

## 1. We envison to have anotebook that takes inputs in first cell itself. For example, in the notebooks from this folder, the variables that it takes in first cell are:

```Python
rule = [[(0.451, 0.713, 0), (0.449, 0.663, 1), (0.191, 0.52, 1), (0.089, 0.296, 0)], [(0.332, 0.51, 0), (0.084, 0.307, 0), (0.182, 0.465, 1)], [(0.799, 0.902, 0), (0.303, 0.456, 0), (0.835, 0.984, 1)]]
blocksize = 2
# thresholds = [0.005, 0.015, 0.020, 0.022, 0.025, 0.027, 0.030, 0.033, 0.035, 0.038, 0.041, 0.044, 0.047, 0.050, 0.053, 0.056, 0.059, 0.062]
upper_alpha = 0.005 # temp for testing
lower_alpha = 0.062 # temp for testing
width = 100
height = 100
steps = 9
initial_state_probability = 0.06
seed_value = 1
number_of_states = 5
```

## 2. For multi state we need to have even distributionof thresholds with respective state value. For example, if input is 4 states, then we should have even distribution of thresholds from threshold 1 to threshold 2. Where thresholds 1 and 2 are max and min thresholds that can be as input. 

## 3. HD and CG videos as corresponding output for end user to see it.

## Summary:
```python
# Part 2.1
We envision to have a notebook, that takes grid size, block size, number_of_states, etc. as input from user initially (at later stage)

# Part 2.2
For multi-states, we need to have even distribution of thresholds with respective state value. For example, with lets say, input is 4 states, then we should have an even distribution of thresholds from threshold1 to thresholds2 where thresholds 1 and 2 are max and min thresholds that can be as input. 4 states, 2 thresholds (max and min) ==> evenly divide 2 thresholds and assign one state to each of it (something that Hugo et al has done)

# Part 2.3
We should have final output as video HD and then video CG corresponding to each other so that it is easier to track for a person to see the difference.

```