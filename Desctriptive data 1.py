import statistics as stats
import numpy as np
import pandas as pd

df = pd.read_csv("dataset1_cleaned.csv")
df2 = pd.read_csv("dataset2_cleaned.csv")

#creating the variables from the columns
bat_time = df['bat_landing_to_food']
sec_after = df['seconds_after_rat_arrival']
risk = df['risk']
reward = df['reward']
rat_num = df2['rat_arrival_number']
bat_num = df2['bat_landing_number']
rat_time = df2['rat_minutes']
food = df2['food_availability']
habit = df['habit']


#modes
habit_mode = stats.mode(habit)
print("Mode for the habit:", habit_mode)

mode_bat = stats.mode(bat_num)
print("Mode for number of rats: %d" % mode_bat)

mode_rat = stats.mode(rat_num)
print("Mode for number of rats: %d" % mode_rat)

mode_risk = stats.mode(risk)
print("Mode for risks: %d" % mode_risk)

mode_reward = stats.mode(reward)
print("Mode for rewards: %d" % mode_reward, "\n")

#frequencies

habit_freq = habit.value_counts()
print("The habit frequency", habit_freq)

bat_frequency = bat_num.value_counts()
print("total sum of values for", bat_frequency)

rat_frequency = rat_num.value_counts()
print("total sum of values for", rat_frequency)

risk_frequency = risk.value_counts()
print("total sum of values for", risk_frequency)

reward_frequency = reward.value_counts()
print("total sum of values for", reward_frequency,"\n")

#medians
med_rat = stats.median(rat_num)
print("the median number of rats is:", med_rat)

med_bat = stats.median(bat_num)
print("the median number of bats is:", med_bat, '\n')

#mean
mean_food = stats.mean(food)
mean_food = round(mean_food, 2)
print("average food remaining", mean_food,)

mean_rat = stats.mean(rat_time)
mean_rat = round(mean_rat, 2)
print("average time rats were present", mean_rat, 'minutes')

mean_bat = stats.mean(bat_time)
mean_bat = round(mean_bat, 2)
print("average time it took the bat to land at the food:", mean_bat, 'seconds')

mean_after = stats.mean(sec_after)
mean_after = round(mean_after, 2)
print("average time between the rat arriving after the bats", mean_after, 'seconds\n')

#range
the_range_rat = np.max(rat_time) - np.min(rat_time)
print("Range: %d" % the_range_rat, 'minutes')

the_range_after = np.max(sec_after) - np.min(sec_after)
print("Range: %d" % the_range_after, 'seconds')

the_range_bat = np.max(bat_time) - np.min(bat_time)
print("Range: %d" % the_range_bat, 'seconds\n')

#variance
var_rat = rat_time.var()
var_rat = round(var_rat, 2)
print("Population variance for rat times:", var_rat)

var_bat = bat_time.var()
var_bat = round(var_bat, 2)
print("Population variance for bat times:", var_bat)

var_after = sec_after.var()
var_after = round(var_after, 2)
print("Population variance for the rats arriving after the bats:", var_after, '\n')

#standard deviation
std_rat = rat_time.std()
std_rat = round(std_rat, 2)
print("Population deviation for rat times:", std_rat)

std_bat = bat_time.std()
std_bat = round(std_bat, 2)
print("Population deviation for bat times:", std_bat)

std_after = sec_after.std()
std_after = round(std_after, 2)
print("Population deviation for the rats arriving after the bats:", std_after)
