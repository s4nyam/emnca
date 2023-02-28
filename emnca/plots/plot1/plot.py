import pandas as pd
import matplotlib.pyplot as plt

# read the Excel file into a pandas dataframe
df = pd.read_excel('plot_data.xlsx')

# plot the column as a bar chart
plt.plot(df['DEFLATES'])

# set the chart title and axis labels
plt.title('DEFLATE Chart')
plt.xlabel('Generations')
plt.ylabel('DEFLATES')

# save the chart as an image file
plt.savefig('plot.png')
