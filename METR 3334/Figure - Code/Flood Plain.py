import pandas as pd
import matplotlib.pyplot as plt

plotdata = pd.DataFrame({

    "Easton":[45, 46, 9],

    "Lambertville":[58, 32, 10],

    "Total":[51, 38, 10]},

    index=["Yes", "No", "Don't Know"])

ax = plotdata.plot(kind="bar",figsize=(12, 6), color = ["#23a0da", "#fc6b04", "#a1b1af"], edgecolor = "white", linewidth = 3, zorder = 1)

positions = [10, 20, 30, 40, 50, 60, 70]  # Change these values according to your needs
for pos in positions:
    plt.axhline(y=pos, color='gray', linestyle='-', linewidth=1, zorder = 0)

plt.title("Percent Living in a Floodplain", size = 25)
plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.25), ncol = 3)
plt.ylim(0, 70)
plt.xticks(rotation = 'horizontal')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.savefig('recreatedgraph.png')