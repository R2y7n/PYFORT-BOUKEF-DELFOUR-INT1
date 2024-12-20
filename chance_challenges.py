import random
def shell_game():
    l=['A','B','C']
    n=2
    print("You are going to play the shell game. The aim is to find under which shell the key is hidden")
    print("Be careful, you only got 2 attempts")
    print("Each time choose between A, B or C")
    i=0
    found=False
    while i<2 and found==False:
        shell=random.choice(l)
        print("You still have", 2-i,'attempts')
        choice=input("Enter your choice: ")
        if 'a'<=choice<='z':
            choice=chr(ord(choice)+32)
        while choice not in l:
            print('Your attempt was unsucessful')
            choice=input("Please enter another choice: ")
            if 'a' <= choice <= 'z':
                choice = chr(ord(choice) + 32)
        if choice==shell:
            print("The key has been found!")
            found=True
        else:
            i+=1
            print("The key not been found")
    if found==False:
        print('You lost, the key was under shell',shell)
    return found

def roll_dice_game():
    win=False
    i = 0
    while win==False and i<3:
        print('You have',3-i,'attempts left')
        roll=input("Roll the dice by pressing the 'Enter' key")
        player_dice=(random.randint(1,6),random.randint(1,6))
        print('You obtained', player_dice)
        if player_dice[0]==6 or player_dice[1]==6:
            print('You win the game and the key')
            win=True
        else:
            master_dice=(random.randint(1,6),random.randint(1,6))
            print('The master has obtained', master_dice)
            if master_dice[0] == 6 or master_dice[1] == 6:
                print('You lost the game')
                break
            else:
                print('Nobody has won')
                i+=1
    if i==3:
        print('Nobody has won, it is a draw')
    return win





roll_dice_game()


shell_game()
