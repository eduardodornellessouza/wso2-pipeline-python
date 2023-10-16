import requests
import json
import os
import variables
import step1_gera_token

global applicationId
applicationId = "sem_id"

def busca_app(token):
    url = variables.busca_app_url
    print(url)
    headers = { variables.busca_app_headers_content_type: variables.busca_app_headers_content_type_value, 
                variables.busca_app_headers_accept_charset: variables.busca_app_headers_accept_charset_value, 
                variables.busca_app_headers_auth: token }


    request = requests.get(url, headers=headers)
    response = request.json()
    list = response["list"]

    for item in list:
        global applicationId
        applicationId = item['applicationId']


def cria_app(token):
    url = variables.cria_app_url
    print(url)
    headers = { variables.busca_app_headers_content_type: variables.busca_app_headers_content_type_value, 
                variables.busca_app_headers_auth: token }
    # montando payload do tipo body/raw
    print(headers)
    dataReq = '{\"name\":"'+ variables.cria_app_name_value +'",\"throttlingPolicy\": "'+ variables.cria_app_throttlingPolicy_value +'",\"description\":"'+ variables.cria_app_description_value +'",\"tokenType\": "'+ variables.cria_app_tokenType_value +'"\r\n\t}'
    request = requests.post(url, data=dataReq, headers=headers)
    response = request.json()
    print(" ")
    print("Criada nova aplicacao com nome: " + response['applicationId'])
    print(json.dumps(response, indent=4, sort_keys=True))
    global applicationId
    applicationId = response['applicationId']
        
    