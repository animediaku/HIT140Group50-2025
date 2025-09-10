import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset2_cleaned.csv")

food = df['food_availability']
rat_num = df['rat_arrival_number']

plt.bar(rat_num, food)

plt.xlabel('Number of Rats')
plt.ylabel('food left')
plt.title('number of rats on the leftover food')

plt.show()
