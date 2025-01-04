# Fort Boyard Project
# Authors: Anaïs Delfour, Rayane Boukef
# Role : presents the chance challenges that the player might face

import random

##### Chance challenge function

# Role: Simulates a shell game where the player tries to find a hidden key under one of three shells
# Parameters: None
# Returns: True if the player finds the key within the given attempts, False otherwise
def shell_game():
    l = ['A', 'B', 'C'] # List of the possible shells
    n = 2 # number of attempts allowed
    #Game's rule
    print("You are going to play the shell game. The aim is to find under which shell the key is hidden")
    print("Be careful, you only got 2 attempts")
    print("Each time choose between A, B or C")

    i = 0
    found = False
    # Main loop of the game
    while i < 2 and found == False:
        shell = random.choice(l) #Randomly choose a shell
        print("You still have", 2 - i, 'attempts')

        # Allows the player to take a guess and ensure the input is valid
        choice = input("Enter your choice: ")
        if 'a' <= choice <= 'z':
            choice = chr(ord(choice) - 32)
        while choice not in l or choice<'a' and choice>'c':
            print('Your attempt was unsucessful')
            choice = input("Please enter another choice: ")
            if 'a' <= choice <= 'z':
                choice = chr(ord(choice) - 32)

        # Compare the shell and the choice
        if choice == shell:
            print("The key has been found!")
            found = True
        else:
            i += 1
            print("The key has not been found")
    if found == False:
        print('You lost, the key was under shell', shell)
    return found

# Role: simulates rolling a six-sided dice
# Parameters: none
# Returns: an integer between 1 and 6 representing the outcome of the dice roll
def roll_dice():
    outcome=random.choice([1,2,3,4,5,6])
    return outcome

# Role: simulates a dice game where the player attempts to roll a 6 to win
# Parameters: none
# Returns: True if the player rolls a 6 within 3 attempts False otherwise
def roll_dice_game():
    #Display the rules
    print("Welcome to the Dice Game! Roll a 6 to win the key.")
    print("You have 3 attempts.")
    print("If the master rolls a 6 before you or no attempt is left you lose.")

    # Main loop which alternates the player and the master's turn
    for attempt in range(1, 4):
        print(f"Attempt {attempt}/3")
        input("Press Enter to roll the dice...")
        player_roll = roll_dice()
        print(f"You rolled: {player_roll}")

        #Check if the player wins
        if player_roll==6:
            print("You rolled a 6 and won the key!")
            return True

        master_roll = roll_dice()
        print(f"The game master rolled: {master_roll}")

        #Check if the master wins
        if master_roll==6:
            print("The game master rolled a 6.")
            return False

    #Neither rolled a 6 after 3 attempts
    print("Game over. No one rolled a 6. It's a draw!")
    return False

# Role: randomly selects and executes one of the chance-based challenges (shell game or roll dice game)
# Parameters: none
# Returns: the result of the chosen challenge (True if the player wins, False otherwise)
def chance_challenge():
    challenge = [shell_game, roll_dice_game] # List of available challenges

    challenge = random.choice(challenge) #Randomly select a challenge

    result = challenge() # Execute the selected challenge

    # Announce the result of the challenge
    if result:
        print("Congratulations! You won the challenge")
    else:
        print("You lost the challenge !")

    return result