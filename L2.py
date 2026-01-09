import random
import sys
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()
#rock paper scissor
choice = int(input('Please enter a choice :\n1 for Rock.\n2 for paper\n3 for scissors.\n\n'))
random_choice = random.randint(1,3)
if choice < 1 or choice > 3 :
    sys.exit("You must enter 1,2 or 3.") 
print("Your choice ",str(RPS(choice)).replace('RPS.',''),".\nComputer choice",str(RPS(random_choice)).replace('RPS.',''),".\n")

if ((choice == 1 and random_choice == 3) or (choice == 2 and random_choice == 1) or (choice == 3 and random_choice == 2)):
    print(" 🏆 You Win!")
elif choice == random_choice:
    print(" 😲 Tie!")
else: 
    print(" 🤖 Computer Wins!")
