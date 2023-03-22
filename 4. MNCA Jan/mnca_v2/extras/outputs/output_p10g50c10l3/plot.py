import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["figure.autolayout"] = True
plt.margins(x=0, y=0)

df = pd.read_excel("output_p10g50c10l3.xlsx")
plt.plot(df['gen'],df['lowest'],label="lowest",color='green', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)
plt.plot(df['gen'],df['mean'],label="mean",color='red', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)
plt.plot(df['gen'],df['best'],label="best",color='yellow', marker='o', linestyle='dashed',
     linewidth=2, markersize=6)
plt.ticklabel_format(style='plain') 


plt.xlabel("Generations")
plt.ylabel("DEFLATE")

fig = plt.gcf()
fig.set_size_inches(10.5, 6.5)
plt.legend()
fig.savefig('output_p10g50c10l3.png', dpi=100)
# plt.show()
