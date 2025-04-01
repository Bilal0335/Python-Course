
# ! JSON Pratice

import json
myDict = {
    'peoples':[
        {
            'name': 'John Doe',
            'age': 30,
            'city': 'New York'
        }
        ,
        {
            'name': 'Jenny',
            'age': 28,
            'city': 'Los Angeles'
        }
        ,
        {
            'name': 'Sarah',
            'age': 32,
            'city': 'Chicago'
        }
    ]
} 

# print(myDict)

'''
! load
! dumps
'''

json_str = json.dumps(myDict,indent=4)
with open('my_data.json','w') as f:
    f.write(json_str)