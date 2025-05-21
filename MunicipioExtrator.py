import requests
import json

API = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"

DADOS_API = requests.get(API)
DADOS_JSON = DADOS_API.json()

REGIAO = 'Nordeste'
municipiosNordeste = []

for municipio in DADOS_JSON:
    if (municipio['microrregiao']):
        if (municipio['microrregiao']['mesorregiao']['UF']['regiao']['nome'] == REGIAO):
            municipiosNordeste.append(municipio)
    else:
        pass

with open('municipios.json', 'w', encoding='utf-8') as dadosJson:
    json.dump(municipiosNordeste, dadosJson, indent="\t", ensure_ascii=False)