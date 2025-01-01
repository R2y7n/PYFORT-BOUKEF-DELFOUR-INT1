def introduction():
    print("Welcome to Fort Boyard!")
    print("The player(s) must complete challenges to earn keys and unlock the treasure room.")
    print("The aim is to collect three keys to access")


def compose_equip(n):
    # List to store team members
    team = []

    # Ask how many players the user wants to include
    # Collect player details
    for i in range(n):
        print(f"Player {i + 1}:")
        name = input("Enter the player's name: ")
        profession = input("Enter the player's profession: ")

        # Ask if the player is the leader
        is_leader = input("Is this player the team leader? (yes/no): ").strip().lower()
        is_leader = True if is_leader == 'yes' else False

        # Create a dictionary for the player
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


def challenges_menu():
    l = ["Mathematics challenge", "Chance challenge", "Logic challenge", "Père Fouras'riddle"]
    for i in range(4):
        print(i + 1, l[i])
    choice = int(input("Choose your challenge by entering the number corresponding to your choice:"))
    while choice > 4 or choice < 1:
        choice = int(input(("Invalid input, enter another number:")))
    return l[choice - 1]


def chose_player(team):
    for i in range(len(team)):
        print(i + 1, team[i]["name"], "(", team[i]["profession"], ")", "-", end=" ")
        if team[i]["is_leader"]:
            print("Leader")
        else:
            print("Member")
    which_player = int(input("Enter the player's number:"))
    while which_player < 1 or which_player > len(team):
        which_player = int(input("Enter the player's number:"))
    return team[which_player - 1]


def record_history(challenges, team, nb_of_keys):
    with open("output/history.txt", 'a') as f1:
        f1.write(challenges)
        f1.write(team)
        f1.write(nb_of_keys)



