import csv, json

escolas = []
regiao = "Nordeste"

def emptyToZero(valor):
    return 0 if valor == '' else valor

with open('./microdados_censo_escolar_2024/dados/microdados_ed_basica_2024.csv', 'r', encoding='latin1') as arquivo:
    reader = csv.DictReader(arquivo, delimiter=';')

    for row in reader:
        if row['NO_REGIAO'] == regiao:
            escola = {
                "NO_REGIAO": row["NO_REGIAO"],
                "CO_REGIAO": row["CO_REGIAO"],
                "NO_UF": row["NO_UF"],
                "SG_UF": row["SG_UF"],
                "CO_UF": row["CO_UF"],
                "NO_MUNICIPIO": row["NO_MUNICIPIO"],
                "CO_MUNICIPIO": row["CO_MUNICIPIO"],
                "NO_MESORREGIAO": row["NO_MESORREGIAO"],
                "CO_MESORREGIAO": row["CO_MESORREGIAO"],
                "NO_MICRORREGIAO": row["NO_MICRORREGIAO"],
                "CO_MICRORREGIAO": row["CO_MICRORREGIAO"],
                "NO_ENTIDADE": row["NO_ENTIDADE"],
                "CO_ENTIDADE": row["CO_ENTIDADE"],
                "QT_MAT_BAS": emptyToZero(row["QT_MAT_BAS"]),
                "QT_MAT_EJA": emptyToZero(row["QT_MAT_EJA"]),
                "QT_MAT_ESP": emptyToZero(row["QT_MAT_ESP"]),
                "QT_MAT_FUND": emptyToZero(row["QT_MAT_FUND"]),
                "QT_MAT_INF": emptyToZero(row["QT_MAT_INF"]),
                "QT_MAT_MED": emptyToZero(row["QT_MAT_MED"]),
                "QT_MAT_PROF": emptyToZero(row["QT_MAT_PROF"]),
            }

            escolas.append(escola)


with open('microdados2024.json', 'w', encoding='utf-8') as dadosJson:
    json.dump(escolas, dadosJson, indent=4, ensure_ascii=False)
