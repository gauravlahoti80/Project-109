#importing the modules
import pandas as pd
import statistics

#reading the csv
df = pd.read_csv("Data.csv")

#making an array
df_math = []
#defining the array and converting it into list
df_math = df["math"].tolist()

#getting the mean
df_mean = statistics.mean(df_math)
#printing the mean
print(f"Mean of this data is: {df_mean}")

#getting the median
df_median = statistics.median(df_math)
#printing the median
print(f"Median of this data is: {df_median}")

#getting the mode
df_mode = statistics.mode(df_math)
#printing the mode
print(f"Mode of this data is: {df_mode}")

#getting the stdev
std = statistics.stdev(df_math)
#printing the stdev
print(f"Standard Deviation of this data is: {std}")