import numpy as np
from PIL import Image
import sys
import deflate




np.set_printoptions(threshold=sys.maxsize)
# Define grid size
GRID_SIZE = (50, 50)

# Define probability of each cell being active (white cells)
ACTIVE_PROBABILITY = 0.2


plot_data = []
for i in range(50):
    all_boards = []
    for i in range(50):
        # Generate random grid with probabilistic active cells
        grid = np.random.choice([0, 1], size=GRID_SIZE, p=[1 - ACTIVE_PROBABILITY, ACTIVE_PROBABILITY])
        # print(grid)
        # Create PIL image from grid
        all_boards.append(grid)
        # img = Image.fromarray((grid * 255).astype(np.uint8))

        # Save image as PNG file
        # img.save("random_grid_"+str(i)+".png")


    with open("board_arrays.txt", "w") as output:
        output.write(str(all_boards))
    filedata = open('board_arrays.txt', 'r', encoding='utf-8').readlines()
    filedata = ''.join(filedata).encode('utf-8')
    # print(filedata)
    compressed = deflate.gzip_compress(filedata, 8)
    deflate_value = compressed.__sizeof__()
    print(deflate_value)
    import os
    os.system("rm board_arrays.txt")
    plot_data.append(deflate_value)


import matplotlib.pyplot as plt
plt.plot(plot_data)
plt.show()