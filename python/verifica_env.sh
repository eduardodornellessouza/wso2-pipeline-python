export usuarioatual=$(users)
export env_vazia="environments: {}"
export env_apictl=$(grep "environments: {}" /Users/$usuarioatual/.wso2apictl/main_config.yaml) 
echo "usuarioatual: " $usuarioatual
echo "env_vazia: " $env_vazia
echo "env_apictl: " $env_apictl
if [ "$env_vazia" = "$env_apictl" ]; then
    echo "ïnclui variavel"
    apictl add-env -e $wso2env --apim $ambiente
else
    echo "remove variavel existente"
    apictl remove env $wso2env --verbose
    echo "ïnclui nova variavel"
    if [ $wso2env = "prd" ]; then
        apictl add-env -e prd \
        --apim https://mycloudprda1wsof001.mycompany.com.br:9443 \
        --registration https://mycloudprda1wsof001.mycompany.com.br:9443 \
        --publisher https://mycloudprda1wsof001.mycompany.com.br:9443 \
        --devportal  https://mycloudprda1wsof001.mycompany.com.br:9443 \
        --admin  https://mycloudprda1wsof001.mycompany.com.br:9443 \
        --token https://myprda1.mycompany.com.br/token
    else
        apictl add-env -e $wso2env --apim $ambiente
    fi
fi
apictl list env
