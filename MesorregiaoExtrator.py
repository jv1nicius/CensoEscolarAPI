import json

with open('./municipios.json', 'r', encoding='utf-8') as f:
    dados_json = json.load(f)

mesorregioes = []

for item in dados_json:
    mesorregiao = item['microrregiao']['mesorregiao']
    if (mesorregiao not in mesorregioes):
        mesorregioes.append(mesorregiao)

with open('mesorregioes.json', 'w', encoding='utf-8') as f:
    json.dump(mesorregioes, f, ensure_ascii=False, indent=4)