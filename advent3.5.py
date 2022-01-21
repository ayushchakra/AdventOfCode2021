import numpy as np
import csv

codes = []
code = []

with open("Sheet3.csv") as file_name:
    csvReader = csv.reader(file_name)
    for row in csvReader:
        codes.append(int(row[0]))
        code.append(int(row[0]))
count_zeros = 0
count_ones = 1
counter = 11
temp = []
while(len(codes)>1):
    for i in range(0,len(codes)):
        if(int(codes[i]/(10**counter)%10)==0):
            count_zeros+=1
        else:
            count_ones+=1
    if(count_ones>=count_zeros):
        for i in range(0,len(codes)):
            if(int(codes[i]/(10**counter)%10)==1):
                temp.append(codes[i])
    else:
        for i in range(0,len(codes)):
            if(int(codes[i]/(10**counter)%10)==0):
                temp.append(codes[i])
    count_zeros = 0
    count_ones = 0
    counter-=1
    codes = temp
    temp = []
ox = codes[0]
codes = code
counter = 11
while(len(codes)>1):
    for i in range(0,len(codes)):
        if(int(codes[i]/(10**counter)%10)==0):
            count_zeros+=1
        else:
            count_ones+=1
    if(count_ones<count_zeros):
        for i in range(0,len(codes)):
            if(int(codes[i]/(10**counter)%10)==1):
                temp.append(codes[i])
    else:
        for i in range(0,len(codes)):
            if(int(codes[i]/(10**counter)%10)==0):
                temp.append(codes[i])
    count_zeros = 0
    count_ones = 0
    counter-=1
    codes = temp
    print(codes)
    temp = []
co2 = codes[0]
ox_dec = 0
co2_dec = 0
for i in range(0,12):
    ox_dec += ox%10 * 2**i
    co2_dec += co2%10 * 2**i
    ox = int(ox/10)
    co2 = int(co2/10)
print(ox_dec, co2_dec, ox_dec*co2_dec)