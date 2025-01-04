import random


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
