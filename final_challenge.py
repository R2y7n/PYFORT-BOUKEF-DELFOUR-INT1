import json
import random

def lowercase(str):
    str_lower=''
    for char in str:
        if 'A' <= char <= 'Z':
            str_lower += chr(ord(char) + 32)
        else:
            str_lower += char
    return str_lower

def find_the_word(list,word):
    print("You have to find the final word to open the treasure room")
    print("Here are the first three clues, you have three attempts to find the word:")
    for i in range(3):
        print(list[i])
    attempts = 3
    i = 4
    answer_correct = False
    while attempts > 0:
        answer = input("Please enter your answer: ")
        answer = lowercase(answer)
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
    return answer_correct

def treasure_room():
    with open("data/TRClues.json", "r") as f:
        tv_game = json.load(f)
    available_years=[]
    programs=[]
    show={}
    for year in tv_game["Fort Boyard"].keys():
        available_years.append(year)
    year=random.choice(available_years)
    for program in tv_game["Fort Boyard"][year].keys():
        programs.append(program)
    program=random.choice(programs)
    for data in tv_game["Fort Boyard"][year][program].keys():
        show[data]=tv_game["Fort Boyard"][year][program][data]
    for key in show.keys():
        if key=='Clues':
            clues=show[key]
        if key=='CODE-WORD':
            code_word=lowercase(show[key])
    answer_correct=find_the_word(clues,code_word)
    if answer_correct:
        print("Congratulations, you won!")
        return True
    else:
        print("Sorry, you lost!")
        return False






