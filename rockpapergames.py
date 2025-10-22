import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices ={"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock" and computer == "scissors":
        return "Rock smashes scissors! You win!"
    elif player == "paper" and computer == "rock":
        return "Paper covers rock! You win!"
    elif player == "scissors" and computer == "paper":
        return "Scissors cut paper! You win!"
    else:
        return "You lose!"

choice = get_choices()
result = check_win(choice["player"], choice["computer"])
print(result)

# key topics to knwo in python
# variable
# data types
# conitional statement 
# functions
# loops - for and while loops
# maps, filter and reduce 






