import numpy as np
import random
w = 100
h = 100
# initial mask

# First 50 steps
# if you want to look steps 51 to 100 then introduce time delta
CA_STEPS = 50
mat = 'center'
radius = 2
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
      grid = np.zeros((w, h),dtype=int)
      probability = 0.3
      for i in range(w*probability):
        grid[random.randint(1,w),random.randint(1,h)] = 1
      return grid
    # Add or infuse component of Multi State CA in the same 
    # random initialisation so that it looks like:
    elif state == 'probab_multistate':
      grid = np.zeros((w, h),dtype=int)
      probability = 0.3
      for i in range(w*probability/2):
        grid[random.randint(1,w),random.randint(1,h)] = 1
      for i in range(w*probability/2):  
        grid[random.randint(1,w),random.randint(1,h)] = 2
      return grid
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
        neighbors.append(element)
  return neighbors



# def cellularautomata(B,D):
def cellularautomata():
    for i in range(CA_STEPS):
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
                if(neighbors_sum>=0 and neighbors_sum<=1):
                    cells_arr[i][j] = 0
                elif(neighbors_sum>=3 and neighbors_sum<=3):
                    cells_arr[i][j] = 1
                elif(neighbors_sum>=4 and neighbors_sum<=8):
                    cells_arr[i][j] = 0
        
        current_state_mat = [[cells_arr[i][j] for i in range(w)] for j in range(h)]
        arr = current_state_mat
        # Store and Append Board Array
        board_arr.append(arr)


    # Calculate Deflate over that board array
    import os
    try:
        os.remove("board_arrays.txt")
        # print("Removed Successfully")
    except:
        pass
    with open("board_arrays.txt", "w") as output:
        output.write(str(board_arr))
    import deflate
    filedata = open('board_arrays.txt', "rb").readline()
    compressed = deflate.gzip_compress(filedata, 6)
    deflate_value = compressed.__sizeof__()
    return deflate_value



# B = [3]
# D = [2,3]
print(cellularautomata())