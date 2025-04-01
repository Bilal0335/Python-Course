import json


with open('my_data.json','r') as f:
    json_obj = json.load(f)
    # f.read()
    
print(json_obj)
print(json_obj['peoples'][0]['age'])