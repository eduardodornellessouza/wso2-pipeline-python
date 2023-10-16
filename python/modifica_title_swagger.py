import json
import os

with open('swagger.json', 'r') as arq:
    # le o arquivo inteiro
    obj = json.load(arq)

    obj_info = obj['info']

    obj_info['title'] = os.environ.get('nomeapi')
    os.environ['SWAGGER_VERSION'] = obj_info['version']

with open('swagger.json', 'w') as arq:
    json.dump(obj, arq, indent=2)   

arquivo = open("arquivo.txt", "a")
arquivo.write(os.environ['SWAGGER_VERSION'])
