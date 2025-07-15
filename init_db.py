import sqlite3
import json

# 1 - Abrir a conexão
conn = sqlite3.connect('censoescolar.db')
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
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        item["NO_REGIAO"], item["CO_REGIAO"], item["NO_UF"], item["SG_UF"], item["CO_UF"], item["NO_MUNICIPIO"], item["CO_MUNICIPIO"], item["NO_MESORREGIAO"], item["CO_MESORREGIAO"], item["NO_MICRORREGIAO"], item["CO_MICRORREGIAO"], item["NO_ENTIDADE"], item["CO_ENTIDADE"], item["QT_MAT_BAS"], item["QT_MAT_EJA"], item["QT_MAT_ESP"], item["QT_MAT_FUND"], item["QT_MAT_INF"], item["QT_MAT_MED"], item["QT_MAT_PROF"]
    ))
    
with open("UFs.json", "r", encoding="utf-8") as ufs:
    dadosUf = json.load(ufs)
for uf in dadosUf:
    cursor.execute("""
        INSERT INTO tb_uf (id, uf, nome, regiao) VALUES (?, ?, ?, ?)
    """, (
        uf['id'], 
        uf['sigla'], 
        uf['nome'], 
        uf['regiao']['nome']
    ))

# Inserir dados na tabela tb_mesorregiao
with open("mesorregioes.json", "r", encoding="utf-8") as mesorregioesFile:
    mesorregioes = json.load(mesorregioesFile)
for msrg in mesorregioes:
    cursor.execute("""
        INSERT INTO tb_mesorregiao (id, nome, idUf) VALUES (?, ?, ?)
    """, (
        msrg['id'],
        msrg['nome'],
        msrg['UF']['id']
    ))

# Inserir dados na tabela tb_microrregiao
with open("microrregioes.json", "r", encoding="utf-8") as microrregioesFile:
    microrregioes = json.load(microrregioesFile)
for mcrrg in microrregioes:
    cursor.execute("""
        INSERT INTO tb_microrregiao (id, nome, idMes, idUf, regiao) VALUES (?, ?, ?, ?, ?)
    """, (
        mcrrg['id'], 
        mcrrg['nome'], 
        mcrrg['mesorregiao']['id'],
        mcrrg['mesorregiao']['UF']['id'], 
        mcrrg['mesorregiao']['UF']['regiao']['nome']
    ))

# Inserir dados na tabela tb_municipio
with open("municipios.json", "r", encoding="utf-8") as municipiosFile:
    municipios = json.load(municipiosFile)
for mncp in municipios:
    cursor.execute("""
        INSERT INTO tb_municipio (id, nome, idMes, idMicro, idUf, regiao) VALUES (?, ?, ?, ?, ?, ?)
    """, (
        mncp['id'], 
        mncp['nome'], 
        mncp['microrregiao']['mesorregiao']['id'], 
        mncp['microrregiao']['id'], 
        mncp['microrregiao']['mesorregiao']['UF']['id'],
        mncp['microrregiao']['mesorregiao']['UF']['regiao']['nome']
    ))

conn.commit()
conn.close()
