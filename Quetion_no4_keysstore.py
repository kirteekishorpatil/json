import json
data={'4': 5,
    '6': 7, 
    '1': 3, 
    '2': 4}
print(json.dumps(data,indent=2,sort_keys=True))
