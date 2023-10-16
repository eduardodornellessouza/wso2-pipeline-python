# Documentacao WSO2
APICTL          - https://apim.docs.wso2.com/en/3.1.0/learn/api-controller/getting-started-with-wso2-api-controller/
Sample Deploy   - https://apim.docs.wso2.com/en/3.1.0/learn/api-controller/importing-apis-via-dev-first-approach/

# WSO2 DEV
Usuário:        devops
Senha:          YyCVW9Y9C8pMWnbT
apim Azure:     https://mydeva1.mycompany.com.br:9443/token
apim OCI:       https://mydevo1.mycompany.com.br:9443/token 
registration:   https://myclouddeva1wsof001.mycompany.com.br:9443
admin:          https://myclouddeva1wsof001.mycompany.com.br:9443/admin 
publisher:      https://myclouddeva1wsof001.mycompany.com.br:9443/publisher 
devportal:      https://myclouddeva1wsof001.mycompany.com.br:9443/devportal

curl --location --request POST 'https://mydeva1.mycompany.com.br/token' -d "grant_type=client_credentials" --header 'Authorization: Basic NGVUWWtyTUdIMGZaTVNPdXJlMm5IMGtXekM0YTpkVEJZdjJuN2hvaDRjNTBfYTVCVFFEbTYxaWNh'


 curl -X POST -H "Authorization: Basic ZGV2b3BzOll5Q1ZXOVk5QzhwTVduYlQ" -H "Content-Type: application/json" -d @payload.json https://mydeva1.mycompany.com.br/client-registration/v0.16/register

# modo default ou kubernetes
apictl set --mode default

# cria variaveis de conexao com ambiente
apictl add-env -e dev --apim https://myclouddeva1wsof001.mycompany.com.br:9443 
apictl add-env -e dev --apim https://mydevo1.mycompany.com.br:9443/token 

# pra remover ENV
apictl remove env dev --verbose

# faz login 
apictl login dev -u devops -p 
 -k --verbose

# faz logout
apictl logout -e dev --verbose

# lista apis
apictl list apis -e dev -k --verbose --limit 100 
apictl list apis -e dev -k --verbose --limit 100 --query name OMS

# cria o projeto
 - yaml:    apictl init SampleAPI --definition definition.yaml --force=true --verbose
 - swagger: apictl init api-importada-via-devops --oas api-importada-via-devops.yaml --verbose

# importa api
apictl import-api -f ./api-importada-via-devops -e dev -k --verbose

# publica apoi
apictl change-status api -a Publish -n lab-test-wso2 -v 1.0.0 -e dev -k --verbose

# apaga api
apictl delete api -n lab-wso2-test -v 1.0.0 -e dev -k --verbose


## API WSO2
DevPortal:  https://apim.docs.wso2.com/en/3.2.0/develop/product-apis/devportal-apis/devportal-v1/devportal-v1/
Publisher:  https://apim.docs.wso2.com/en/3.2.0/develop/product-apis/publisher-apis/publisher-v1/publisher-v1/

# auth
curl -X POST -H "Authorization: Basic ZGV2b3BzOll5Q1ZXOVk5QzhwTVduYlQ" -H "Content-Type: application/json" -d @payload.json https://myclouddeva1wsof001.mycompany.com.br:9443/client-registration/v0.16/register

# gera token
curl -k -X POST 'https://mydeva1.mycompany.com.br/token' -d 'grant_type=password&username=admin&password=zvdcgh44LFVKdqp3&scope=apim:api_view apim:api_create apim:api_delete apim:api_publish apim:subscription_view apim:subscription_block apim:external_services_discover apim:threat_protection_policy_create apim:threat_protection_policy_manage apim:document_create apim:document_manage apim:mediation_policy_view apim:mediation_policy_create apim:mediation_policy_manage apim:client_certificates_view apim:client_certificates_add apim:client_certificates_update apim:ep_certificates_view apim:ep_certificates_add apim:ep_certificates_update apim:publisher_settings apim:pub_alert_manage apim:shared_scope_manage apim:app_import_export apim:api_import_export apim:api_product_import_export' --header 'Authorization: Basic ZWFGNXpUajNtdkNCS3JadG9qdWZIcGlBRGNBYToxaTlxVlU3a1BPU2RpSnowOHpXQUhuckdVSG9h'

# lista apis
curl --location --request GET 'https://myclouddeva1wsof001.mycompany.com.br:9443/api/am/publisher/v1.2/apis?query=OMS-COMMERCE-API' --header 'Authorization: Bearer <my_token>'

# lista apps
curl -k -H 'Authorization: Bearer <my_token>' 'https://myclouddeva1wsof001.mycompany.com.br:9443/api/am/store/v1/applications'

# cria nova APP
curl --location --request POST 'https://myclouddeva1wsof001.mycompany.com.br:9443/api/am/store/v1/applications' \
--header 'Authorization: Bearer <my_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "name": "CalculatorApp",
  "throttlingPolicy": "Unlimited",
  "description": "Sample calculator application",
  "tokenType": "JWT",
  "groups": [],
  "attributes": {},
  "subscriptionScopes": []
}'

# lista subscricoes
curl -k -H "Authorization: Bearer <my_token>" "https://myclouddeva1wsof001.mycompany.com.br:9443/api/am/publisher/v1/subscriptions?apiId=03402be2-ba7b-4f30-8828-b3c71092ae10"


# criar nova subscricao
curl --location --request POST 'https://myclouddeva1wsof001.mycompany.com.br:9443/api/am/store/v1/subscriptions' \
--header 'Authorization: Bearer <my_token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "applicationId":"461eec98-15d6-40d1-b751-3287ceb49d94",
    "throttlingPolicy": "Unlimited",
    "apiId":"d3a31529-43a5-45c5-8793-09b557d726fa",
    "requestedThrottlingPolicy": "Unlimited",
    "status": "UNBLOCKED"
}'