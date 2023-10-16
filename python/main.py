import variables
import os
import step1_gera_token
import step2_busca_app
import step3_lista_apis
import step4_busca_subs_api

# gera token
step1_gera_token.gera_token()
print("step1 - Access Token gerado: " + step1_gera_token.access_token)

# busca APP
step2_busca_app.busca_app(step1_gera_token.access_token)
if step2_busca_app.applicationId == "sem_id":
    print("step2 - ID da Aplicação " + os.environ['nomeApp'] + " não encontrado")
    step2_busca_app.cria_app(step1_gera_token.access_token)
    print("step3 - ID da nova Aplicação: "+ step2_busca_app.applicationId)
else:
    print("step2 - ID da Aplicação: "+ step2_busca_app.applicationId)

# busca apis
step3_lista_apis.busca_apis(step1_gera_token.access_token)
print("step3 - ID da API: "+ step3_lista_apis.idAPI + " - Nome da API: "+ step3_lista_apis.nomeAPI)

# busca subscricoes
step4_busca_subs_api.busca_subs(step1_gera_token.access_token,step3_lista_apis.idAPI,step3_lista_apis.nomeAPI)

# subscreve a APP na API
if step3_lista_apis.statusApi == "PUBLISHED":
    print("step5 - Inicia subscrição da API " + step3_lista_apis.idAPI + " na aplicação " + step2_busca_app.applicationId)
    step4_busca_subs_api.inclui_subs(step1_gera_token.access_token,step3_lista_apis.idAPI,step2_busca_app.applicationId)
else:
    print("step5 - A API se encontra no status " + step3_lista_apis.statusApi + ". Para adicionar subscrições, é necessário publicar a API!")
