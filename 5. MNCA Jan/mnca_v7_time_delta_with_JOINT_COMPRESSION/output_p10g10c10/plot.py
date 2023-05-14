import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["figure.autolayout"] = True
plt.margins(x=0, y=0)

df = pd.read_excel("p10g10c10_curve_data.xlsx")
plt.plot(df['Geneartions'],df['emnca_Joint_Compression_lowest_with_time_delta'],label="JCA_LOWEST",color='green', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)
plt.plot(df['Geneartions'],df['emnca_Joint_Compression_mean_with_time_delta'],label="JCS_MEAN",color='red', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)
plt.plot(df['Geneartions'],df['emnca_Joint_Compression_best_with_time_delta'],label="JCS_BEST",color='yellow', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)
plt.ticklabel_format(style='plain') 


plt.xlabel("Generations")
plt.ylabel("DEFLATE")

fig = plt.gcf()
fig.set_size_inches(10.5, 6.5)
plt.legend()
fig.savefig('p10g10c10_curve_data.png', dpi=100)
# plt.show()