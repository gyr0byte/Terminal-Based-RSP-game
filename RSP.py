import random
def get_choices():
    player_choice = input("Enter a choice(rock, paper, scissors: ").lower()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    
    return choices

def check_win(player, computer):
    print(f"You choose {player}, Computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes Scissors! You Win!"
        else:
            return "Paper covers rock :( You Lost!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You Win!"
        else:
            return "Scissors cuts Paper :( You Lost!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts Paper! You Win!"
        else:
            return "Rock smashes Scissors :( You Lost!"
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)