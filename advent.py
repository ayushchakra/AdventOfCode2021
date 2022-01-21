import numpy as np

with open("Sheet1.csv") as file_name:
    array = np.loadtxt(file_name, delimiter=",")
print(array)