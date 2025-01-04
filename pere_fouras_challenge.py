# Fort Boyard Project
# Authors : Anaïs Delfour, Rayane Boukef
# Role: allows to recreate Père Fouras famous and key riddle

import json
import random

# Role: converts a given string to lowercase manually, without using '.lower()' method
# Parameters: a string
# Returns: a new string where all uppercase letters in the input have been converted to lowercase
def lowercase(str):
    str_lower=''
    for char in str:
        # If the character is uppercase, converts it in lowercase
        if 'A' <= char <= 'Z':
            str_lower += chr(ord(char) + 32)
        # If the character is not uppercase, leaves it unchanged
        else:
            str_lower += char
    return str_lower

# Role: loads riddles from a JSON file
# Parameters: a JSON file
# Returns: a list of dictionaries (each dictionary represents a riddle)
def load_riddles(file):
    # Open the file and load its content
    with open(file, 'r') as file:
        riddles_data = json.load(file)

    riddles = []
    # Only extracts questions and answers from riddles_data
    for riddle in riddles_data:
        if 'question' in riddle and 'answer' in riddle:
            riddles.append({
                'question': riddle['question'],
                'answer': riddle['answer']
            })

    return riddles



# Role: presents a père fouras' riddle to the player
# Parameters: none
# Returns: 'True' if the player answers the riddle correctly and 'False' otherwise
def pere_fouras_riddles():
    print("You are facing Père Fouras. Answer correctly his riddle to win a key.")
    # Loads the riddle and selects one randomly
    list_riddles = load_riddles('data/PFRiddles.json')
    selected_riddle=random.choice(list_riddles)
    print (selected_riddle['question'])

    # Prepare the answer for comparison
    riddle_answer_lower = lowercase(selected_riddle['answer'])
    words_in_answer=riddle_answer_lower.split()

    attempt=3
    # The player has 3 attempts to answer correctly
    while attempt > 0:
        answer=input("Please enter your answer:")
        answer_lower=lowercase(answer)

        # Checks if the player's answer is correct and return if he has won or not
        if answer_lower == riddle_answer_lower or answer_lower+'s' == riddle_answer_lower or answer_lower in words_in_answer or answer_lower+'s' in words_in_answer:
            print("Your answer is correct !")
            print("You win a key !")
            return True
        else:
            print("Your answer is incorrect !")
            attempt-=1
            print(f"You have {attempt} attempts left")
    print("You lose the key !")
    print("The correct answer was:" , selected_riddle['answer'])
    return False