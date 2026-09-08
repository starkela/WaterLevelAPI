import requests
from random import randrange

url = "http://10.17.168.82:5000/add"
headers = {'Content-Type': 'application/json'}

# Reuses the underlying TCP connection
with requests.Session() as session:
        data = {"waterlevel": randrange(3000)}
        response = session.post(url, json=data, headers=headers)