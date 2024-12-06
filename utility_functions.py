def introduction():
    print("Welcome to Fort Boyard!")
    print("The player(s) must complete challenges to earn keys and unlock the treasure room.")
    print("The aim is to collect three keys to access")


def compose_equipe(n):
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
            'keys_wons': 0  # Initialize the 'keys_wons' field to 0
        }

        # Add the player to the team
        team.append(player)

    # Check if any player was designated as the leader, if not, make the first player the leader
    if not any(player['is_leader'] for player in team):
        print("No leader was designated. The first player will automatically become the leader.")
        team[0]['is_leader'] = True  # Automatically make the first player the leader

    # Return the team
    return team


n = int(input("How many players do you want : "))

while n <1 or n >3:
    n = int(input("How many players do you want : "))

print(compose_equipe(n))
