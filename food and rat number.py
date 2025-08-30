import pandas as pd
import matplotlib.pyplot as plt


# read csv into a DataFrame
df = pd.read_csv("dataset2_cleaned.csv")

food = df['food_availability']
rat_num = df['rat_arrival_number']

plt.bar(rat_num, food)

# Add labels and title
plt.xlabel('Number of Rats')
plt.ylabel('food left')
plt.title('number of rats on the leftover food')

# Display the plot
plt.show()