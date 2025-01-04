# Fort Boyard Project
# Authors : Anaïs Delfour, Rayane Boukef
# Role : simulates the final step to access Fort Boyard's treasure room

import json
import random

# Role: converts a given string to lowercase manually, without using '.lower()' method
# Parameters: a string
# Returns: a new string where all uppercase letters in the input have been converted to lowercase
def lowercase(str):
    str_lower=''
    for char in str:
        #If the character is uppercase, converts it in lowercase
        if 'A' <= char <= 'Z':
            str_lower += chr(ord(char) + 32)
        #If the character is not uppercase, leaves it unchanged
        else:
            str_lower += char
    return str_lower

#Role: allows the player to guess the word of the treasure room
#Parameters:
#   - list: list of the clues to help the player guess the word
#   - word: correct code word the player needs to guess
# Returns: 'True' or 'False' whether the player guesses the word correctly or not
def find_the_word(list,word):
    print("You have to find the final word to open the treasure room")
    print("Here are the first three clues, you have three attempts to find the word:")

    #Display the three clues
    for i in range(3):
        print(list[i])

    attempts = 3 # Players start with 3 attempts
    i = 4 # Index to provide additional clues
    answer_correct = False # Help to know if the player guessed the word

    # This loop allows the player to take guesses until he has no attempt left
    while attempts > 0:
        answer = input("Please enter your answer: ")
        answer = lowercase(answer)
        #Check if the player's answer matches the correct answer
        if answer == word:
            answer_correct = True
            break
        else:
            attempts -= 1
            print("Your answer is wrong!")
            print(f"You have {attempts} attempts left")
            if attempts > 0:
                print("Here's another clue to help you find the word:")
                print(list[i])
                i += 1
            else:
                print("The correct word is:", word)
    # Return the result
    return answer_correct

#Role: Simulates the final treasure room challenge where the player uses clues to guess the correct code word.
# Parameters: none (all data is loaded from the TRClues.json file).
# Returns: 'True if the player wins and 'False' otherwise
def treasure_room():
    #Load the datas from the file and initialize variables
    with open("data/TRClues.json", "r") as f:
        tv_game = json.load(f)
    available_years=[]
    programs=[]
    show={}

    #Select a random year
    for year in tv_game["Fort Boyard"].keys():
        available_years.append(year)
    year=random.choice(available_years)

    #Select a random program
    for program in tv_game["Fort Boyard"][year].keys():
        programs.append(program)
    program=random.choice(programs)

    #Extract the code word and its clues
    for data in tv_game["Fort Boyard"][year][program].keys():
        show[data]=tv_game["Fort Boyard"][year][program][data]
    for key in show.keys():
        if key=='Clues':
            clues=show[key]
        if key=='CODE-WORD':
            code_word=lowercase(show[key])

    # The player takes guesses
    answer_correct=find_the_word(clues,code_word)

    # Return the result
    if answer_correct:
        print("Congratulations, you won!")
        return True
    else:
        print("Sorry, you lost!")
        return False