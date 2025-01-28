import json


path="/yourpath"

with open(path, 'r') as file:
    data = json.load(file)

dataList=[]

for i in data:

    ques="<s>[INST] "+i["instruction"]+" [/INST] "
    answer=i["output"]+"</s>"

    line=ques+answer
    dataList.append(line)


with open('csvfile.csv','w') as file2:
    for line in dataList:
        file2.write(line)
        file2.write('\n')