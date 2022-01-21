import numpy as np
import csv

codes = []

with open("Sheet3.csv") as file_name:
    csvReader = csv.reader(file_name)
    for row in csvReader:
        codes.append(int(row[0]))

count_one = 0
count_zero = 0
most_common = np.ones(12)
for j in range(0,12):
    for i in range(0,len(codes)):
        if(codes[i]%10==0):
            count_zero+=1
        else:
            count_one+=1
        codes[i]=int(codes[i]/10)
    if(count_zero>count_one):
        most_common[j]=0
    else:
        most_common[j]=1
    count_one = 0
    count_zero = 0

gamma = most_common[11]
epsilon = 0

for i in range(1,len(most_common)):
    gamma = gamma*10
    gamma += most_common[11-i]
epsilon = 111111111111-gamma

epsilon_dec = 0
gamma_dec = 0

for i in range(0,12):
    epsilon_dec += (epsilon%10)*2**i
    gamma_dec += (gamma%10)*2**i
    epsilon = int(epsilon/10)
    gamma = int(gamma/10)
    print(epsilon_dec)

print(epsilon,gamma,epsilon*gamma)
print(epsilon_dec, gamma_dec, epsilon_dec*gamma_dec)