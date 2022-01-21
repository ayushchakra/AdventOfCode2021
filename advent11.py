import csv
import numpy as np

data = list(csv.reader(open("Sheet11.csv")))
print(data[0][0])

for i in range(0,len(data)):
    data = [int(a) for a in str(int(data[i][0]))]
print(data)