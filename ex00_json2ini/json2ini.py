import configparser
import json
import os

config = configparser.ConfigParser()

f = open("file.json")
data = json.load(f)

for i in data :
    config[i] = {}
    iData = data[i]
    for j in iData :
        config[i][j] = iData[j]

with open('file.ini', 'w') as configfile:
    config.write(configfile)
print("file.ini has been create.")

f.close()

print("Do you want to launch again the script ? (Y/N)")
choice = input()
if choice == "Y" or choice == "y" :
    print("")
    os.system("python json2ini.py") 
exit()