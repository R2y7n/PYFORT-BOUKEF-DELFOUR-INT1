

###def turn(player, player_shots_grid, opponent_grid):

###def opponent_grid:

###def has won(player_shots_grid):

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
        pos = int(input("try to guess the position of the boat, the position should be in the form of (row,col) between 1 and 3 (eg . 1,2): "))
        row, col = map(int, pos.split(","))

        if 1 <= row <= 3 and 1 <= col <=3:
            return row - 1, col - 1
        else:
            print("invalid position")
    except ValueError:
        print("invalid position you should enter a position of the form (row,col) between 1 and 3 (eg . 1,2) )")


def initialize():
    grid = empty_grid()

    for i in range(2):
        print(f"place boat  {i+1}")
        while true:
            row, col = ask_position()
            if grid[row][col] == "":
                grid[row][col] = "B"
                break
            else:
                print("position already occupied, choose another")

    return grid



