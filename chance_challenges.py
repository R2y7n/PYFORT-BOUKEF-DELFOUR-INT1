import random

##### Chance challenge function

def shell_game():
    l = ['A', 'B', 'C']
    n = 2
    print("You are going to play the shell game. The aim is to find under which shell the key is hidden")
    print("Be careful, you only got 2 attempts")
    print("Each time choose between A, B or C")
    i = 0
    found = False
    while i < 2 and found == False:
        shell = random.choice(l)
        print("You still have", 2 - i, 'attempts')
        choice = input("Enter your choice: ")
        if 'a' <= choice <= 'z':
            choice = chr(ord(choice) + 32)
        while choice not in l:
            print('Your attempt was unsucessful')
            choice = input("Please enter another choice: ")
            if 'a' <= choice <= 'z':
                choice = chr(ord(choice) + 32)
        if choice == shell:
            print("The key has been found!")
            found = True
        else:
            i += 1
            print("The key not been found")
    if found == False:
        print('You lost, the key was under shell', shell)
    return found

def roll_dice():
    outcome=random.choice([1,2,3,4,5,6])
    return outcome


def roll_dice_game():
    print("Welcome to the Dice Game! Roll a 6 to win the key.")
    print("You have 3 attempts.")

    for attempt in range(1, 4):
        print(f"Attempt {attempt}/3")
        input("Press Enter to roll the dice...")
        player_roll = roll_dice()
        print(f"You rolled: {player_roll}")

        if player_roll==6:
            print("Congratulations! You rolled a 6 and won the key!")
            return True

        master_roll = roll_dice()
        print(f"The game master rolled: {master_roll}")
        if master_roll==6:
            print("The game master rolled a 6. You lost!")
            return False

    print("Game over. No one rolled a 6. It's a draw!")
    return False


def chance_challenge():
    challenge = [shell_game, roll_dice_game]

    challenge = random.choice(challenge)

    result = challenge()

    if result:
        print("Congratulations! You won the challenge")
    else:
        print("You lost the challenge !")

    return result


##### The logical_challenge function
chance_challenge()
