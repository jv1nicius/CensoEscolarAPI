import requests
import json

API = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

DADOS_API = requests.get(API)
DADOS_JSON = DADOS_API.json()

REGIAO = 'Nordeste'
estadosNordeste = []

for estado in DADOS_JSON:
    if (estado['regiao']['nome'] == REGIAO):
        estadosNordeste.append(estado)

with open('Ufs.json', 'w', encoding='utf-8') as dadosJson:
    json.dump(estadosNordeste, dadosJson, indent="\t", ensure_ascii=False)