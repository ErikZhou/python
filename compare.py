
# Create two lists of float data
#list1 = [1.2, 3.4, 5.6, 7.8]
#list2 = [1.3, 3.4, 5.5, 7.9]
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Open the text file
with open('lat_390-a.txt', 'r') as f: # new
    # Read the contents of the file
    contents = f.read()

# Split the contents into individual lines
list1 = contents.splitlines()
print("list1 {0}", len(list1))

with open('lat_390-b.txt', 'r') as f: # old
    # Read the contents of the file
    contents = f.read()

# Split the contents into individual lines
list2 = contents.splitlines()
print("list2 {0}", len(list2))

# Initialize counters for same and different values
same_count = 0
diff_count = 0

# Iterate over each element of the first list and compare it to the corresponding element of the second list
differences = []
x1 = []
x2 = []

data1 = {'X': [], 'Y': []} # new
data2 = {'X': [], 'Y': []} # old


for i in range(len(list1)):
    data1['X'].append(i)
    data1['Y'].append(float(list1[i]))
    data2['X'].append(i)
    data2['Y'].append(float(list2[i]))
    if list1[i] != list2[i]:
        differences.append((i, list1[i], list2[i]))
        diff_count += 1
    else:
        same_count += 1

# Report the differences
if differences:
    print("The following differences were found:")
    for diff in differences:
        print(f"At index {diff[0]}, list1 has {diff[1]} while list2 has {diff[2]}")
else:
    print("The lists are the same")

# Calculate the percentage of same and different values
total_count = len(list1)
same_percentage = (same_count / total_count) * 100
diff_percentage = (diff_count / total_count) * 100

# Print the results
print(f"Same percentage: {same_percentage:.2f}%")
print(f"Different percentage: {diff_percentage:.2f}%")

# create some data


# create a scatter plot for the first dataset with blue color

#plt.scatter(list1, x1, color='blue', label='Dataset 1')
# create a scatter plot for the second dataset with red color

#plt.scatter(list2, x2, color='red', label='Dataset 2')

# add labels and title

# sort the DataFrame by the 'Y' column

df2 = pd.DataFrame(data2)
df_sorted2 = df2.sort_values('X')
# create a line plot of the sorted data
plt.plot(df_sorted2['X'], df_sorted2['Y'],'-o', color='blue', label='Old')

df1 = pd.DataFrame(data1)
df_sorted1 = df1.sort_values('X')
# create a line plot of the sorted data
plt.plot(df_sorted1['X'], df_sorted1['Y'],'-o', color='red', label='New')


# add labels and title

plt.xlabel('Index')
plt.ylabel('LAT')
plt.title('Comparisons')

# show the plot
plt.legend()
plt.show()
