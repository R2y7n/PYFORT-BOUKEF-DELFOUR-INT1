import json


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
