#!/usr/bin/env python3

from tqdm import tqdm
import requests as req
import json

ACCESS_TOKEN = '???'
API_URL = '???' + 'api/v1/'

data = json.loads(open('data.json').read())

s = req.Session()
s.headers.update({'Authorization': f'Token {ACCESS_TOKEN}'})

for chal in tqdm(data):
    r = s.post(
        API_URL + 'challenges', 
        headers = {'Content-Type': 'application/json'}, 
        json = {
            'name': chal['name'], 
            'category': chal['category'], 
            'value': chal['value'], 
            'description': open('description/' + chal['description']).read(), 
            'type': chal['type'], 
            'state': chal['state'], 
        }
    )

    chal_id = r.json()['data']['id']

    s.post(
        API_URL + 'flags', 
        headers = {'Content-Type': 'application/json'}, 
        json = {
            'challenge_id': chal_id, 
            'type': 'static', 
            'content': chal['flag'], 
            'data': ''
        }
    )

    s.post(
        API_URL + 'files', 
        files = {'file': (chal['filename'], open('description/' + chal['file'], 'rb'))}, 
        data = {
            'challenge': chal_id, 
            'type': 'challenge'
        }
    )

    if 'hints' in chal:
        s.post(
            API_URL + 'hints', 
            headers = {'Content-Type': 'application/json'}, 
            json = {
                'challenge_id': chal_id, 
                'type': 'standard', 
                'cost': 0, 
                'content': open('description/' + chal['hints']).read()
            }
        )
