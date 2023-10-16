import json
import os

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
