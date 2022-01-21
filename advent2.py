import numpy as np
import csv

depth = 0
horizontal = 0
aim = 0

array = []

with open("Sheet2.csv") as file_name:
    csvReader = csv.reader(file_name)
    for row in csvReader:
        array.append(row[0])

for i in range(0,len(array)):
    if(array[i][0:2]=="up"):
        aim-= int(array[i][len(array[i])-1:len(array[i])])
    if(array[i][0:4]=="down"):
        aim+= int(array[i][len(array[i])-1:len(array[i])])
    if(array[i][0:7]=="forward"):
        horizontal+= int(array[i][len(array[i])-1:len(array[i])])
        depth+= int(array[i][len(array[i])-1:len(array[i])])*aim
print(horizontal)
print(depth)
print(horizontal*depth)