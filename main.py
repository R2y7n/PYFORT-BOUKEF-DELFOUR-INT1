# Fort Boyard Project
# Authors : Anaïs Delfour, Rayane Boukef
# Role : this file centralizes all game actions using the functions of the other modules created

from math import *
import random
from utility_functions import *
from math_challenges import *
from logical_challenges import *
from pere_fouras_challenge import *
from final_challenge import *
from chance_challenges import *


# Role: This function is the main loop of the game
# Parameters: none (relies on user input and other functions from other files)
# Result: none (outputs the game result and records it in the history)
def game():
    """Main game loop."""
    # Ask the number of players and compose the team
    n = int(input("Enter the number of players (1 to 3): "))
    while n < 1 or n > 3:
        n = int(input("Invalid number. Please enter a number of players between 1 and 3: "))
    team = compose_equip(n)

    challenges = []  # List to keep track of all the challenges

    attempts = 0
    keys_cpt = 0
    # Main game loop
    # Players must collect the 3 keys within 5 attempts
    while keys_cpt < 3 and attempts < 5:
        attempts += 1

        # The user selects the challenge and the player
        choice_of_challenge = challenges_menu()
        print(f"Selected challenge: {choice_of_challenge}")
        player_chosen = choose_player(team)
        print(f"The selected player is {player_chosen['name']}")

        # Execute the chosen challenge
        if choice_of_challenge == "Mathematics challenge":
            win = math_challenge()
        elif choice_of_challenge == "Chance challenge":
            win = chance_challenge()
        elif choice_of_challenge == "Logic challenge":
            game_selected = random.choice(["The game of Nim", "Tic-Tac-Toe", "Battleship"])
            print(f"You are going to play a duel against the master of time at {game_selected}")
            if game_selected == "The game of Nim":
                win = nim_game()
            elif game_selected == "Tic-Tac-Toe":
                win = tictactoe_game()
            elif game_selected == "Battleship":
                try:
                    win = battleship_game()
                except Exception as e:
                    print(f"An error occurred while running the Battleship game: {e}")
                    win = False
        elif choice_of_challenge == "Père Fouras' riddle":
            win = pere_fouras_riddles()
        elif choice_of_challenge == "Battle Ship Game":
            try:
                win = battleship_game()
            except Exception as e:
                print(f"An error occurred while running the Battleship game: {e}")
                win = False
        else:
            print("Invalid challenge choice.")
            win = False

        # Update the number of keys
        if win:
            player_chosen['keys_won'] += 1
            keys_cpt += 1
            print("You won this challenge!")
        else:
            print("You lost this challenge!")

        print(f"Keys collected: {keys_cpt}")
        if keys_cpt < 3 and attempts < 5:
            print(f"You still have to collect {3 - keys_cpt} keys and have only {5 - attempts} attempts left.")

        # Record the challenge result
        challenge = {
            'type': choice_of_challenge,
            'player': player_chosen['name'],
            'win': win
        }
        challenges.append(challenge)

    # Determine if the team can access the treasure room
    if keys_cpt < 3:
        print("Sorry, you lost and you will not have access to the treasure room.")
        win_the_game = False
    else:
        print("Congratulations! You won three keys!")
        print("You will now have to find the code word")

        # Attempt to find the code word and win the game
        found_code_word = treasure_room()
        if found_code_word:
            print("You win the treasure!")
            win_the_game = True
        else:
            print("You do not have access to the treasure room!")
            win_the_game = False

    # Record the game in the history file
    record_history(team, challenges, keys_cpt, win_the_game)

#p

# Main entry point of the program
if __name__ == "__main__":
    introduction()

    # Wait for the user to start the game
    begin = input("Enter 'start' to play: ").strip().lower()
    while begin != "start":
        begin = input("Enter 'start' to play: ").strip().lower()

    game()
