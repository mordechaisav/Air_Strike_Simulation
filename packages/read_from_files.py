import json
def read_from_json(path):
    with open(path, 'r') as file:
        json_data = file.read()
    data = json.loads(json_data)
    return data