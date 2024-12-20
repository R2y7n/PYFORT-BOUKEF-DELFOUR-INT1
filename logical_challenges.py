#nim game
def display_sticks(n):
    for i in range(n):
        print("|", end=" ")

def player_removal(n):
    remove=int(input("How many sticks do you want to remove? : "))
    while remove<1 or remove>3:
        print("You cannot remove that many sticks!")
        remove=int(input("How many sticks do you want to remove? : "))
    return remove

def master_removal(n):
    if
    return remove

def nim_game():
    n=20
    turn=True
    i=0
    while n>0:
        print("There is",n,"sticks left")
        display_sticks(n)
        if i%2==0:
            remove=player_removal(n)
            n=n-remove
            turn=True
        elif i%2==1:
            remove=master_removal(n)
            n=n-remove
            turn=False
        i+=1
    if turn:
        print('You lost')
        return False
    else:
        print('You won')
        return True
nim_game()

#tic-tac-toe
def display_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=" ")
        print("-"*len(grid[i]))

def check_victory(grid, symbol):
    for i in range(len(grid)):
        cpt=0
        for j in range(len(grid[i])):
            if grid[i][j]==symbol:
                cpt+=1
        if cpt==3:
            return True
            break



