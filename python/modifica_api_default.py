import json
import yaml
import os

with open('swagger.json', 'r') as arq:
    # le o arquivo inteiro
    obj = json.load(arq)

    obj_info = obj['info']

    nome_api = obj_info['title']
    versao_api = obj_info['version']
    descricao_api = obj_info['description']

    # pega o objeto INFO do Json
    url = obj['servers'][0]
    contexto = str(url)
    tam = len(contexto)  
    contexto = contexto[9:tam]
    fim = int(contexto.rfind("'}"))
    contexto = contexto[0:fim]

    print('nome: ' + nome_api)
    print('versao: ' + versao_api)
    print('descricao: ' + descricao_api)
    print('contexto: ' + contexto)
    
with open('api-default.json', 'r') as arq:
    # le o arquivo inteiro
    obj = json.load(arq)

    obj['description'] = descricao_api
    obj['context'] = contexto + "/{version}"
    obj['contextTemplate'] = contexto + "/{version}"
    obj['productionUrl'] = os.environ.get('ENDPOINT') + "/v1"
    obj['sandboxUrl'] = os.environ.get('ENDPOINT') + "/v1"

    # pega o objeto INFO do Json
    obj_id = obj['id']
    obj_id['apiName'] = nome_api
    obj_id['version'] = versao_api   


with open('api_default_novo.json', 'w') as arq:
    json.dump(obj, arq, indent=2)


with open('api_default_novo.json', 'r') as arq:
    obj = json.load(arq)
    
    file = open("novo.yaml","w")
    yaml.dump(obj,file)
    file.close()
    print("YAML file saved.")
    

'''
# grava Variaveis de Ambiente
if not os.environ.get('WSO2_API_NAME') is None:
	wso2_api_nome = os.environ['WSO2_API_NAME']
	print('python wso2_api_nome: ' + wso2_api_nome)

if not os.environ.get('WSO2_API_VERSION') is None:
	wso2_api_version = os.environ['WSO2_API_VERSION']
	print('python wso2_api_version: ' + wso2_api_version)

if not os.environ.get('INGRESS_IP') is None:
	wso2_ingress_ip = os.environ['INGRESS_IP']
	print('python wso2_ingress_ip: ' + wso2_ingress_ip)

# metodo para pegar o Endpoint da API
# file1 = open('api.json', 'r')
# count = 0

# for line in file1:
#     count += 1
#     if "url" in line:
#         str = line
#         tam = len(str)
#         ini = str.rfind("http://")
#         endpoint = str[ini:tam]
#         fin = int(endpoint.find(","))-2
#         endpoint = endpoint[0:fin]

# with open('api.json', 'r') as arq:
#     obj = json.load(arq)
#     basepath = obj['context']
#     pos = int(basepath.rfind("/"))+1
#     # basepath = basepath[0:pos]

# metodo para extrair o basepath do endpoint
# str_de = "http://" + wso2_ingress_ip + "/"
# str_para = "/"
# basepath = endpoint.replace(str_de,str_para)

basepath = "/supplyChainLogistics/transportationManagement/rlog/transportOrder/v1"
endpoint = "http://10.201.218.200/rlog/logistics-transport-tracking/"

with open('swagger.json', 'r') as arq:
    # le o arquivo inteiro
    obj = json.load(arq)

    # pega o objeto INFO do Json
    obj_info = obj['info']
    obj_info['title'] = wso2_api_nome
    obj_info['version'] = wso2_api_version   

    # modifica Host e BasePath
    obj['host'] = endpoint
    obj['basePath'] = basepath


with open('swagger.json', 'w') as arq:
    json.dump(obj, arq, indent=2)
'''