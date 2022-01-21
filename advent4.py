import csv
import numpy as np

data = list(csv.reader(open("Sheet4.5.csv")))
bingo = np.zeros([500, 5])
calls = [85,84,30,15,46,71,64,45,13,90,63,89,62,25,87,68,73,47,65,78,2,27,67,95,88,99,96,17,42,31,91,98,57,28,38,93,43,0,55,49,22,24,82,54,59,52,3,26,9,32,4,48,39,50,80,21,5,1,23,10,58,34,12,35,74,8,6,79,40,76,86,69,81,61,14,92,97,19,7,51,33,11,77,75,20,70,29,36,60,18,56,37,72,41,94,44,83,66,16,53]

for i in range(0,500):
    k=0
    for j in range(0,len(data[i])):
        if(data[i][j]!=''):
            bingo[i][k]=data[i][j]
            k+=1

def is_in_array(index_calls, number_board):
    for i in range(0, index_calls+1):
        if(calls[i]==number_board):
            return True
            break
    return False

end = False
current_board = []
last_call = 0
indexes = []


def addition(index):
    bool = False
    for i in range(0,len(indexes)):
        if(indexes[i]==index):
            bool = True
    if(bool==False):
        indexes.append(index)
while(len(indexes)<99):
    for i in range(5,len(calls)):
        for j in range(0,int(len(bingo)/5)):
            current_board = bingo[5*j:5*j+5]
            for k in range(0,5):
                if(is_in_array(i,current_board[k][0]) and is_in_array(i,current_board[k][1]) and is_in_array(i,current_board[k][2]) and is_in_array(i,current_board[k][3]) and is_in_array(i,current_board[k][4])):
                    addition(j)
                    last_call = i
                    break
                if(is_in_array(i,current_board[0][k]) and is_in_array(i,current_board[1][k]) and is_in_array(i,current_board[2][k]) and is_in_array(i,current_board[3][k]) and is_in_array(i,current_board[4][k])):
                    addition(j)
                    last_call = i
                    break
            if(len(indexes)==99):
                break
        if(len(indexes)==99):
            break
        
print(last_call)
score = 0
print(current_board)
current_board = bingo[5*93:5*93+5]
print(sum(indexes))
sum = 0
for i in range(0,100):
    sum+=i
print(sum)
for i in range(0,5):
    for j in range(0,5):
        if(is_in_array(last_call, current_board[i][j])==False):
            score+=current_board[i][j]
print(score)
print(score*calls[last_call])