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

def load_riddles(file):
    with open(file, 'r') as file:
        riddles_data = json.load(file)
    riddles = []
    for riddle in riddles_data:
        if 'question' in riddle and 'answer' in riddle:
            riddles.append({
                'question': riddle['question'],
                'answer': riddle['answer']
            })

    return riddles

print(load_riddles('data/PFRiddles.json'))


def pere_fouras_riddles():
    list_riddles = load_riddles('data/PFRiddles.json')
    selected_riddle=random.choice(list_riddles)
    print (selected_riddle['question'])
    selected_riddle_lower = lowercase(selected_riddle['answer'])
    attempt=3
    while attempt > 0:
        answer=input("Please enter your answer:")
        answer_lower=lowercase(answer)
        if answer_lower == selected_riddle_lower:
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

pere_fouras_riddles()
