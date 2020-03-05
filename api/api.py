import requests

def get_json_request(current_url, task):
    resp = requests.post(current_url, json=task)
    return resp.json()

def clean_json_request(j_request, key, item):
    temp_dict = {}
    for line in j_request:
        temp_dict[line[key]] = line[item]
    return temp_dict