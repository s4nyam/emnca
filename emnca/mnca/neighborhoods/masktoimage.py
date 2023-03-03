from PIL import Image
import numpy as np
import os


# Read the text file
with open('mask_c3.txt', 'r') as f:
    lines = f.readlines()

# Convert the lines to a 2D NumPy array
data = []
for line in lines:
    row = [int(x) for x in line.split()]
    data.append(row)
data = np.array(data)

# Add a border of 1s
data = np.pad(data, ((1, 1), (1, 1)), mode='constant', constant_values=1)

# Convert the NumPy array to a PIL image
img = Image.fromarray(data.astype(np.uint8) * 255)
# Save the image file
img.save('mask_c3nh.png')
