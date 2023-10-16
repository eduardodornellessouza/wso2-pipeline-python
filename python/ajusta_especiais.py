import unicodedata
import re
import json 
import os
import codecs

filename = "swagger.json"
filename_new = "new_swagger.json"

fdata = codecs.open(filename, 'r+', encoding='mac_latin2',errors='replace')
conteudo = fdata.read()
fdata.seek(0)
fdata.write(conteudo)
url_prd_old = "ÔŅĹ"
url_prd_new = "_"
conteudo = conteudo.replace(url_prd_old, url_prd_new)

url_prd_old = "ę"
url_prd_new = "_"
conteudo = conteudo.replace(url_prd_old, url_prd_new)

url_prd_old = "Ľ"
url_prd_new = "_"
conteudo = conteudo.replace(url_prd_old, url_prd_new)

url_prd_old = "„"
url_prd_new = "_"
conteudo = conteudo.replace(url_prd_old, url_prd_new)

url_prd_old = "√ß"
url_prd_new = "_"
conteudo = conteudo.replace(url_prd_old, url_prd_new)

url_prd_old = "√£"
url_prd_new = "_"
conteudo = conteudo.replace(url_prd_old, url_prd_new)

with open(filename, 'w', encoding='utf-8') as swagger:
	swagger.write(conteudo)

fdata.close()
swagger.close()
