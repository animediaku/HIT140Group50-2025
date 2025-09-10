
import pandas as pd
import numpy as np
from scipy.stats import fisher_exact
data1 = pd.read_csv("dataset1_cleaned.csv")

risk = data1.risk.values
reward = data1.reward.values

a = 0
b = 0
c = 0
d = 0

for i, e in zip(risk, reward):
    if i == 1 and e == 1:
        a += 1
    elif i == 1 and e == 0:
        b += 1
    elif i == 0 and e == 1:
        c += 1
    else:
        d += 1

table = [[a, b], [c, d]]
ratio, p_value = fisher_exact(table)
if p_value < 0.05:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")
if ratio > 1:
    print("Chances of their being a reward are higher if there is a risk")
else:
    print("Chances of their being a reward are higher if there is no risk")