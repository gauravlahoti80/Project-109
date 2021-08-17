#importing the modules
import pandas as pd
import statistics

#reading the csv
df = pd.read_csv("Data.csv")

#making an array
math_list = []
#defining the array and converting it into list
math_list = df["math"].tolist()

#creating another array to store final values
final_list1 = []
final_list2 = []
final_list3 = []

#finding mean
df_stdev = statistics.stdev(math_list)
#finding mean
df_mean = statistics.mean(math_list)


'''finding the data which lies in 1st standard deviation'''

#starting point of stdev
s_p_stdev1 = df_mean-df_stdev
#ending point of stdev
e_p_stdev2 = df_mean+df_stdev

#for loop
for i in math_list:
    #if condition to check weather the values lie between 1st stdev
    if i > s_p_stdev1 and i < e_p_stdev2:
        #appending the values in the final array
        final_list1.append(i)

#printing the percentage of the data that lies between 1st stdev
print(f"{(len(final_list1)/len(math_list))*100}% of the data lies between 1st standard deviation.")


'''finding the data which lies in 2nd standard deviation'''

#starting point of the stdev
s_p_stdev2 = df_mean-2*(df_stdev)
#ending point of stdev
e_p_stdev2 = df_mean+2*(df_stdev)

#for loop
for i in math_list:
    #if condition to check weather the values lie between 1st stdev
    if i > s_p_stdev2 and i < e_p_stdev2:
        #appending the values to the final list
        final_list2.append(i)

#printing the percentage of the data that lies between 1st stdev
print(f"{(len(final_list2)/ len(math_list))*100}% of the data lies between 2nd standard deviation.")


'''Finding the data which lies between 3rd standard deviation''' 

#starting point of the stdev
s_p_stdev3 = df_mean - 3*(df_stdev)
#ending point of the stdev
e_p_stdev3 = df_mean + 3*(df_stdev)

#for loop
for i in math_list:
    #if condition to check weather the values lie between 1st stdev
    if i > s_p_stdev3 and i < e_p_stdev3:
        #appending the values to the final list
        final_list3.append(i)

#printing the percentage of the data that lies between 1st stdev
print(f"{(len(final_list3)/ len(math_list))*100}% of the data lies between 3rd standard deviation.")
