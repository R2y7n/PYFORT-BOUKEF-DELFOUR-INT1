# Fort Boyard Project
# Authors : Anaïs Delfour and Rayane Boukef
# Role : this file lists all essential functions to organize and track the game's progress

import random

# Role: display the game's purpose and objective
# Parameters: none
# Returns: none, this function is for display purposes only
def introduction():
    print("Welcome to Fort Boyard!")
    print("The player(s) must complete challenges to earn keys and unlock the treasure room.")
    print("The aim is to collect three keys to access to the treasure room.")

# Role: creates a team of players based on user input
# Parameters: n is the number of players to add in the team
# Returns: list of dictionaries


def compose_equip(n):
    # Initialization of an empty list to store team members
    team = []

    # Gather information on each player
    for i in range(n):
        print(f"Player {i + 1}:")
        name = input("Enter the player's name: ")
        profession = input("Enter the player's profession: ")

        # Ask if the player is the leader
        is_leader = input("Is this player the team leader? (yes/no): ").strip().lower()
        is_leader = True if is_leader == 'yes' else False

        # Create a dictionary with the player's information
        player = {
            'name': name,
            'profession': profession,
            'is_leader': is_leader,
            'keys_won': 0  # Initialize the keys_won to 0
        }

        # Add the player to the team
        team.append(player)

    # Check if any player was designated as the leader, if not, make the first player the leader
    if not any(player['is_leader'] for player in team):
        print("No leader was designated. The first player will automatically become the leader.")
        team[0]['is_leader'] = True  # Automatically make the first player the leader

    # Return the team
    return team

# Role: allow the user to choose one type of challenges
# Parameters: none
# Returns: the type of the chosen challenge as a string.


def challenges_menu():
    """Displays the available challenges and lets the user select one."""
    # List of the different challenges
    challenges = ["Mathematics challenge", "Chance challenge", "Logic challenge", "Père Fouras'riddle"]

    # Display challenges with their corresponding numbers
    print("Available challenges:")
    for i, challenge in enumerate(challenges, start=1):
        print(f"{i}. {challenge}")

    # Ask the user to choose a challenge
    while True:
        try:
            choice = int(input("Choose your challenge by entering the number corresponding to your choice (1-5): "))
            if 1 <= choice <= len(challenges):
                break  # Valid input, exit the loop
            else:
                print(f"Invalid input. Please enter a number between 1 and {len(challenges)}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Return the chosen challenge
    return challenges[choice - 1]


# Role: allows the user to select a player to play the challenge
# Parameters: a list of dictionaries
# Returns: A dictionary representing the selected player's information.


def choose_player(team):
    #Display the team member, their profession and role
    for i in range(len(team)):
        print(i + 1, team[i]["name"], "(", team[i]["profession"], ")", "-", end=" ")
        if team[i]["is_leader"]:
            print("Leader")
        else:
            print("Member")

    #Ask the user to choose a player and validates the input
    which_player = int(input("Enter the player's number:"))
    while which_player < 1 or which_player > len(team):
        which_player = int(input("Enter the player's number:"))

    #Return the selected player and its information
    return team[which_player - 1]


#Role: saves the history of the game in a file
# Parameters:
#   - team: a list of dictionaries with the players' informations
#   - challenges: a list of dictionaries with the challenges' informations
#   - nb_of_key: the number of keys collected during the game
#   - game_win: a boolean indicating whether the game was won or lost
# Returns: none, it directly writes the game history into the file "output/history.txt".


def record_history(team, challenges,nb_of_key, game_win):
    #Open the file in append mode
    with open("output/history.txt", 'a') as f1:

        #Record team details
        f1.write("=== Team ===\n")
        for i in range(len(team)):
            f1.write(f"Player {i + 1}: {team[i]['name']} ({team[i]['profession']})\n")
            f1.write(f"  - Leader: {'Yes' if team[i]['is_leader'] else 'No'}\n")
            f1.write(f"  - Keys won: {team[i]['keys_won']}\n")

        #Record challenges details
        f1.write("\n=== Challenges ===\n")
        for i in range(len(challenges)):
            f1.write(f"Challenge {i + 1}:\n")
            f1.write(f"  - Type: {challenges[i]['type']}\n")
            f1.write(f"  - Player: {challenges[i]['player']}\n")
            f1.write(f"  - Win: {'Yes' if challenges[i]['win'] else 'No'}\n")
            f1.write("\n")

        #Record the final results
        f1.write("\n=== Final Result ===\n")
        f1.write(f"Number of keys collected: {nb_of_key}\n")
        f1.write(f"Game won: {'Yes' if game_win else 'No'}\n")
        f1.write("-------------------------\n")



def next_player(player):
    """Switch to next player."""
    return 1 - player


def empty_grid():
    """Create  empty 3x3 grid."""
    return [[" " for _ in range(3)] for _ in range(3)]


def display_grid(grid, msg):
    """Display the grid with message."""
    print(msg)
    for row in grid:
        print("| " + " | ".join(row) + " |")
    print("-" * 13)


def ask_position():
    """Prompt the user to enter valid position and return as a tuple."""
    while True:
        try:
            pos = input("Enter the position (row,column) between 1 and 3 (e.g., 1,2): ")
            row, col = map(int, pos.split(","))
            if 1 <= row <= 3 and 1 <= col <= 3:
                return row - 1, col - 1  # Convert 0-based index
            else:
                print("Invalid position. Please enter values between 1 and 3.")
        except ValueError:
            print("Invalid format. Please enter a position in the form row,column (e.g., 1,2).")


def initialize():
    """Allow the player to place two boats on 3x3 grid."""
    grid = empty_grid()
    for i in range(2):
        print(f"Place boat {i + 1}:")
        while True:
            row, col = ask_position()
            if grid[row][col] == " ":
                grid[row][col] = "B"
                break
            else:
                print("Position already occupied. Choose another.")
    return grid


def turn(player, player_shots_grid, opponent_grid):
    """Handle a single turn for player or game master."""
    if player == 0:
        # Player turn
        display_grid(player_shots_grid, "History of your shots:")
        row, col = ask_position()
        if opponent_grid[row][col] == "B":
            print("Hit, sunk!")
            player_shots_grid[row][col] = "x"
            opponent_grid[row][col] = "x"
        else:
            print("Splash!")
            player_shots_grid[row][col] = "."
    else:
        # Game master's turn
        print("It's the game master's turn!")
        while True:
            row, col = random.randint(0, 2), random.randint(0, 2)
            if player_shots_grid[row][col] == " ":
                break
        print(f"The game master shoots at position {row + 1},{col + 1}")
        if opponent_grid[row][col] == "B":
            print("Hit, sunk!")
            player_shots_grid[row][col] = "x"
            opponent_grid[row][col] = "x"
        else:
            print("Splash!")
            player_shots_grid[row][col] = "."


def has_won(opponent_grid):
    """Check if all boats on the opponent's grid have been sunk."""
    for row in opponent_grid:
        if "B" in row:  # If any boat left, the player hasn't won
            return False
    return True


def battleship_game():
    """Orchestrate the Battleship game."""
    # Display game rules
    print("Welcome to Battleship!")
    print("Each player must place 2 boats on a 3x3 grid.")
    print("Boats are represented by 'B', missed shots by '.', and sunk boats by 'x'.\n")

    # Initialize the player boat grid
    print("Player, place your boats:")
    player_grid = initialize()
    display_grid(player_grid, "Here is your game grid with your boats:")

    # Create and initialize boat grid for the game master
    print("\nThe game master is placing their boats...")
    game_master_grid = empty_grid()
    placed_boats = 0
    while placed_boats < 2:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if game_master_grid[row][col] == " ":
            game_master_grid[row][col] = "B"
            placed_boats += 1

    # Initialize empty shooting grids
    player_shots_grid = empty_grid()
    game_master_shots_grid = empty_grid()

    current_player = 0  # Start with the player (0 = player, 1 = game master)
    while True:
        if current_player == 0:
            # Player's turn
            display_grid(player_shots_grid, "History of your shots:")
            turn(0, player_shots_grid, game_master_grid)
            if has_won(game_master_grid):  # Check if player has won
                print("Congratulations! You sank all the game master's boats. You win!")
                return True
        else:
            # Game master's turn
            print("It's the game master's turn!")
            turn(1, game_master_shots_grid, player_grid)
            if has_won(player_grid):  # Check if game master has won
                print("The game master has sunk all your boats. You lose!")
                return False

        # Switch next player
        current_player = next_player(current_player)
