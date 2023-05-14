import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["figure.autolayout"] = True
plt.margins(x=0, y=0)

df = pd.read_excel("p10g10c10_curve_data_compare.xlsx")
plt.plot(df['Geneartions'],df['emnca_deflate_lowest'],label="emnca_deflate_lowest",color='indigo', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)
plt.plot(df['Geneartions'],df['emnca_deflate_mean'],label="emnca_deflate_mean",color='blue', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)
plt.plot(df['Geneartions'],df['emnca_deflate_best'],label="emnca_deflate_best",color='cyan', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)

plt.plot(df['Geneartions'],df['emnca_deflate_lowest_highmutation'],label="emnca_deflate_lowest_highmutation",color='tomato', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)
plt.plot(df['Geneartions'],df['emnca_deflate_mean_highmutation'],label="emnca_deflate_mean_highmutation",color='brown', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)
plt.plot(df['Geneartions'],df['emnca_deflate_best_highmutation'],label="emnca_deflate_best_highmutation",color='magenta', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)

plt.plot(df['Geneartions'],df['emnca_deflate_lowest_with_time_delta'],label="emnca_deflate_lowest_with_time_delta",color='yellow', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)
plt.plot(df['Geneartions'],df['emnca_deflate_mean_with_time_delta'],label="emnca_deflate_mean_with_time_delta",color='goldenrod', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)
plt.plot(df['Geneartions'],df['emnca_deflate_best_with_time_delta'],label="emnca_deflate_best_with_time_delta",color='lime', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)

plt.plot(df['Geneartions'],df['emnca_Joint_Compression_lowest_with_time_delta'],label="Joint_Compression_lowest",color='black', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)
plt.plot(df['Geneartions'],df['emnca_Joint_Compression_mean_with_time_delta'],label="Joint_Compression_mean",color='grey', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)
plt.plot(df['Geneartions'],df['emnca_Joint_Compression_best_with_time_delta'],label="Joint_Compression_best",color='silver', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)



plt.ticklabel_format(style='plain') 


plt.xlabel("Generations")
plt.ylabel("DEFLATE")

fig = plt.gcf()
fig.set_size_inches(10.5, 6.5)
plt.legend()
fig.savefig('outputComparative.png', dpi=100)
# plt.show()