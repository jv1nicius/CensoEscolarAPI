import requests
import json

API = "https://servicodados.ibge.gov.br/api/v1/localidades/mesorregioes"

DADOS_API = requests.get(API)
DADOS_JSON = DADOS_API.json()

REGIAO = 'Nordeste'
mesorregioesNordeste = []

for mesorregiao in DADOS_JSON:
    if(mesorregiao['UF']['regiao']['nome'] == REGIAO):
        mesorregioesNordeste.append(mesorregiao)

with open('mesorregioes.json', 'w', encoding='utf-8') as dadosJson:
    json.dump(mesorregioesNordeste, dadosJson, indent="\t", ensure_ascii=False)