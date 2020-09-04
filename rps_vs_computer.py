from random import choice
from colorama import init
from termcolor import colored

init()


while True:
    player_score = 0
    computer_score = 0
    ties = 0
    print(colored(
        "\nWELCOME TO ROCK PAPER SCISSORS, CAN YOU BEAT THE COMPUTER?", on_color="on_cyan"))

    name = str(input("What's your name? \n"))
    while True:
        try:
            games = abs(int(
                input("How many games would you like to play? (enter any positive number)\n")))
            if games > 25:
                games = 25
                print(
                    colored("You have been assigned a maximum of 25 games", on_color="on_red"))
            else:
                print(
                    colored(f"You have chosen to play {games} games... good luck!", on_color="on_green"))
        except ValueError:
            print(colored("PLEASE ENTER A VALID NUMERIC INPUT", on_color='on_red'))
        else:
            break

    while (player_score + computer_score + ties) < games:

        user = input(
            f"{(player_score + computer_score + ties+1)}) Choose one of the following: rock, paper, scissors\n  (type 'quit' to quit the game at any time)\n").lower()

        computer = choice(("rock", "paper", "scissors"))

        if user == "quit":
            break
        elif user in ("rock", "paper", "scissors"):
            print(f"\nComputer Chose {computer}...\n")
            if user == computer:
                print(colored("It's a tie!", 'cyan'))
                player_score += 0
                computer_score += 0
                ties += 1
            elif user == "rock":
                if computer == "scissors":
                    print(colored(f"{name} Wins!", "green"))
                    player_score += 1
                else:
                    print(colored("Computer Wins!", 'red'))
                    computer_score += 1
            elif user == "scissors":
                if computer == "paper":
                    print(colored(f"{name} Wins!", "green"))
                    player_score += 1
                else:
                    print(colored("Computer Wins!", 'red'))
                    computer_score += 1
            elif user == "paper":
                if computer == "rock":
                    print(colored(f"{name} Wins!", "green"))
                    player_score += 1
                else:
                    print(colored("Computer Wins!", 'red'))
                    computer_score += 1
            print(colored(
                f"{name} Wins: {player_score}, Computer Wins: {computer_score}, Ties: {ties} \n", on_color='on_magenta'))
        else:
            print(colored("ENTER A VALID CHOICE", on_color='on_red'))

    if player_score > computer_score:
        if (player_score-computer_score) >= games // 2.5:
            print(colored(
                f"Wow {name}, you absolutely destroyed the computer!", on_color='on_green'))
        elif (player_score-computer_score) == 1:
            print(
                colored(f"Well done {name}, you won a very close game!", on_color='on_green'))
        else:
            print(colored(f"Nice work {name}, you won!", on_color='on_green'))
    elif player_score == computer_score:
        print(colored("It's a tie overall!", on_color='on_cyan'))
    else:
        if (computer_score-player_score) >= games // 2.5:
            print(colored
                  (f"Hard luck {name}, you got absolutely destroyed by the computer!", on_color='on_red'))
        elif (computer_score-player_score) == 1:
            print(
                colored(f"Unlucky {name}, you lost a very close game!", on_color='on_red'))
        else:
            print(
                colored(f"Better luck next time {name}, the computer won!", on_color='on_red'))
    play_again = input(
        "\nDo you want to play again? (type 'y' to replay, enter anything else to exit)\n").lower()
    if play_again == "y":
        pass
    else:
        print(colored("Thank you for playing :)", "green"))
        break
