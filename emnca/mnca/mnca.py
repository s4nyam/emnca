import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init_board(width, height, init_state):
    if init_state == "single cell in center":
        board = np.zeros((height, width), dtype=np.int)
        board[height//2, width//2] = 1
    elif init_state == "random cells with some probability":
        p = 0.250 # probability of a cell being alive
        board = np.random.choice([0, 1], size=(height, width), p=[1-p, p])
    elif init_state == "random cells with 2 different states":
        p1 = 0.250 # probability of a cell being state 1
        board = np.random.choice([0, 1, 2], size=(height, width), p=[1-p1, p1/2, p1/2])
    else:
        raise ValueError("Invalid initial state")
    return board


def update(frame, img, board, neighborhoods, range_of_neighborhood_sums):
    new_board = np.zeros_like(board, dtype=int)
    height, width = board.shape
    for i in range(height):
        for j in range(width):
            next_state = board[i, j]
            for neighborhood, range_of_neighborhood_sum in zip(neighborhoods, range_of_neighborhood_sums):
                cell_neighborhood = [board[(i + ni + height) % height, (j + nj + width) % width]
                                     for ni, nj in neighborhood]
                
                # # use this for sum
                # neighborhood_sum = sum(cell_neighborhood)
                
                # use this for average
                neighborhood_sum = sum(cell_neighborhood)/len(cell_neighborhood)
                for lower, upper, new_next_state in range_of_neighborhood_sum:
                    if lower <= neighborhood_sum <= upper:
                        next_state = new_next_state
            new_board[i, j] = next_state
    board[:] = new_board[:]
    img.set_data(board)
    return img,

def run_automaton(width, height, steps, init_state, filename, neighborhoods, range_of_neighborhood_sums):
    board = init_board(width, height, init_state)
    fig, ax = plt.subplots()
    plt.axis('off')
    img = ax.imshow(board, cmap='gist_earth')
    ani = animation.FuncAnimation(fig, update, frames=steps, fargs=(img, board, neighborhoods, range_of_neighborhood_sums), repeat=False)
    # ani.save(filename, dpi=80, writer='imagemagick')
    ani.save(filename, dpi=200, writer='ffmpeg', codec='h264')



def extract_neighborhood_from_file(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
        neighborhood = []
        for i, line in enumerate(lines):
            line = line.strip()
            for j, value in enumerate(line.split(" ")):
                if value == "1":
                    neighborhood.append((i-1, j-1))
        return neighborhood


width = 500
height = 350
steps = 100
init_state = "random cells with some probability"


# GoL
# neighborhoods = [extract_neighborhood_from_file('neighborhoods/8_neighbor.txt')]
# range_of_neighborhood_sums = [[(2, 3, 1), (3, 3, 1), (4, 8, 0)]]
# run_automaton(width, height, steps, init_state, filename, neighborhoods, range_of_neighborhood_sums)

# mask_a and mask_b
# ref - https://slackermanz.com/understanding-multiple-neighborhood-cellular-automata/


nh1 = extract_neighborhood_from_file('neighborhoods/mask_c1.txt')
nh2 = extract_neighborhood_from_file('neighborhoods/mask_c2.txt')
nh3 = extract_neighborhood_from_file('neighborhoods/mask_c3.txt')
neighborhoods = [nh1,nh2,nh3]

# # Slcakermanz known rule
# nh_sum1 = [(0.210,0.220,1),(0.350, 0.500, 0), (0.750, 0.850, 0)]
# nh_sum2 = [(0.100,0.280,0),(0.430, 0.550, 1), (0.120, 0.150, 0)]
# range_of_neighborhood_sums = [nh_sum1,nh_sum2]


# Found rule through EC
# range_of_neighborhood_sums_21feb = [[(0.317, 0.917, 0)], [(0.176, 0.397, 1), (0.619, 0.706, 0), (0.966, 0.97, 1)], [(1, 1, 0)]]
# range_of_neighborhood_sums=[[(0.375, 0.614, 1), (0.152, 0.183, 1), (0.542, 0.962, 0), (0.12, 0.948, 1), (0.099, 0.22, 0), (0.318, 0.348, 0), (0.389, 0.728, 1), (0.107, 0.309, 1), (0.391, 0.413, 0), (0.384, 0.677, 0), (0.698, 0.847, 0), (0.021, 0.497, 1), (0.27, 0.337, 1), (0.39, 0.718, 0), (0.107, 0.883, 0), (0.521, 0.944, 1), (0.883, 0.974, 1), (0.112, 0.665, 1), (0.109, 0.968, 0), (0.643, 0.846, 0)], [], []]

# 22 feb
# range_of_neighborhood_sums=[[], [], [(0.036, 0.122, 1), (0.181, 0.578, 0), (0.14, 0.146, 1), (0.508, 0.617, 0), (0.381, 0.869, 1), (0.099, 0.367, 1), (0.594, 0.951, 1), (0.197, 0.334, 1), (0.387, 0.619, 0), (0.617, 0.857, 1), (0.168, 0.731, 0), (0.082, 0.751, 0), (0.292, 0.587, 0), (0.136, 0.25, 0), (0.359, 0.784, 1), (0.15, 0.684, 0), (0.276, 0.639, 1), (0.046, 0.522, 0), (0.503, 0.553, 0), (0.239, 0.955, 1), (0.502, 0.807, 0), (0.22, 0.858, 1), (0.387, 0.713, 1), (0.613, 0.946, 1), (0.613, 0.862, 0)]] # 142687
range_of_neighborhood_sums=[[(0.071, 0.62, 1), (0.06, 0.189, 1), (0.376, 0.389, 0), (0.449, 0.866, 0), (0.444, 0.789, 1), (0.466, 0.748, 0), (0.01, 0.436, 1), (0.199, 0.495, 1), (0.511, 0.781, 0), (0.308, 0.386, 0), (0.366, 0.502, 1), (0.519, 0.686, 0)], [], []] #with fitness score 119661



filename = "cellular_automaton_"+str(range_of_neighborhood_sums)[0:10]+".mp4"
run_automaton(width, height, steps, init_state, filename, neighborhoods, range_of_neighborhood_sums)
