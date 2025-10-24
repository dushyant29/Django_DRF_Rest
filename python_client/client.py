import requests

endpoint ="http://127.0.0.1:8000/car/list"
getresponse = requests.get(endpoint)
print(getresponse.json())
print(f'This is status code-{getresponse.status_code}')

