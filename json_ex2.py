import json

dict_data = {'Name' : 'Kim', 'Department' : 'IoT', 'University' : 'Soonchunhyang'}

with open('data.json', 'w') as f:
    json.dump(dict_data, f)