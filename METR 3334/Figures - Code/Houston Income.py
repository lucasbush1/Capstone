import matplotlib.pyplot as plt

us = 61000
foreign = 45000
phil = 95000
ind = 93000
china = 63000
col = 56000
pak = 52000
es = 37000
mex = 36000
guat = 33000
hond = 28000

countries = ["US Born", "Total Foreign Born", "Philippines", "India", "China", "Colombia", "Pakistan", "El Salvador", "Mexico", "Guatemala", "Honduras"]
income = [us, foreign, phil, ind, china, col, pak, es, mex, guat, hond]
plt.figure(figsize=(15, 6))
bars = plt.bar(countries, income, width = 0.25, color = "#3bb0ba")
plt.xticks(rotation=45, ha='right')
for bar, amount in zip(bars, income):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 500, '${:,.0f}'.format(amount), ha='center', va='bottom')
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))
bars[0].set_color("#08728c")
bars[1].set_color("#afdde9")
