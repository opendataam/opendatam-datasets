import json

for l in open('data.jsonl', 'r', encoding='utf8'):
    data = json.loads(l)
    if 'cardData' in data.keys() and 'language' in data['cardData'].keys():
        if len(data['cardData']['language']) == 1:
            print(l.strip())