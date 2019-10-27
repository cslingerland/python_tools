import pandas as pd

data = pd.read_csv('skaters_small.csv')
#data = data[data.situation == 'all']
data = data.query('team=="DET" and situation=="all"')
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