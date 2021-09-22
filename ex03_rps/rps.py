import os
from random import randint

n = randint(1,3)

print("Press '1' to pick Rock")
print("Press '2' to pick Paper")
print("Press '3' to pick Scissors")
user_choice = int(input("Choose your weapon : "))

while user_choice == ValueError or user_choice < 1 or user_choice > 3:
    print("You have to pick a number between 1 and 3")
    user_choice = int(input("Choose again : "))

switcher = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}
print("You :",switcher.get(user_choice,"Invalid weapon !"))
print("Vs")
print("IA :",switcher.get(n,"Invalid weapon !"))

condition_rock = user_choice == 1 and n == 3
condition_paper = user_choice == 2 and n == 1
condition_scissors = user_choice == 3 and n == 2

if user_choice == n :
    print("Draw !")
elif condition_rock or condition_paper or condition_scissors :
    print("You Win !")
else :
    print("You loose !")

choice = input("Do you want to replay ? (Y/N)")
if choice == "Y" or choice == "y" :
    print("")
    os.system("python rps.py") 
exit()