import sqlite3
import json

# 1 - Abrir a conexão
conn = sqlite3.connect('censoescolarExtrator.db')
cursor = conn.cursor()

#inserir estados
with open("schemas.sql", "r", encoding="utf-8") as sql_file:
    sql_script = sql_file.read()
    cursor.executescript(sql_script)

with open("microdados2024.json", "r", encoding="utf-8") as json_file:
    dados = json.load(json_file)
for item in dados:
    cursor.execute("""
        INSERT INTO tb_instituicao (
            no_regiao, co_regiao, no_uf, sg_uf, co_uf, no_municipio, co_municipio, no_mesorregiao, co_mesorregiao, no_microrregiao, co_microrregiao, no_entidade, co_entidade, qt_mat_bas, qt_mat_eja, qt_mat_esp, qt_mat_fund, qt_mat_inf, qt_mat_med, qt_mat_prof
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        item["no_regiao"], item["co_regiao"], item["no_uf"], item["sg_uf"], item["co_uf"], item["no_municipio"], item["co_municipio"], item["no_mesorregiao"], item["co_mesorregiao"], item["no_microrregiao"], item["co_microrregiao"], item["no_entidade"], item["co_entidade"], item["qt_mat_bas"], item["qt_mat_eja"], item["qt_mat_esp"], item["qt_mat_fund"], item["qt_mat_inf"], item["qt_mat_med"], item["qt_mat_prof"]
    ))
    
with open("UFs.json", "r", encoding="utf-8") as ufs:
    dadosUf = json.load(ufs)
for uf in dadosUf:
    cursor.execute("INSERT INTO tb_uf (id, uf, nome, regiao) VALUES (?, ?, ?, ?)", (
        uf['id'],
        uf['sigla'],
        uf['nome'],
        uf['regiao']['nome']
    ))

with open("microrregioes.json", "r", encoding="utf-8") as microrregioesFile:
    microrregioes = json.load(microrregioesFile)
for mcrrg in microrregioes:
    cursor.execute(
        "INSERT INTO tb_messoregiao (cod_municipio, nome, cod_microrregiao, cod_mesorregiao, cod_uf) VALUES (?, ?, ?, ?, ?)",
        (
            mcrrg['id'],
            mcrrg['nome'],
            mcrrg['mesorregiao']['id'],
            mcrrg['mesorregiao']['UF']['id']
        )
    )

with open("municipios.json", "r", encoding="utf-8") as municipiosFile:
    municipios = json.load(municipiosFile)
for mncp in municipios:
    cursor.execute(
        "INSERT INTO tb_municipio (cod_municipio, nome, cod_microrregiao, cod_mesorregiao, cod_uf) VALUES (?, ?, ?, ?, ?)",
        (
            mncp['id'],
            mncp['nome'],
            mncp['microrregiao']['id'],
            mncp['microrregiao']['mesorregiao']['id'],
            mncp['microrregiao']['mesorregiao']['UF']['id']
        )
    )

with open("mesorregioes.json", "r", encoding="utf-8") as mesorregioesFile:
    mesorregioes = json.load(mesorregioesFile)
for msrg in mesorregioes:
    cursor.execute(
        "INSERT INTO tb_messoregiao (cod_municipio, nome, cod_microrregiao, cod_mesorregiao, cod_uf) VALUES (?, ?, ?, ?, ?)",
        (
            msrg['id'],
            msrg['nome'],
            msrg['microrregiao']['id'],
            msrg['microrregiao']['mesorregiao']['id'],
            msrg['microrregiao']['mesorregiao']['UF']['id']
        )
    )

conn.commit()
conn.close()
