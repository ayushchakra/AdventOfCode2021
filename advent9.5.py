import numpy as np
import csv

data = list(csv.reader(open("Sheet9.csv")))
#print(data[22])
nums = np.zeros(len(data))
for i in range(0, len(data)):
    nums[i] = data[i][0]
#print(nums[22])
for i in range(0, len(data)):
    data[i] = [int(a) for a in str(int(data[i][0]))]
#print(data[22])
risk = 0
temp = data[22]
#print(len(temp))
data[22] = np.zeros(100)
for i in range(0,len(temp)):
    data[22][i+1] = temp[i]
temp = data[59]
data[59] = np.zeros(100)
#print(data[59])
for i in range(0, len(temp)):
    data[59][i+1] = temp[i]
start = True

def count_basin(i, j):

for i in range(0, len(data)):
    for j in range(0, len(data[0])):
        print(i)
        print(j)
        print(count_basin(i,j,1))