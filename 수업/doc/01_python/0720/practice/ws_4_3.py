import requests
from pprint import pprint as print

dummy_data = []
for i in range(1, 11):
    user_info = {}
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL).json()
    if (
        -80 < float(response['address']['geo']['lat']) < 80
        and -80 < float(response['address']['geo']['lng']) < 80
    ):
        user_info = {
            'name': response['name'],
            'lat': response['address']['geo']['lat'],
            'lng': response['address']['geo']['lng'],
            'company': response['company']['name'],
        }
        dummy_data.append(user_info)

print(dummy_data)