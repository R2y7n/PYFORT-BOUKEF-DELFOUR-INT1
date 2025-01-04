# Fort Boyard Project
# Authors : Anaïs Delfour, Rayane Boukef
# Role : presents the logical challenges that the player might face

import random

#nim game

# Role: displays the remaining sticks in the game.
# Parameters: the number of sticks left.
# Returns: none (displays a visual representation of the sticks on the output)
def display_sticks(n):
    for i in range(n):
        print("|", end=" ")

# Role: allows the player to remove a certain number of sticks
# Parameters: the number of sticks left
# Returns: the number of sticks the player decides to remove
def player_removal(n):
    remove=int(input("How many sticks do you want to remove? : "))
    # Validate the input to ensure it is between 1 and 3
    while remove<1 or remove>3 or remove>n:
        print("You cannot remove that many sticks!")
        remove=int(input("How many sticks do you want to remove? : "))
    return remove

# Role: determines the master's move
# Parameters: the number of sticks left
# Returns: the number of sticks the master decides to remove
def master_removal(n):
        # Optimal strategy for the master to win if possible
        remove = (n - 1) % 4
        if remove == 0:
            remove = random.randint(1,3)
        return remove

# Runs the Nim game.
# Parameters: None
# Returns: True if the player wins, False otherwise
def nim_game():
    # Display the rules
    print("You are going to face the master at the game of the nim")
    print("Each turn you can choose to remove 1, 2 or 3 sticks")
    print("Whoever removes the last stick loses the game")
    n=20 # Initialize the number of sticks
    turn=True #True = player's turn
    i=0 # Counter to alternate turns

    # Loop that alternate turns until there is no stick left
    while n>0:
        print("There is",n,"sticks left")
        display_sticks(n)
        print()
        if i%2==0:
            remove=player_removal(n)
            n=n-remove
            turn=True
        elif i%2==1:
            remove_master=master_removal(n)
            n=n-remove_master
            print("The master remove", remove_master, " sticks")
            turn=False
        i+=1
    if turn:
        print('You lost')
        return False
    else:
        print('You won')
        return True


#tic-tac-toe

# Role: displays the Tic-Tac-Toe grid
# Parameters: 2D list (the grid)
# Returns: none (displays the grid)
def display_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=" | ")
        print()
        print("-"*len(grid)*4)

# Role: checks if a player has won the game.
# Parameters:
#   - 2D list (grid)
#   - string (symbol of the player or the master's ("X" or "O"))
# Returns: True if the symbol has won, False otherwise.
def check_victory(grid, symbol):
    #Checks row victory
    for i in range(len(grid)):
        cpt=0
        for j in range(len(grid[i])):
            if grid[i][j]==symbol:
                cpt+=1
        if cpt==3:
            return True

    #Checks column victory
    for j in range(len(grid)):
        cpt=0
        for i in range(len(grid)):
            if grid[i][j]==symbol:
                cpt+=1
        if cpt==3:
            return True

    #Checks diagonal victory
    cpt=0
    for i in range(len(grid)):
        if grid[i][i]==symbol:
            cpt+=1
        if cpt==3:
            return True
    cpt=0
    for i in range(len(grid)):
        if grid[i][3-i-1]==symbol:
            cpt+=1
        if cpt==3:
            return True
    return False

# Role: determines the master's move
# Parameters:
#   2D list (the grid)
#   String (the master's symbol ("O").
# Returns: the row and column of the master's move (tuple)
def master_move(grid,symbol):
    #Check if the master can win in the next move
    for row in range(3):
        for col in range(3):
            if grid[row][col] == " ":
                grid[row][col] = symbol
                if check_victory(grid, symbol):
                    grid[row][col] = " "
                    return (row, col)
                grid[row][col] = " "

    # Otherwise try to block the player's winning move
    for row in range(3):
        for col in range(3):
            if grid[row][col] == " ":
                grid[row][col] = "X"
                if check_victory(grid, "X"):
                    grid[row][col] = " "
                    return (row, col)
                grid[row][col] = " "

    # Choose a random empty cell if no strategic move is found
    empty_cells = [(row, col) for row in range(3) for col in range(3) if grid[row][col] == " "]
    if empty_cells:
        return random.choice(empty_cells)

    return None

# Role: executes the master's turn
# Parameters: 2D list (grid)
# Returns: the grid updated with the master's move
def master_turn(grid):
    move=master_move(grid,"O")
    grid[move[0]][move[1]]="O"
    return grid

# Role: executes the player's turn
# Parameters: 2D list (grid)
# Returns: the grid updated with the player's move
def player_turn(grid):
    #List of empty cells in which the player can put a symbol
    empty_cells = [(row, col) for row in range(3) for col in range(3) if grid[row][col] == " "]

    # Ask the player where he wants to make a move then validates the coordinates
    row_coordinate=int(input("In which row do you want to place your symbol? : "))
    column_coordinate=int(input("In which column do you want to place your symbol? : "))
    coordinates=(row_coordinate-1,column_coordinate-1)
    while coordinates not in empty_cells:
        print("You cannot place your symbol in this cell! Choose another one!")
        row_coordinate = int(input("In which row do you want to place your symbol? : "))
        column_coordinate = int(input("In which column do you want to place your symbol? : "))
        coordinates = (row_coordinate-1, column_coordinate-1)

    # Place the symbol
    grid[row_coordinate-1][column_coordinate-1] = "X"
    return grid

# Role: checks if the grid is full
# Parameters: 2D list (grid)
# Returns: True if the grid is full, False otherwise
def full_grid(grid):
    # Create a list of all empty cells
    empty_cells = [(row, col) for row in range(3) for col in range(3) if grid[row][col] == " "]
    if empty_cells:
        return False
    return True

# Role: checks if the game is over.
# Parameters: 2D list (grid)
# Returns: True if there is a winner or the grid is full, False otherwise


def check_result(grid):
    if full_grid(grid) or check_victory(grid, "O") or check_victory(grid, "X"):
        return True
    return False

# Runs the Tic-Tac-Toe game
# Parameters: none
# Returns: True if the player wins, False otherwise


def tictactoe_game():
    # Display the rules
    print("You are going to face the master at tic-tac-toe")
    print("The first one to line up three of their symbols wins")
    grid=[[" "]*3 for i in range(3)] # Initialize the grid

    # Main loop that alternates turns between the player and the master until one of them won or until the grid is full
    while not check_result(grid):
        display_grid(grid)
        player_turn(grid)
        if check_result(grid):
            if check_victory(grid, "X"):
                print("Congratulations, you won!")
                return True
            print("It's a tie!")
            return False
        master_turn(grid)
        if check_result(grid):
            if check_victory(grid, "O"):
                print("The master won! You lost!")
            elif full_grid(grid):
                print("It's a tie!")
            return False