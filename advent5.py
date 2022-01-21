import csv
import numpy as np

data = list(csv.reader(open("Sheet5.csv")))


board_spaces = np.zeros([1000,1000])

for i in range(0,len(data)):
    for j in range(0,len(data[0])):
        data[i][j] = int(data[i][j])

for i in range(0, len(data)):
    if(data[i][0]==data[i][2]):
        if(data[i][1]>data[i][3]):
            for j in range(data[i][3], data[i][1]+1):
                board_spaces[data[i][0]][j] +=1
        else:
            for j in range(data[i][1], data[i][3]+1):
                board_spaces[data[i][0]][j] +=1
    elif(data[i][1]==data[i][3]):
        if(data[i][0]>data[i][2]):
            for j in range(data[i][2], data[i][0]+1):
                board_spaces[j][data[i][1]] +=1
        else:
            for j in range(data[i][0], data[i][2]+1):
               board_spaces[j][data[i][1]] +=1
    else:
        if(data[i][2]>data[i][0] and data[i][3]>data[i][1]):
            for j in range(0, data[i][3]-data[i][1]+1):
                board_spaces[data[i][0]+j][data[i][1]+j] += 1
        if(data[i][0]>data[i][2] and data[i][3]>data[i][1]):
            for j in range(0, data[i][3]-data[i][1]+1):
                board_spaces[data[i][0]-j][data[i][1]+j] += 1
        if(data[i][2]>data[i][0] and data[i][1]>data[i][3]):
            for j in range(0, data[i][1]-data[i][3]+1):
                board_spaces[data[i][0]+j][data[i][1]-j] += 1
        if(data[i][0]>data[i][2] and data[i][1]>data[i][3]):
            for j in range(0, data[i][1]-data[i][3]+1):
                board_spaces[data[i][0]-j][data[i][1]-j] += 1

counter = 0
for i in range(0, len(board_spaces)):
    for j in range(0, len(board_spaces[0])):
        if(board_spaces[i][j]>1):
            counter+=1
print(counter)