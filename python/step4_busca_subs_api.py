import requests
import json
import os
import variables
import step2_busca_app 
import step3_lista_apis

def busca_subs(token, idAPI, nomeAPI):
    url = variables.busca_subs_url + idAPI
    headers = { variables.busca_subs_header_auth: token }
    request = requests.get(url, headers=headers)
    response = request.json()
    if response["count"] == 0:
        print("step4 - Não foram encontradas subscrições ativas para essa API")
    else:
        print("step4 - Lista subscricoes da API: " + nomeAPI)
        print("--------------------------------- || ---------------------------------")
        list = response["list"]
        for item in list:
            print("ID da Subscrição: "+ item['subscriptionId'])
            print(json.dumps(item['applicationInfo'], indent=4, sort_keys=True))

def inclui_subs(token, idAPI, idAPP):
    url = variables.cria_subs_url
    headers = { variables.busca_app_headers_content_type: variables.busca_app_headers_content_type_value, 
                variables.busca_app_headers_auth: token }
    dataReq = '{\"applicationId\":"'+ idAPP +'",\"throttlingPolicy\": "'+ variables.cria_app_throttlingPolicy_value +'",\"apiId\":"'+ idAPI +'",\"requestedThrottlingPolicy\": "'+ variables.cria_app_throttlingPolicy_value +'",\"status\": "'+ variables.cria_sub_status +'"\r\n\t}'
    request = requests.post(url, data=dataReq, headers=headers)
    response = request.json()
    print(json.dumps(response, indent=4, sort_keys=True))
    
    