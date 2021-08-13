import json
data={"name": "David","class":"I","age": 6}
with open("data.json","w")as k:
    json.dump(data,k,indent=4)


