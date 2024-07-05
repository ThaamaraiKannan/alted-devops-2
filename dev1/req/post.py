import requests
import json

def dummy_post():
    url = 'https://dummyjson.com/auth/login'
    headers = { 'Content-Type': 'application/json' }
    payload = {
    "username": 'emilys',
    "password": 'emilyspass',
    "expiresInMins": 30 }
    json_str = json.dumps(payload)
    response = requests.post(url=url, data=json_str,headers=headers )
    print(response.json())
    return

dummy_post()