import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("dataset1_cleaned.csv")
risk = df['risk'].value_counts()

plt.pie(risk, labels=risk.index, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Ensures the pie chart is circular
plt.title('Distribution of risks taken by bats') # Optional: Add a title
plt.show()
