import requests
from time import sleep
headers =  {'Content-Type': 'application/json; charset=utf-8'}
url = "http://localhost:5000/add"

for i in range(9):
    sleep(5)
    data = {"waterlevel" : 300 * i}
    response = requests.post(url, json=data , headers=headers )


if response.status_code == 200:
    print(data)
else:
    print("invalid")