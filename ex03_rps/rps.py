import os
from random import randint

n = randint(1,3)
print("n is",n)

# 1 => Rock
# 2 => Paper
# 3 => Scissors
print("Press '1' to pick Rock")
print("Press '2' to pick Paper")
print("Press '3' to pick Scissors")
print("Choose you weapon :")
user_choice = input()

# condition_rock = user_choice == 1 and n == 3
# condition_paper = user_choice == 2 and n == 1
# condition_scissors = user_choice == 3 and n == 2

if n == user_choice :
    print("Draw ! Play again :")
    user_choice = input()
# elif condition_rock or condition_paper or condition_scissors :
#     print("You Win")
# else :
#     print("You loose !")
print("Press 'Y' then 'Enter' to play again or press enter to leave.")
choice = input()
if choice == "Y" or choice == "y" :
    os.system("python rps.py") 
exit()