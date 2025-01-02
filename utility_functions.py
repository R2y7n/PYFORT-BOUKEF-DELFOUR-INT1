# Fort Boyard Project
# Authors : Anaïs Delfour and Rayane Boukef
# Role : this file lists all essential functions to organize and track the game's progress


# Role: display the game's purpose and objective
# Parameters: none
# Returns: none, this function is for display purposes only
def introduction():
    print("Welcome to Fort Boyard!")
    print("The player(s) must complete challenges to earn keys and unlock the treasure room.")
    print("The aim is to collect three keys to access")

# Role: creates a team of players based on user input
# Parameters: n is the number of players to add in the team
# Returns: list of dictionaries
def compose_equip(n):
    # Initialization of an empty list to store team members
    team = []

    # Gather informations on each player
    for i in range(n):
        print(f"Player {i + 1}:")
        name = input("Enter the player's name: ")
        profession = input("Enter the player's profession: ")

        # Ask if the player is the leader
        is_leader = input("Is this player the team leader? (yes/no): ").strip().lower()
        is_leader = True if is_leader == 'yes' else False

        # Create a dictionary with the player's informations
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
    #List of the different challenges and then displays it
    l = ["Mathematics challenge", "Chance challenge", "Logic challenge", "Père Fouras'riddle"]
    for i in range(4):
        print(i + 1, l[i])

    #Ask the user to choose a challenge and validates the input
    choice = int(input("Choose your challenge by entering the number corresponding to your choice:"))
    while choice > 4 or choice < 1:
        choice = int(input(("Invalid input, enter another number:")))

    #Return the chosen challenge
    return l[choice - 1]

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

    #Return the selected player and its informations
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
