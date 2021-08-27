import csv 
from collections import Counter

with open("SOCR-HeightWeight.csv") as f:
   reader =  csv.reader(f)
   filedata = list(reader)

filedata.pop(0)
newData = []
for i in range(len(filedata)):
    number = filedata[i][1]
    newData.append(number)

data = Counter(newData)
modeData = {
    "50-60":0,
    "60-70":0,
    "70-80":0,
}

for height,occurence in data.items():
    if 50 < float(height) < 60:
        modeData["50-60"] += occurence 

    elif 60 < float(height) < 70:
        modeData["60-70"] += occurence

    elif 70 < float(height) < 80:
        modeData["70-80"] += occurence

modeRange,modeOccurence = 0,0 
for range,occurence in modeData.items():
    if occurence > modeOccurence :
        modeRange,modeOccurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence

mode = float((modeRange[0]+modeRange[1])/2)

print(mode)