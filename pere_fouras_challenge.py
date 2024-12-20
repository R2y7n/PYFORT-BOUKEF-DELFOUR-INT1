import json


def load_riddles(file):
   d={}
   with open(file, 'r', encoding='utf-8') as f:
       content = f.readlines()
       for i in range(len(content)):
            riddle=json.load(content[i])
            for j in riddle:
                for k in riddle[j]:
                    if k=='question':
                        question=riddle[j][k]
                    if k=='answer':
                        answer=riddle[j][k]
                    d1={
                        'question':question,
                        'answer':answer
                    }
            d.append(d1)
       print(d)


load_riddles('data/PFRiddles.json')