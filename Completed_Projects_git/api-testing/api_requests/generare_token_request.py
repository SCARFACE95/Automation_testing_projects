import random

import requests


def get_token():
    endpoint = "https://simple-books-api.glitch.me//api-clients/"

    random_number = random.randint(1, 9999999999999999)

    #here is the payload sent to server for autentication
    request_body = {
             "clientName": "Postman_Andrei_Robert",
             "clientEmail": f"BST{random_number}@gmail.com"
            }
    response = requests.post(url=endpoint, json=request_body)

    #asa returnam token-ul care s-a primit de la server si ne folosim de el si il returnam
    token = response.json()['accessToken']
    return token

print(get_token())