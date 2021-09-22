import os
import re
from random import *
import random

random_words = ["efrei", "master", "laptop", "playstation", "developpeur", "fifa"]
word = random.choice(random_words)
word_lenght = len(word)
i = randint(0, word_lenght-1)
life = 4

to_guess = [" _ "]*word_lenght
to_guess[i] = word[i]
print(to_guess)

while life != 0 :
    user_choice = input("Guess one of the letter : ")
    if len(user_choice) != 1 :
        print("You have to enter one letter at the time")

    elif user_choice in word :
        print("You right, there is '"+user_choice+"' in the word")
        matches = re.finditer(user_choice, word)
        index_letter = [match.start() for match in matches]
        for j in index_letter :
            to_guess[j] = word[j]
        if " _ " not in to_guess :
            break

    elif user_choice not in word :
        life -= 1
        print("This letter is not in the word")
    print(to_guess)
    print("Remaining lives :",life,"\n")

result = "You loose !"
if " _ " not in to_guess and life > 0 :
    result = "You win !"

print(result)
choice = input("Do you want to replay ? (Y/N)")
if choice == "Y" or choice == "y" :
    print("")
    os.system("python hangman.py") 
exit()