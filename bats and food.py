import pandas as pd
import matplotlib.pyplot as plt


# read csv into a DataFrame
df = pd.read_csv("dataset2_cleaned.csv")

food = df['food_availability']
bat_num = df['bat_landing_number']

plt.bar(bat_num, food)

# Add labels and title
plt.xlabel('Number of Bats')
plt.ylabel('food left')
plt.title('number of bats on the leftover food')

# Display the plot
plt.show()