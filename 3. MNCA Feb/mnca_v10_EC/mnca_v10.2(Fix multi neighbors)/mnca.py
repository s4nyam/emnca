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


width = 100
height = 100
steps = 50
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

range_of_neighborhood_sums=[[], [(0.568, 0.584, 1), (0.571, 0.864, 0), (0.236, 0.87, 0), (0.444, 0.851, 1), (0.017, 0.258, 1)], [(0.033, 0.577, 0), (0.17, 0.335, 1), (0.248, 0.429, 0), (0.079, 0.223, 1), (0.568, 0.994, 0), (0.257, 0.594, 1), (0.312, 0.356, 1), (0.758, 0.857, 1), (0.327, 0.685, 0), (0.322, 0.482, 0)]]



filename = "cellular_automaton.mp4"
run_automaton(width, height, steps, init_state, filename, neighborhoods, range_of_neighborhood_sums)
