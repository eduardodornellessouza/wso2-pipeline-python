import requests
import json
import os
import variables

def gera_token():
    url = variables.gera_token_url
    headers = { variables.gera_token_header_auth: variables.gera_token_header_auth_value }
    dataReq = { variables.gera_token_header_grant_type: variables.gera_token_header_grant_type_value, 
                variables.gera_token_header_username: variables.gera_token_header_username_value,
                variables.gera_token_header_password: variables.gera_token_header_password_value,
                variables.gera_token_header_scope: variables.gera_token_header_scope_value
            }

    request = requests.post(url, data=dataReq, headers=headers)
    response = request.json()
    global access_token
    access_token = "Bearer " + response["access_token"]
    
