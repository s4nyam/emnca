import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init_board(width, height, init_state):
    if init_state == "single cell in center":
        board = np.zeros((height, width), dtype=np.int)
        board[height//2, width//2] = 1
    elif init_state == "random cells with some probability":
        p = 0.5 # probability of a cell being alive
        board = np.random.choice([0, 1], size=(height, width), p=[1-p, p])
    elif init_state == "random cells with 2 different states":
        p1 = 0.4 # probability of a cell being state 1
        board = np.random.choice([0, 1, 2], size=(height, width), p=[1-p1, p1/2, p1/2])
    else:
        raise ValueError("Invalid initial state")
    return board


def update(frame, img, board, neighborhood, range_of_neighborhood_sum):
    new_board = np.zeros_like(board, dtype=int)
    height, width = board.shape
    for i in range(height):
        for j in range(width):
            cell_neighborhood = [board[(i + ni + height) % height, (j + nj + width) % width]
                                 for ni, nj in neighborhood]
            neighborhood_sum = sum(cell_neighborhood)
            for lower, upper, next_state in range_of_neighborhood_sum:
                if lower <= neighborhood_sum <= upper:
                    new_board[i, j] = next_state
    board[:] = new_board[:]
    img.set_data(board)
    return img,


def run_automaton(width, height, steps, init_state, filename, neighborhood, range_of_neighborhood_sum):
    board = init_board(width, height, init_state)
    fig, ax = plt.subplots()
    img = ax.imshow(board, cmap='gray')
    ani = animation.FuncAnimation(fig, update, frames=steps, fargs=(img, board, neighborhood, range_of_neighborhood_sum), repeat=False)
    # ani.save(filename, dpi=80, writer='imagemagick')
    ani.save(filename, dpi=80, writer='pillow')


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


width = 200
height = 200
steps = 100
init_state = "random cells with some probability"


# GoL
# neighborhood = extract_neighborhood_from_file('neighborhoods/8_neighbor.txt')
# range_of_neighborhood_sum = [(2, 3, 1), (3, 3, 1), (4, 8, 0)]
# run_automaton(width, height, steps, init_state, filename, neighborhood, range_of_neighborhood_sum)

# mask_a
neighborhood = extract_neighborhood_from_file('neighborhoods/mask_a.txt')
range_of_neighborhood_sum = [(1,92,1),(93, 100, 0), (101, 199, 0)]

filename = "cellular_automaton"+str(range_of_neighborhood_sum)+".gif"
run_automaton(width, height, steps, init_state, filename, neighborhood, range_of_neighborhood_sum)
