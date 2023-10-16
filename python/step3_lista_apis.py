import requests
import json
import os
import variables

def busca_apis(token):
    url = variables.busca_apis_url
    # headers = { variables.busca_apis_header_auth: token }
    headers = "Authorization: " + token

    print("printa url: " + url)
    print("printa headers: " + headers)

    request = requests.get(url, headers=headers)
    print("printa request: " + request)
    response = request.json()
    print("printa response: " + response) 
    list = response["list"]
    print("printa list: " + list)


    for item in list:
        global idAPI
        idAPI = item['id']
        global nomeAPI
        nomeAPI = item['name']
        global statusApi
        statusApi = item['lifeCycleStatus']






