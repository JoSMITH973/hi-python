import csv
import json
import os

f = open("file.json")
data = json.load(f)

headerArray = []
valueArray = []
for object in data :
    list = []
    for header in object :
        if header not in headerArray :
            headerArray.append(header)
        list.append(object[header])
    valueArray.append(list)

with open('file.csv', 'w', newline="", encoding='utf-8') as fileToWrite:
    writer = csv.writer(fileToWrite)
    writer.writerow(headerArray)
    for i in valueArray :
        writer.writerow(i)
    
f.close()

print("Do you want to launch again the script ? (Y/N)")
choice = input()
if choice == "Y" or choice == "y" :
    print("\n")
    os.system("python json2csv.py") 
exit()