import random

user_wins = 0
computer_wins = 0

choices = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter your choice [Rock/Paper/Scissors] or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in choices:
        print("Enter a valid choice.")
        continue
#'continue' cmd inside a while loop is used to send the compiler back to the starting of the while loop.
    
    random_choice = random.randint(0,2)
    computer_input = choices[random_choice]
    print(f"Computer chose {computer_input}.")

    if user_input == "rock" and computer_input == "paper":
        print("Computer wins!")
        computer_wins += 1
    elif user_input == "paper" and computer_input == "scissors":
        print("Computer wins!")
        computer_wins += 1
    elif user_input == "scissors" and computer_input == "rock":
        print("Computer wins!")
        computer_wins += 1
    elif user_input == computer_input:
        print("Tie!")
    else:
        print("You won!")
        user_wins += 1


if computer_wins > user_wins:
    print("Computer won the overall game.")
elif user_wins > computer_wins:
    print("User won the overall game.")
else:
    print("The game was a tie!")
print(f"The final score is :- USER: {user_wins} | COMPUTER: {computer_wins}")

