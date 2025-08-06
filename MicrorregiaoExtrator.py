import json

with open('./municipios.json', 'r', encoding='utf-8') as f:
    dados_json = json.load(f)

microrregioes = []

for item in dados_json:
    microrregiao = item['microrregiao']
    if (microrregiao not in microrregioes):
        microrregioes.append(microrregiao)

with open('microrregioes.json', 'w', encoding='utf-8') as f:
    json.dump(microrregioes, f, ensure_ascii=False, indent=4)