#!/bin/bash
DIR=$caminho
FILE=api.json
APIYAML=api.yaml

echo $DIR$FILE
echo $DIR$APIYAML

if [ -e "$DIR$FILE" ] ; then
    echo "Arquivo api.json existe!"
elif [ -e "$DIR$APIYAML" ] ; then
    yq e -o=json $DIR$APIYAML > $DIR$FILE
    cat api.json
    echo "Criado arquivo api.json!"
else       
    echo "Arquivo api.json nao existe."
    echo "Arquivo api.yaml tambem nao existe."
    echo "ATENCAO --> Verifique com o time de DEV"
fi
