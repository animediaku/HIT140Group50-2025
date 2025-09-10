import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset2_cleaned.csv")

food = df['food_availability']
bat_num = df['bat_landing_number']

plt.bar(bat_num, food)

plt.xlabel('Number of bats')
plt.ylabel('Food Left')
plt.title('number of bats on the leftover food')

plt.show()
