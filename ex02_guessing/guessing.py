import os
from random import randint

print("Pick the start number of the range :")
start_range = int(input())
print("Pick the end number of the range :")
end_range = int(input())

n = randint(start_range, end_range)
print("Guess the number :")
user_choice = int(input())
while user_choice != n :
    print("The good number is", "smaller." if user_choice > n else "bigger.")
    print("Try again :")
    user_choice = int(input())

print("Well played, the good number was : ",n)
print("Press 'Y' then 'Enter' to play again or press enter to leave.")
choice = input()
if choice == "Y" or choice == "y" :
    os.system("python guessing.py") 
exit()