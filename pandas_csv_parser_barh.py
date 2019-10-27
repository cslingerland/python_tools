import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('skaters_small.csv')
#data = data[data.situation == 'all']
data = data.query('team=="EDM" and situation=="all"')
data = data.sort_values(ascending=False, by='I_F_points')


total_assists = []
for line in data.iterrows():
    a = line[1]['I_F_primaryAssists']
    a += line[1]['I_F_secondaryAssists']
    total_assists.append(a)

data['I_F_assists'] = total_assists

out_data = data[['name','games_played','I_F_goals','I_F_assists','I_F_points']]
#data_top = out_data.head()
#print(data_top)
print(out_data)

# matplotlib
fig, ax = plt.subplots()

# Example data
people = out_data['name']
points = out_data['I_F_points']

for i, v in enumerate(points):
    ax.text(v + .5, i + .4, str(v), color='red', size='8')
ax.barh(people, points)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Points')
ax.set_title(data['team'].values[0] + '\n2018-2019 Point Totals')
fig.set_size_inches((20, 6))


plt.show()
