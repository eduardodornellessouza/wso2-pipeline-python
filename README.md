# Repositório para execução de Deploy Automatizado de APIs no WSO2
    01 - realiza checkout do repositório onde está o swagger da api
    02 - realiza checkout do repositório onde está o Python que complementa o processo (wso2-deploy-template)
    03 - move arquivo swagger para pasta do Python
    04 - faz o replace dos parametros Host e Path do swagger conforme variaveis do pipeline
    05 - copia swagger modificado para pasta root onde o agente está executando o pipeline
    ------ Abaixo os comandos do Operador da WSO2
    06 - seta modo default: apictl set --mode default
    07 - executa shell script para incluir o ambiente do WSO2 na qual o Operador irá conectar - apictl add-env -e $wso2env --apim $ambiente
    08 - faz login no WSO2 - apictl login dev -u devops-k --verbose
    09 - lista apis - apictl list apis -e dev -k --verbose --limit 100
    10 - inicia o projeto - apictl init OMS-COMMERCE-API --oas swagger.json --verbose copy
    11 - importa o swagger para criar a API - apictl import-api -f ./OMS-COMMERCE-API -e dev -k --verbose
    12 - lista novamente as APIs - apictl list apis -e dev -k --verbose --limit 100 --query name OMS-COMMERCE-API
    13 - altera o status da API para Publicada - apictl change-status api -a Publish -n OMS-COMMERCE-API -v 2.0.1 -e dev -k --verbose
    14 - lista novamente as APIs - apictl list apis -e dev -k --verbose --limit 100 --query name OMS-COMMERCE-API
    15 - faz logout do WSO2 - apictl logout https://rnndeva1wsof001.mycompany.com.br:9443 --verbose
    16 - remove variáveis para conexão - apictl remove env dev --verbose
    ------ Abaixo executa aplicação python para subscrever API 
    17 - python3 main.py
    o python utiliza a API do API Manager para manipular as informações
    step1 - gera token para conectar na api
    step2 - busca Aplicação conforme variável do Pipeline (cria uma nova aplicação caso não exista)
    step3 - lista apis com o nome da API conforme variável do Pipeline
    step4 - busca subscrições da api
    step5 - Inicia subscrição da API na aplicação
    step6 - Caso a API se encontre no status diferente de Publicado, o Pipeline mosta o erro e não executa mais nada
    