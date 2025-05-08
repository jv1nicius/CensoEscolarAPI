import sqlite3
import json

# 1 - Abri a conexão
conn = sqlite3.connect('censoescolar.db')
cursor = conn.cursor()

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


conn.commit()
conn.close()
