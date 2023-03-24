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

![download](https://user-images.githubusercontent.com/13884479/227126697-df60099a-0640-442e-b927-e99d77502519.png)

Best Rule found:

```
Generation:  24
Best Individual: 
[[(0.091, 0.177, 1), (0.393, 0.993, 1), (0.643, 0.784, 0), (0.525, 0.589, 1)], [(0.371, 0.805, 1), (0.01, 0.223, 1), (0.346, 0.66, 0), (0.264, 0.642, 0), (0.531, 0.657, 1), (0.345, 0.445, 0)], [(0.556, 0.566, 0)]]
Best Fitness: 
127611
```

Output

https://user-images.githubusercontent.com/13884479/227143685-f81199b6-39f3-40a0-a91c-ee39c7998131.mp4


### p10g25_2.ipynb

EC outputs / notebook - https://github.com/s4nyam/emnca/blob/main/1.%20emnca/EC%20runs%2023%20march/p10g25_2.ipynb

Fitness vs Generation plot

![download-1](https://user-images.githubusercontent.com/13884479/227127116-82f86884-656d-41ba-8849-b9efbfa5fcdd.png)


Last Rule found:

```
Generation:  24
Best Individual: 
[[(0.427, 0.972, 0), (0.716, 0.839, 1)], [(0.264, 0.784, 1), (0.479, 0.654, 0), (0.813, 0.894, 1)], [(0.738, 0.821, 1)]]
Best Fitness: 
132442
```

Best Rule found
```
Generation:  23
Best Individual: 
[[(0.427, 0.972, 0), (0.716, 0.839, 1)], [(0.264, 0.784, 1), (0.479, 0.654, 0), (0.813, 0.894, 1)], [(0.738, 0.821, 1)]]
Best Fitness: 
135685
```

Output


https://user-images.githubusercontent.com/13884479/227144020-48e7b9e5-2789-45fe-a9e8-3364915cca56.mp4




### p10g25_3.ipynb

EC outputs / notebook - https://github.com/s4nyam/emnca/blob/main/1.%20emnca/EC%20runs%2023%20march/p10g25_3.ipynb

Fitness vs Generation plot

![download](https://user-images.githubusercontent.com/13884479/227127469-63896575-3add-4b5e-9e0c-ade987d74687.png)


Best Rule found:

```
Generation:  24
Best Individual: 
[[(0.451, 0.713, 0), (0.449, 0.663, 1), (0.191, 0.52, 1), (0.089, 0.296, 0)], [(0.332, 0.51, 0), (0.084, 0.307, 0), (0.182, 0.465, 1)], [(0.799, 0.902, 0), (0.303, 0.456, 0), (0.835, 0.984, 1)]]
Best Fitness: 
135495
```

Output

https://user-images.githubusercontent.com/13884479/227144111-da934475-39e8-4325-9f95-fda8ec127bae.mp4





### p10g25_4.ipynb (File Lost)
<!--
### p10g25_4.ipynb

EC outputs / notebook - https://github.com/s4nyam/emnca/blob/main/1.%20emnca/EC%20runs%2023%20march/p10g25_4.ipynb

Fitness vs Generation plot

![image](https://user-images.githubusercontent.com/13884479/227127897-a4a6d429-3c76-4f13-b7a0-65fcece39478.png)

***(There is no problem with this curve because the difference in drop is not much in numbers, it may be the exceptional case because of the initialisation of the board in that paarticular MNCA)***

Last Rule found:

```
Generation:  24
Best Individual: 
[[(0.222, 0.482, 1), (0.783, 0.877, 0)], [(0.31, 0.526, 0), (0.63, 0.874, 0)], [(0.897, 0.966, 0), (0.358, 0.414, 0)]]
Best Fitness: 
128678
```


Best Rule found:

```
Generation:  17
Best Individual: 
[[(0.222, 0.482, 1), (0.366, 0.752, 1), (0.701, 0.908, 0)], [(0.31, 0.526, 0), (0.63, 0.874, 0)], [(0.897, 0.966, 0), (0.938, 0.977, 1), (0.358, 0.414, 0)]]
Best Fitness: 
133829
```
-->

### p10g25_5.ipynb

EC outputs / notebook - https://github.com/s4nyam/emnca/blob/main/1.%20emnca/EC%20runs%2023%20march/p10g25_5.ipynb

Fitness vs Generation plot

![image](https://user-images.githubusercontent.com/13884479/227128685-0f450862-c8bd-4732-91f1-3e07496c33c2.png)



Best Rule found:

```
Generation:  24
Best Individual: 
[[(0.148, 0.346, 1)], [(0.742, 0.886, 1), (0.593, 0.932, 1), (0.746, 0.884, 0), (0.348, 0.403, 0)], [(0.63, 0.937, 0), (0.043, 0.185, 0), (0.659, 0.819, 1), (0.912, 0.987, 0)]]
Best Fitness: 
137661
```

Output


https://user-images.githubusercontent.com/13884479/227144208-bb4b53bd-1f35-4616-90c5-13a3a46e99ac.mp4



### p10g25_6.ipynb (File lost)


### p10g25_7.ipynb

EC outputs / notebook - https://github.com/s4nyam/emnca/blob/main/1.%20emnca/EC%20runs%2023%20march/p10g25_7.ipynb

Fitness vs Generation plot

![image](https://user-images.githubusercontent.com/13884479/227128984-1bb3d050-c7f7-407c-abba-aac2de8b56a6.png)


Best Rule found:

```
Generation:  24
Best Individual: 
[[(0.651, 0.82, 0)], [(0.823, 0.909, 1), (0.049, 0.277, 1)], [(0.642, 0.962, 0)]]
Best Fitness: 
144211
```

Output:

![cellular_automaton_ (0 651, 0 82, ](https://user-images.githubusercontent.com/13884479/227140405-a260098b-c151-4109-bd59-bf78e4952543.gif)



### p10g25_8.ipynb

EC outputs / notebook - https://github.com/s4nyam/emnca/blob/main/1.%20emnca/EC%20runs%2023%20march/p10g25_8.ipynb

Fitness vs Generation plot

![image](https://user-images.githubusercontent.com/13884479/227129181-89c2587b-6cce-4fbd-b967-045ef0bf1000.png)



Best Rule found:

```
Generation:  24
Best Individual: 
[[(0.236, 0.267, 0), (0.219, 0.301, 1), (0.207, 0.293, 0), (0.808, 0.954, 0)], [(0.27, 0.299, 1)], [(0.641, 0.947, 0)]]
Best Fitness: 
143917
```

Output


https://user-images.githubusercontent.com/13884479/227144263-63da39bb-1826-492b-8d71-48c7bd0bb946.mp4



### p10g25_9.ipynb

EC outputs / notebook - https://github.com/s4nyam/emnca/blob/main/1.%20emnca/EC%20runs%2023%20march/p10g25_9.ipynb

Fitness vs Generation plot

![image](https://user-images.githubusercontent.com/13884479/227129342-5d72ce69-f366-442f-9b19-ac3c798c676d.png)


Last Rule found:

```
Generation:  24
Best Individual: 
[[(0.238, 0.965, 1), (0.059, 0.103, 1), (0.615, 0.885, 0), (0.839, 0.863, 1), (0.86, 0.925, 0), (0.38, 0.71, 1)], [(0.172, 0.772, 0), (0.497, 0.617, 1), (0.305, 0.622, 1), (0.421, 0.569, 1)], [(0.389, 0.501, 0), (0.205, 0.286, 0)]]
Best Fitness: 
131209
```


Best Rule found:

```
Generation:  21
Best Individual: 
[[(0.238, 0.965, 1), (0.059, 0.103, 1), (0.615, 0.885, 0), (0.839, 0.863, 1), (0.86, 0.925, 0), (0.38, 0.71, 1), (0.667, 0.914, 0)], [(0.172, 0.772, 0), (0.497, 0.617, 1), (0.305, 0.622, 1), (0.421, 0.569, 1)], [(0.389, 0.501, 0), (0.205, 0.286, 0)]]
Best Fitness: 
133641
```

***(Notice that last and best rule are same. In fact the slight bend we are seeing is because of the initialisation)***


(Some metaphors - https://youtu.be/A_6fxpraulg and other videos on his channel)

