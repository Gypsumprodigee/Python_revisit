import random
import sys
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def play_rps():
    while True:
        # 1. Get User Input with validation loop
        line_break = "-" * 20
        print(f"\n{line_break}")
        user_input = input('Enter a choice:\n1 for Rock\n2 for Paper\n3 for Scissors\n\nChoice: ')
        
        if user_input not in ['1', '2', '3']:
            print("❌ Invalid input. Please enter 1, 2, or 3.")
            continue
            
        choice = int(user_input)
        user_choice = RPS(choice)
        computer_choice = RPS(random.randint(1, 3))

        # 2. Display Choices using .name (Cleaner than .replace)
        print(f"\nYour choice: {user_choice.name}")
        print(f"Computer choice: {computer_choice.name}\n")

        # 3. Determine Winner
        if user_choice == computer_choice:
            print("😲 It's a Tie!")
        elif (user_choice == RPS.ROCK and computer_choice == RPS.SCISSORS) or \
             (user_choice == RPS.PAPER and computer_choice == RPS.ROCK) or \
             (user_choice == RPS.SCISSORS and computer_choice == RPS.PAPER):
            print("🏆 You Win!")
        else:
            print("🤖 Computer Wins!")

        # 4. Play Again Logic
        while True:
            playagain = input("\nPlay again? (Y/Q): ").lower()
            if playagain == "y":
                break # Breaks the inner loop to restart the game
            elif playagain == "q":
                print("\nThanks for playing! Bye! 👋")
                sys.exit()
            else:
                print("Please enter Y or Q.")

if __name__ == "__main__":
    play_rps()