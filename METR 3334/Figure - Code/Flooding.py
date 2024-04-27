# Cause of Death
drowning = 57
physicalTramuma = 3
lackMedTreatment = 4
electrocution = 4
other = 1 + 1

# Drowning - Subcategories
vehicle = 21
sweptAwayExit = 8
boat = 9
pedestrian = 9
building = 11
outiside = 23

# vehicle, swept away, and pedestrian equal 21/57. However, not given seperatley

import matplotlib.pyplot as plt

# Overall death causes data
labels_main = ['Drowning', 'Physical Trauma', 'Lack of Medical Treatment', 'Electrocution', 'Other']
sizes_main = [57, 3, 4, 4, 2]

# Drowning subcategories data
labels_drowning = ['Vehicle', 'Swept Away/Exit', 'Boat', 'Pedestrian', 'Building', 'Outside']
sizes_drowning = [21, 8, 9, 9, 11, 23]

# Calculate percentages for the main causes pie chart
sizes_main_percent = [size / sum(sizes_main) * 100 for size in sizes_main]

# Calculate weighted percentages for the drowning subcategories pie chart
total_drownings = sum(sizes_drowning)
sizes_drowning_weighted = [(size / total_drownings) * (sizes_main[0] / sum(sizes_main)) * 100 for size in sizes_drowning]

# Create the pie charts
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Main causes pie chart
axs[0].pie(sizes_main_percent, labels=labels_main, autopct='%1.1f%%', startangle=140)
axs[0].set_title('Main Causes of Death')

# Drowning subcategories pie chart
axs[1].pie(sizes_drowning_weighted, labels=labels_drowning, autopct='%1.1f%%', startangle=140)
axs[1].set_title('Drowning Subcategories as % of Total Deaths')

plt.tight_layout()
plt.show()
