import random
#nim game
def display_sticks(n):
    for i in range(n):
        print("|", end=" ")

def player_removal(n):
    remove=int(input("How many sticks do you want to remove? : "))
    while remove<1 or remove>3 or remove>n:
        print("You cannot remove that many sticks!")
        remove=int(input("How many sticks do you want to remove? : "))
    return remove

def master_removal(n):
        remove = (n - 1) % 4
        if remove == 0:
            remove = random.randint(1,3)
        return remove


def nim_game():
    n=20
    turn=True
    i=0
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
def display_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=" | ")
        print()
        print("-"*len(grid)*4)

def check_victory(grid, symbol):
    for i in range(len(grid)):
        cpt=0
        for j in range(len(grid[i])):
            if grid[i][j]==symbol:
                cpt+=1
        if cpt==3:
            return True
    for j in range(len(grid)):
        cpt=0
        for i in range(len(grid)):
            if grid[i][j]==symbol:
                cpt+=1
        if cpt==3:
            return True
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

def master_move(grid,symbol):
    for row in range(3):
        for col in range(3):
            if grid[row][col] == " ":
                grid[row][col] = symbol
                if check_victory(grid, symbol):
                    grid[row][col] = " "
                    return (row, col)
                grid[row][col] = " "

    for row in range(3):
        for col in range(3):
            if grid[row][col] == " ":
                grid[row][col] = "X"
                if check_victory(grid, "X"):
                    grid[row][col] = " "
                    return (row, col)
                grid[row][col] = " "

    empty_cells = [(row, col) for row in range(3) for col in range(3) if grid[row][col] == " "]
    if empty_cells:
        return random.choice(empty_cells)

    return None

def master_turn(grid):
    move=master_move(grid,"O")
    grid[move[0]][move[1]]="O"
    return grid

def player_turn(grid):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if grid[row][col] == " "]
    row_coordinate=int(input("In which row do you want to place your symbol? : "))
    column_coordinate=int(input("In which column do you want to place your symbol? : "))
    coordinates=(row_coordinate-1,column_coordinate-1)
    while coordinates not in empty_cells:
        print("You cannot place your symbol in this cell! Choose another one!")
        row_coordinate = int(input("In which row do you want to place your symbol? : "))
        column_coordinate = int(input("In which column do you want to place your symbol? : "))
        coordinates = (row_coordinate-1, column_coordinate-1)
    grid[row_coordinate-1][column_coordinate-1] = "X"
    return grid

def full_grid(grid):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if grid[row][col] == " "]
    if empty_cells:
        return False
    return True

def check_result(grid):
    if full_grid(grid) or check_victory(grid, "O") or check_victory(grid, "X"):
        return True
    return False

def tictactoe_game():
    grid=[[" "]*3 for i in range(3)]
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

