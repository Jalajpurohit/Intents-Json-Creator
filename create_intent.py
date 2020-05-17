import re, csv, json
from copy import deepcopy
from pprint import pprint


with open(r'intent_main.json') as f:
    template_main=json.loads(f.read())
with open(r'intent_usersays_en.json') as f:
    template_userSays=json.loads(f.read())

with open('intents.csv', encoding='cp1252') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count!=0:
            intentName= row[0]
            trainingPhrase = row[1]
            response = row[2]
            q_copy=deepcopy(template_main)
            u_copy=deepcopy(template_userSays)

            q_copy['name']=intentName
            q_copy['responses'][0]['messages'][0]['speech']= response
            u_copy[0]['data'][0]['text']=trainingPhrase

            with open(f'created_intents/{intentName}.json','w') as f:
                f.write(json.dumps(q_copy))
            with open(f'created_intents/{intentName}_usersays_en.json','w') as f:
                f.write(json.dumps(u_copy))
            
        line_count+=1
