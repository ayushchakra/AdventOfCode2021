import numpy as np
import csv

data = list(csv.reader(open("Sheet8.csv")))
output = np.zeros(len(data))
counter = 0
one = 0
four = 0
seven = 0
eight = 0
counter = 3

def find_missing(data_string):
    list = [char for char in data_string]
    missing = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for i in range(0, len(list)):
        missing.remove(list[i])
    return missing
def char_in_missing(char, missing):
    for i in range(0, len(missing)):
        if(char==missing[i]):
            return True
            break
    return False
def what_number(one_i, four_i, seven_i, eight_i, data_string, i):
    one = [char for char in data[i][one_i]]
    four = [char for char in data[i][four_i]]
    seven = [char for char in data[i][seven_i]]
    eight = [char for char in data[i][eight_i]]
    missing = find_missing(data_string)
    if(len(data_string)==2):
        return 1
    if(len(data_string)==4):
        return 4
    if(len(data_string)==3):
        return 7
    if(len(data_string)==7):
        return 8
    if(len(data_string)==6):
        if(not char_in_missing(four[0], missing) and not char_in_missing(four[1], missing) and not char_in_missing(four[2], missing) and not char_in_missing(four[3], missing)):
            return 9
        if(not char_in_missing(one[0], missing) and not char_in_missing(one[1], missing)):
            return 0
        return 6
    if(len(data_string)==5):
        if(not char_in_missing(one[0], missing) and not char_in_missing(one[1], missing)):
            return 3
        count_missing_four = 0
        for i in range(0,4):
            if(char_in_missing(four[i], missing)):
                count_missing_four +=1
        if(count_missing_four==1):
            return 5
        return 2

for i in range(0, len(data)):
    for j in range(0, 10):
        if(len(data[i][j])==2):
            one = j
        if(len(data[i][j])==4):
            four = j
        if(len(data[i][j])==3):
            seven = j
        if(len(data[i][j])==7):
            eight = j
    for k in range(10, 14):
        output[i] += what_number(one, four, seven, eight, data[i][k], i)*10**counter
        counter -= 1
    counter = 3

print(sum(output))