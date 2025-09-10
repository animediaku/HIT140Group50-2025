import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset2_cleaned.csv")

bat_num = df['bat_landing_number']
rat_num = df['rat_arrival_number']

plt.scatter(rat_num, bat_num)

plt.xlabel('Number of Rats')
plt.ylabel('number of Bats')
plt.title('Number of bats compared to number of rats correlation')

plt.show()
