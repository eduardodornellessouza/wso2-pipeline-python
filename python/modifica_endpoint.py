import json
import os

with open('swagger.json', 'r') as arq:
    # le o arquivo inteiro
    obj = json.load(arq)

    # pega o objeto INFO do Json
    novaurl = obj['openapi']
    print(novaurl)