import csv
from os import read

with open("SOCR-HeightWeight.csv") as f:
    reader = csv.reader(f)
    fileData = list(reader)
    
fileData.pop(0)
newData = []
for i in range(len(fileData)) :
    number = fileData[i][1]
    newData.append(float(number))

n = len(newData)
total = 0
for x in newData:
    total += x

mean = total/n
print(mean)



