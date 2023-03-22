import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation
w = 500
h = 500
# initial mask

# First 50 steps
# if you want to look steps 51 to 100 then introduce time delta
CA_STEPS = 50
mat = 'probab_random'
radius = 5
board_arr = []
def start_state(w, h, state):
    # Initialise Single Cell in center.
    if state == 'center':
      center = np.zeros((w, h),dtype=int)
      pos = int(w/2)
      center[pos,pos] = 1
      return center
    # Initialise random cells in the grid with probability.  
    elif state == 'probab_random':
        p = 0.1
        grid = np.random.randint(0, 2, (w,h))
        for j in range(int(100*w*(1-p))):
            randpos_i = np.random.randint(1,w)
            randpos_j = np.random.randint(1,h)
            grid[randpos_i,randpos_j] = 0
        return grid
    # Add or infuse component of Multi State CA in the same 
    # random initialisation so that it looks like:
    elif state == 'probab_multistate':
      grid = np.zeros((w, h),dtype=int)
      probability = 0.3
      for i in range(int(w*probability/2)):
        grid[random.randint(1,w-1),random.randint(1,h-1)] = 1
      for i in range(int(w*probability/2)):  
        grid[random.randint(1,w-1),random.randint(1,h-1)] = 2
      return grid
    elif state == 'random':
        return np.random.randint(0, 2, (w, h))
    else:
        print('wrong dimensions')



# Sum r1 = 8 elements
# Sum r2 = 24 elements
# Sum r3 = 48 elements
# Sum r4 = 80 elements
# and so on...

# This function takes as input a 2D array array, and the indices i and j 
# of the element for which you want to find the neighbors. The radius r 
# determines how far away from the element you want to search for neighbors.
# The function returns a list of the elements in the neighborhood.
def find_neighbors(array, i, j, r):
  neighbors = []
  for x in range(i-r, i+r+1):
    for y in range(j-r, j+r+1):
      if x >= 0 and x < len(array) and y >= 0 and y < len(array[0]):
        element = array[x][y]
        if(x!=i and x!=j):
            neighbors.append(element)
  return neighbors



# def cellularautomata(B,D):
def cellularautomata():
    # Evolve CA
    initial_mat = start_state(w, h, state=mat)
    neighbors_sum=0
    my_cells=[initial_mat[i, j] for i in range(w) for j in range(h)]
    cells_arr = np.asarray(my_cells).reshape(w, h)
    for i in range(w):
        for j in range(h):

            # Neighbor sum goes here
            current_state = cells_arr[i,j]
            neighbors_array = find_neighbors(cells_arr,i,j,radius)
            neighbors_sum = np.sum(neighbors_array)
            
            # Rule Set goes here - GoL
            if(neighbors_sum>=0 and neighbors_sum<=33):
                cells_arr[i][j] = 0
            elif(neighbors_sum>=34 and neighbors_sum<=45):
                cells_arr[i][j] = 1
            elif(neighbors_sum>=58 and neighbors_sum<=121):
                cells_arr[i][j] = 0
    
    current_state_mat = [[cells_arr[i][j] for i in range(w)] for j in range(h)]
    # Store and Append Board Array
    return current_state_mat





def animate(itr):
    
    ax.cla()
    arr = cellularautomata()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.imshow(arr, cmap=cm.gist_earth, interpolation='nearest')


# B = [3]
# D = [2,3]


fig, ax = plt.subplots()
plt.gca().set_axis_off()
plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
plt.margins(0,0)
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())
# plt.style.use('classic')
animation = FuncAnimation(fig, animate, 50)

# plt.show()
animation.save('op.gif', writer='PillowWriter')
plt.close()

