import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Data
categories = ['Latina/x/o', 'Black', 'White', 'Other']
values1 = [750, 270, 700, 400]
values2 = [1050, 470, 780, 530]

# Define the width of the bars
bar_width = 0.35

# Create an array of evenly spaced values for the bar positions
bar_positions = np.arange(len(categories))

# Combine values from both datasets
all_values = values1 + values2

# Determine the maximum value
plt.rc('axes', axisbelow=True)

# Define custom x-axis tick locations
custom_tick_locations = [0, 500, 1000, 1500, 2000]

# Define colors for each set of bars
color1 = 'steelblue'
color2 = "lightsteelblue"

# Add grid lines from the x-axis with a lower zorder
plt.grid(axis='x', zorder=0)

# Create horizontal bar graphs for each dataset
plt.barh(bar_positions, values1, bar_width, color=color1, label='Flood damage occurring even without climate change')
plt.barh(bar_positions, values2, bar_width, color=color2, label='Flood damage occurring because of climate change',
         left=values1)

# Add labels and title
plt.title('Fig. 3: Estimated per capita property damage from flooding by racial composition (38% scenario)',
          fontweight='bold')
plt.yticks(bar_positions, categories)
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=2)

# Format x-axis ticks as dollars with decimal points
plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.2f}'))

# Set custom x-axis tick locations
plt.xticks(custom_tick_locations)

# Format y-axis ticks as dollars with decimal points
plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.2f}'))

# Show the graph
plt.show()