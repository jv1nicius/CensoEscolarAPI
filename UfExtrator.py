import json


with open('./municipios.json', 'r', encoding='utf-8') as f:
    dados_json = json.load(f)

ufs = []

for item in dados_json:
    uf = item['microrregiao']['mesorregiao']['UF']
    if(uf not in ufs):
        ufs.append(uf)

with open('ufs.json', 'w', encoding='utf-8') as f:
    json.dump(ufs, f, ensure_ascii=False, indent=4)

""" import requests
import json

API = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

DADOS_API = requests.get(API)
DADOS_JSON = DADOS_API.json()

estados = []

for estado in DADOS_JSON:
    estados.append(estado)

with open('ufs.json', 'w', encoding='utf-8') as dadosJson:
    json.dump(estados, dadosJson, indent="\t", ensure_ascii=False) """