import requests
import json

API = "https://servicodados.ibge.gov.br/api/v1/localidades/microrregioes"

DADOS_API = requests.get(API)
DADOS_JSON = DADOS_API.json()

REGIAO = 'Nordeste'
microrregioesNordeste = []

for microrregiao in DADOS_JSON:
    if(microrregiao['mesorregiao']['UF']['regiao']['nome'] == REGIAO):
        microrregioesNordeste.append(microrregiao)

with open('microrregioes.json', 'w', encoding='utf-8') as dadosJson:
    json.dump(microrregioesNordeste, dadosJson, indent="\t", ensure_ascii=False)