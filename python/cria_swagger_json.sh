#!/bin/bash
DIR=$caminho_endpoint/
FILE=swagger.json
APIYAML=swagger.yaml

echo $DIR$FILE
echo $DIR$APIYAML

echo "lista tudo"
tree


if [ -e "$DIR$FILE" ] ; then
    echo "Arquivo swagger.json existe!"
elif [ -e "$DIR$APIYAML" ] ; then
    yq e -o=json $DIR$APIYAML > $DIR$FILE
    cat swagger.json
    echo "Criado arquivo swagger.json!"
else       
    echo "Arquivo swagger.json nao existe."
    echo "Arquivo swagger.yaml tambem nao existe."
    echo "ATENCAO --> Verifique com o time de DEV"
fi
