
###def battleship_game():

def next_player(player):
    return 1 - player


def empty_grid():
    return [["" for i in range(3)] for j in range(3)]


def display_grid(grid, msg):
    print(msg)

    for row in grid:
        print("| + | ".joinstr(row) + " |")
    print("-" * 13)


def ask_position():
    try:
        pos = int(input
            ("try to guess the position of the boat, the position should be in the form of (row,col) between 1 and 3 (eg . 1,2): "))
        row, col = map(int, pos.split(","))

        if 1 <= row <= 3 and 1 <= col <= 3:
            return row - 1, col - 1
        else:
            print("invalid position")
    except ValueError:
        print("invalid position you should enter a position of the form (row,col) between 1 and 3 (eg . 1,2) )")


def initialize():
    grid = empty_grid()

    for i in range(2):
        print(f"place boat  { i +1}")
        while true:
            row, col = ask_position()
            if grid[row][col] == "":
                grid[row][col] = "B"
                break
            else:
                print("position already occupied, choose another")

    return grid


def turn(player, player_shots_grid, opponent_grid):
    if player == 0:
        display_grid(player_shots_gridn, " History of your shots : ")

        row, col = ask_position()

        if opponent_grid[row][col] == "B":
            print("Hint sunk ! ")

            player_shots_grid[row][col] = "x"
            opponent_grid[row][col] = "x"

        else:
            print("Splash ! ")
            player_shots_grid[row][col] = "..."

    else:
        print("Its the game master turn ! ")

        row, col = random.randin(0, 2), random.randin(0, 2)

        while True:
            if player_shots_grid[row][col] == "":
                break

        if opponent_grid[row][col] == "B":
            print("Hint sunk ! ")

            player_shots_grid[row][col] = "x"
            opponent_grid[row][col] = "x"

        else:
            print("Splash ! ")
            player_shots_grid[row][col] = "..."


def has_won(player_shots_grid):
    for row in player_shots_grid:
        for cell in row:
            if cell == 'B':
                return False
            else:
                return True


def battleship_game():
    # Display game rules
    print("Welcome to Battleship!")
    print("Each player must place 2 boats on a 3x3 grid.")
    print("Boats are represented by 'B' and missed shots by '.'. Sunk boats are marked by 'x'.\n")

    # Initialize the player's boat grid
    print("Player, place your boats:")
    player_grid = initialize()  # initialize()to set up player's boats
    display_grid(player_grid, "Here is your game grid with your boats:")

    #Create and initialize the game master's boat grid
    print("\nThe game master is placing their boats...")
    game_master_grid = empty_grid()
    placed_boats = 0
    while placed_boats < 2:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if game_master_grid[row][col] == " ":
            game_master_grid[row][col] = "B"
            placed_boats += 1

    #Initialize empty shooting grids
    player_shots_grid = empty_grid()  # Track player's shots
    game_master_shots_grid = empty_grid()  # Track game master's shots

    #Game loop
    current_player = 0  # Start with the player (0 = player, 1 = game master)
    while True:
        if current_player == 0:
            #Player's turn
            turn(0, player_shots_grid, game_master_grid)
            if has_won(player_shots_grid):  # Check if player has won
                print("Congratulations! You sank all the game master's boats. You win!")
                return True
        else:
            # Game master's turn
            turn(1, game_master_shots_grid, player_grid)
            if has_won(game_master_shots_grid):  # Check if game master has won
                print("The game master has sunk all your boats. You lose!")
                return False

        # Switch to the next player
        current_player = next_player(current_player)
