import os

# export env_wso2=dev
# export nomeApp=rlog
# export nomeApi=RLOG-TRANSPORT-ORDER-API

# variaveis conforme ambiente do WSO2
if os.environ['env_wso2'] == 'dev':
    gera_token_url = "https://mydeva1.mycompany.com.br/token"
    busca_app_url = "https://myclouddeva1wsof001.mycompany.com.br:9443/api/am/store/v1/applications?query=" + os.environ['nomeApp']
    cria_app_url = "https://myclouddeva1wsof001.mycompany.com.br:9443/api/am/store/v1/applications"
    busca_apis_url = "https://myclouddeva1wsof001.mycompany.com.br:9443/api/am/publisher/v1.2/apis?query=" + os.environ['nomeApi']
    busca_subs_url = "https://myclouddeva1wsof001.mycompany.com.br:9443/api/am/publisher/v1.2/subscriptions?apiId="
    cria_subs_url = "https://myclouddeva1wsof001.mycompany.com.br:9443/api/am/store/v1/subscriptions"
    gera_token_header_auth_value = "Basic <token_dev>"
    gera_token_header_username_value = "<user_dev>"
    gera_token_header_password_value = "<pass_dev>"

if os.environ['env_wso2'] == 'hml':
    gera_token_url = "https://myhmla1.mycompany.com.br/token"
    busca_app_url = "https://mycloudhmla1wsof001.mycompany.com.br:9443/api/am/store/v1/applications?query=" + os.environ['nomeApp']
    cria_app_url = "https://mycloudhmla1wsof001.mycompany.com.br:9443/api/am/store/v1/applications"
    busca_apis_url = "https://mycloudhmla1wsof001.mycompany.com.br:9443/api/am/publisher/v1.2/apis?query=" + os.environ['nomeApi']
    busca_subs_url = "https://mycloudhmla1wsof001.mycompany.com.br:9443/api/am/publisher/v1.2/subscriptions?apiId="
    cria_subs_url = "https://mycloudhmla1wsof001.mycompany.com.br:9443/api/am/store/v1/subscriptions"
    gera_token_header_auth_value = "Basic <token_hml>"
    gera_token_header_username_value = "<user_hml>"
    gera_token_header_password_value = "<pass_hml>"

if os.environ['env_wso2'] == 'prd':
    gera_token_url = "https://mycloudprda1wsof001.mycompany.com.br:8243/token"
    busca_app_url = "https://mycloudprda1wsof001.mycompany.com.br:9443/api/am/store/v1/applications?query=" + os.environ['nomeApp']
    cria_app_url = "https://mycloudprda1wsof001.mycompany.com.br:9443/api/am/store/v1/applications"
    busca_apis_url = "https://mycloudprda1wsof001.mycompany.com.br:9443/api/am/publisher/v1.2/apis?query=" + os.environ['nomeApi']
    busca_subs_url = "https://mycloudprda1wsof001.mycompany.com.br:9443/api/am/publisher/v1.2/subscriptions?apiId="
    cria_subs_url = "https://mycloudprda1wsof001.mycompany.com.br:9443/api/am/store/v1/subscriptions"
    gera_token_header_auth_value = "Basic <token_prd>"
    gera_token_header_username_value = "<user_prd>"
    gera_token_header_password_value = "<pass_prd>"

# variáveis para geração de token
gera_token_header_auth = "Authorization"
gera_token_header_grant_type = "grant_type"
gera_token_header_grant_type_value = "password"
gera_token_header_username = "username"
gera_token_header_password = "password"
gera_token_header_scope = "scope"
gera_token_header_scope_value = "apim:api_view apim:api_create apim:api_delete apim:api_publish apim:subscription_view apim:subscription_block apim:external_services_discover apim:threat_protection_policy_create apim:threat_protection_policy_manage apim:document_create apim:document_manage apim:mediation_policy_view apim:mediation_policy_create apim:mediation_policy_manage apim:client_certificates_view apim:client_certificates_add apim:client_certificates_update apim:ep_certificates_view apim:ep_certificates_add apim:ep_certificates_update apim:publisher_settings apim:pub_alert_manage apim:shared_scope_manage apim:app_import_export apim:api_import_export apim:api_product_import_export apim:subscribe apim:app_manage apim:sub_manage"

# variáveis para busca da aplicação e criação da aplicação
busca_app_headers_content_type = "Content-Type"
busca_app_headers_content_type_value = "application/json"
busca_app_headers_accept_charset = "Accept-Charset"
busca_app_headers_accept_charset_value = "UTF-8"
busca_app_headers_auth = "Authorization"
cria_app_name = "name"
cria_app_name_value = os.environ['nomeApp']
cria_app_throttlingPolicy = "throttlingPolicy"
cria_app_throttlingPolicy_value = "Unlimited"
cria_app_description = "description"
cria_app_description_value = os.environ['nomeApp']
cria_app_tokenType = "tokenType"
cria_app_tokenType_value = "JWT"

# variaveis para busca de apis
busca_apis_header_auth = "Authorization"

# variaveis para busca de subscricoes e criação de subscrições
busca_subs_header_auth = "Authorization"
cria_sub_status = "UNBLOCKED"