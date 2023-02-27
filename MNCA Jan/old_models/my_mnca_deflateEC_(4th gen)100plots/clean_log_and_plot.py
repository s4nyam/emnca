# Takes input as std.log file and plot the data
payload = []
data_points = []

linewise_data = []


indices = []
final_indices_for_datapoints = []
# string to search in file
word = '-----------------'
with open(r'std.log', 'r') as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line in lines:
        # check if string present on a current line
        if line.find(word) != -1:
            # print(word, 'string exists in file')
            # print('Line Number:', lines.index(line))
            # print('Line:', line)
            indices.append(lines.index(line))

# print(indices)
final_indices_for_datapoints = [x - 1 for x in indices]
# print(final_indices_for_datapoints)

for i in final_indices_for_datapoints:
    # print(lines[i])
    # print(lines[i][24:26])
    data_points.append(lines[i][24:26])

# print("To plot data points: ", data_points)

# print(indices)
starting_indices_for_payload =[x - 5 for x in indices]

# print(starting_indices_for_payload)
for i in starting_indices_for_payload:
    # print("-------------------------------")
    # print("-------------------------------")
    # print("-------------------------------")
    # print(lines[i:i+3])
    payload.append(lines[i:i+3])
    # print("-------------------------------")
    # print("-------------------------------")
    # print("-------------------------------")


# print("To plot payload: ", payload)

# We have payload as data and data points.
print(len(data_points))
print(len(payload))


# -------------------------------
# -------------------------------
# -------------NEW----------------
# --------------CODE---------------
# -------------------------------

import matplotlib.pyplot as plt
import numpy as np
import random
# data = [random.randint(0, 20) for i in range(0, 10)]  #create a list of 10 random numbers
data = data_points
plt.plot(data, color='magenta', marker='o',mfc='pink' ) #plot the data
plt.xticks(range(0,len(data)+1, 1)) #set the tick frequency on x-axis
plt.ylabel('data') #set the label for y axis
plt.xlabel('index') #set the label for x-axis
plt.title("Plotting a list") #set the title of the graph
plt.show() #display the graph



import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = np.array(data_points)
sns.distplot(data,bins="doane",kde=False,hist_kws={"align" : "right"})
plt.show()