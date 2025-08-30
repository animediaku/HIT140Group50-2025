import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("dataset1_cleaned.csv")
reward = df['reward'].value_counts()

plt.pie(reward, labels=reward.index, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Ensures the pie chart is circular
plt.title('Distribution of rewards from bats taking risks') # Optional: Add a title
plt.show()