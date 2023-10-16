#!/usr/bin/expect

# sudo sed -i -e "s/13.68.202.114/$(INGRESS_IP)/g" ./python/api.json
# sudo sed -i '/uuid/d' ./python/api.json

# echo "step 1 - wget para buscar o swagger no POD"
# wget http://10.201.218.200/rlog/logistics-transport-order/v3/api-docs -O swagger.json  
# sudo chmod 777 swagger.json

echo "step 2 - export variaveis"
export WSO2_API_NAME="RLOG-TRANSPORT-ORDER-TRACKING-API"
export WSO2_API_VERSION="1.4.0.x"
export INGRESS_IP="10.201.218.200"
export INGRESS_URI="/rlog/rlog-transport-order-tracking-service"
export ENDPOINT="http://"$INGRESS_IP$INGRESS_URI

echo "step 3 - exec ajusta_especiais.py"
# chmod 777 ajusta_especiais.py
# python3 ajusta_especiais.py

echo "step 4 - exec modifica_swagger.py"
# chmod 777 modifica_swagger.py
# python3 modifica_swagger.py

# cat ./python/swagger.json
echo "step 5 - inicia importação no WSO2"

echo "step 5.1 - seta variaveis da task group"
export ambiente="https://rnndeva1wsof001.mycompany.com.br:9443"
export apiVersion="1.4.0.x"
export nomeapi="RLOG-TRANSPORT-ORDER-TRACKING-API"
export senha="YyCVW9Y9C8pMWnbT"
export usuario="devops"
export wso2env="dev"
export pathswagger="$nomeapi-$apiVersion/Meta-information"

echo "step 5.2 - sett default"
apictl set --mode default

echo "step 5.3 - verifica_env.sh"
chmod 777 verifica_env.sh
sh verifica_env.sh

echo "step 5.4 - list envs"
apictl list envs

echo "step 5.5 - apictl login"
apictl login $wso2env -u $usuario -p $senha -k --verbose

echo "step 5.6 - apictl list apis"
apictl list apis -e $wso2env -k --verbose --limit 100

echo "step 5.7 - apictl init"
apictl init $nomeapi --oas swagger.json -f --verbose

echo "step 5.8 - cria arquivo api.yaml novo"
# cp ./cria_swagger_json.sh ./$nomeapi/Meta-information/cria_swagger_json.sh
# chmod 777 ./$nomeapi/Meta-information/cria_swagger_json.sh
# sh ./$nomeapi/Meta-information/cria_swagger_json.sh
# cat ./$nomeapi/Meta-information/swagger.json
# cp ./modifica_endpoint.py ./$nomeapi/Meta-information/modifica_endpoint.py
mv ./$nomeapi/Meta-information/api.yaml ./$nomeapi/Meta-information/old_api.yaml.old 
python3 modifica_api_default.py
cp ./novo.yaml ./$nomeapi/Meta-information/api.yaml
# python3 ./$nomeapi/Meta-information/modifica_endpoint.py
# sudo rm ./$nomeapi/api_params.yaml
cat ./$nomeapi/Meta-information/api.yaml

# read -p "enter pra continuar"

echo "step 5.9 - apictl import-api"
apictl import-api -f ./$nomeapi -e $wso2env -k --update --verbose

echo "step 5.10 - apictl list apis"
apictl list apis -e $wso2env -k --verbose --limit 100 --query name $nomeapi

echo "step 5.11 - apictl change-status"
apictl change-status api -a Publish -n $nomeapi -v $apiVersion -e $wso2env -k --verbose

echo "step 5.12 - apictl list apis"
apictl list apis -e $wso2env -k --verbose --limit 100 --query name $nomeapi

echo "step 5.13 - logout"
apictl logout $wso2env --verbose

echo "step 5.14 - remove envs"
apictl remove env $wso2env --verbose
