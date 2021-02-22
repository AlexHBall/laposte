import requests

BASE_URL="http://127.0.0.1:5000/v1/"
response = requests.post(BASE_URL + 'letter')
#response = requests.post(BASE_URL + f'key/{key}')
#response = requests.post(BASE_URL + 'letter/3P11111111110')
print(response.status_code)
print(response.text)
