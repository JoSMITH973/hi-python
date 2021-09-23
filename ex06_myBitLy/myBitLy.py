import json
import random
import string

f = open("data.json")
data = json.load(f)
f.close()
long_url = input("Veuillez entrer votre url : ")
def url_random():
    return "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(4))
end_url_random = url_random()

urlExist = False
for object in data :
    # On vérifie que l'url n'existe pas
    # Si on trouve l'url dans la base de données, alors on n'insérera pas notre url
    if long_url == object["long_url"] :
        print("Impossible to insert this url ! It already exists !")
        print("long url :", object["long_url"])
        print("short url :", object["short_url"])
        urlExist = True
        break

# Fonction qui évite les redendances des url_short  
# Version debug (avec print() et test) à coller à la place du while
# nom du fichier contenant le debug -> while_debug.txt
while True and urlExist == False:
    short_exist = False
    for object in data :
        if end_url_random == object["short_url"][-4:] :
            end_url_random = url_random()
            short_exist = True
            break
    if short_exist == False :
        break
        
short_url = "www.shorterurl.com/"+end_url_random

if urlExist == False :
    urlToInsert = {"short_url":short_url,"long_url":long_url}
    data.append(urlToInsert)
    with open("data.json", "w") as newDataFile :
        json.dump(data, newDataFile)
    print("Base de données mise à jour !")
    print("long url :", long_url)
    print("short url :", short_url)

choice = input("Press enter to exit")
exit()