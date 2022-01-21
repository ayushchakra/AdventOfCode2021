import numpy as np
import csv

data = list(csv.reader(open("Sheet10.csv")))
expected = []
error = 0
counter = len(data)-1
completed = True
score = 0
count = 0
total_score = []
for i in range(0, len(data)):
    for j in range(0, len(data[i][0])):
        if(data[i][0][j]=='('):
            expected.append(')')
        elif(data[i][0][j]=='['):
            expected.append(']')
        elif(data[i][0][j]=='{'):
            expected.append('}')
        elif(data[i][0][j]=='<'):
            expected.append('>')
        elif(data[i][0][j]==expected[-1]):
                del expected[-1]
        else:
            if(data[i][0][j]==')'):
                completed = False
                break
            if(data[i][0][j]==']'):
                completed = False
                break
            if(data[i][0][j]=='}'):
                completed = False
                break
            if(data[i][0][j]=='>'):
                completed = False
                break
    score = 0
    print(expected)
    if(completed):
        while(len(expected)>0):
            score = score*5
            if(expected[-1]==')'):
                score+=1
            if(expected[-1]==']'):
                score+=2
            if(expected[-1]=='}'):
                score+=3
            if(expected[-1]=='>'):
                score+=4
            del expected[-1]
        total_score.append(score)
    expected = []
    completed = True
total_score = sorted(total_score)
print(total_score[int(len(total_score)/2)])