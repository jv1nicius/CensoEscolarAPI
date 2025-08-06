import psycopg2
import json
import pandas as pd


DB_CONFIG = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': 5434
}

conn = psycopg2.connect(
    dbname=DB_CONFIG['dbname'],
    user=DB_CONFIG['user'],
    password=DB_CONFIG['password'],
    host=DB_CONFIG['host'],
    port=DB_CONFIG['port']
)
cursor = conn.cursor()

#Inicializar o schema
with open('schemas.sql', 'r') as f:
    schema = f.read()
    cursor.execute(schema)

#Inicializar a tb_uf
with open('./ufs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for row in data:
        cursor.execute(
            "INSERT INTO tb_uf (id, uf, nome, regiao) VALUES (%s, %s, %s, %s)",
            (row['id'], row['sigla'], row['nome'], row['regiao']['nome'])
        )
#Inicializar o tb_mesorregiao
with open('./mesorregioes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for row in data:
        cursor.execute(
            "INSERT INTO tb_mesorregiao (id, nome, idUf) VALUES (%s, %s, %s)",
            (row['id'], row['nome'], row['UF']['id'])
        )
#Inicializar o tb_microrregiao
with open('./microrregioes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for row in data:
        cursor.execute(
            """
            INSERT INTO tb_microrregiao (id, nome, idMes, idUf)
            VALUES (%s, %s, %s, %s)
            """,
            (
                row['id'],
                row['nome'],
                row['mesorregiao']['id'],
                row['mesorregiao']['UF']['id'],
            )
        )
#Inicializar o tb_municipio
with open('./municipios.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for row in data:
        cursor.execute(
            """
            INSERT INTO tb_municipio (id, nome, idMicro, idMes, idUf)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                row['id'],
                row['nome'],
                row['microrregiao']['id'],
                row['microrregiao']['mesorregiao']['id'],
                row['microrregiao']['mesorregiao']['UF']['id'],
            )
        )
conn.commit()

#Inicializar o microdados/2023 com pandas
chunksize = 10000
df_chunks = pd.read_csv('./microdados_ed_basica_2023.csv', chunksize=chunksize, encoding='ISO-8859-1', sep=';', low_memory=False)

colunas_escola = [
    'CO_ENTIDADE', 'NO_ENTIDADE', 'NU_ANO_CENSO', 'NO_REGIAO', 'CO_REGIAO', 'NO_UF', 'SG_UF', 'CO_UF',
    'NO_MUNICIPIO', 'CO_MUNICIPIO', 'NO_MESORREGIAO', 'CO_MESORREGIAO',
    'NO_MICRORREGIAO', 'CO_MICRORREGIAO', 'QT_MAT_BAS', 'QT_MAT_EJA', 'QT_MAT_ESP', 'QT_MAT_FUND',
    'QT_MAT_INF', 'QT_MAT_MED', 'QT_MAT_PROF'
]

for chunk in df_chunks:
    escola = chunk[colunas_escola]

    for _, row in escola.iterrows():
        cursor.execute(
            """
            INSERT INTO tb_instituicao (
                co_entidade, no_entidade, nu_ano_censo, no_regiao, co_regiao, no_uf, sg_uf, co_uf,
                no_municipio, co_municipio, no_mesorregiao, co_mesorregiao,
                no_microrregiao, co_microrregiao, qt_mat_bas, qt_mat_eja, qt_mat_esp,
                qt_mat_fund, qt_mat_inf, qt_mat_med, qt_mat_prof
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s
            )
            ON CONFLICT (co_entidade, nu_ano_censo) DO UPDATE SET
                no_entidade = EXCLUDED.no_entidade,
                no_regiao = EXCLUDED.no_regiao,
                co_regiao = EXCLUDED.co_regiao,
                no_uf = EXCLUDED.no_uf,
                sg_uf = EXCLUDED.sg_uf,
                co_uf = EXCLUDED.co_uf,
                no_municipio = EXCLUDED.no_municipio,
                co_municipio = EXCLUDED.co_municipio,
                no_mesorregiao = EXCLUDED.no_mesorregiao,
                co_mesorregiao = EXCLUDED.co_mesorregiao,
                no_microrregiao = EXCLUDED.no_microrregiao,
                co_microrregiao = EXCLUDED.co_microrregiao,
                qt_mat_bas = EXCLUDED.qt_mat_bas,
                qt_mat_eja = EXCLUDED.qt_mat_eja,
                qt_mat_esp = EXCLUDED.qt_mat_esp,
                qt_mat_fund = EXCLUDED.qt_mat_fund,
                qt_mat_inf = EXCLUDED.qt_mat_inf,
                qt_mat_med = EXCLUDED.qt_mat_med,
                qt_mat_prof = EXCLUDED.qt_mat_prof
            """,
            tuple(row.where(pd.notnull(row), None))
        )
    conn.commit()

#Inicializar o microdados/2024 utilizando o json.
#O arquivo csv possui modificações nos códigos de mesorregioes e microrregioes
with open('./microdados2024att.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

for row in dados:
    cursor.execute(
        """
        INSERT INTO tb_instituicao (
            co_entidade, no_entidade, nu_ano_censo, no_regiao, co_regiao, no_uf, sg_uf, co_uf,
            no_municipio, co_municipio, no_mesorregiao, co_mesorregiao,
            no_microrregiao, co_microrregiao, qt_mat_bas, qt_mat_eja, qt_mat_esp,
            qt_mat_fund, qt_mat_inf, qt_mat_med, qt_mat_prof
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s
        )
        ON CONFLICT (co_entidade, nu_ano_censo) DO UPDATE SET
            no_entidade = EXCLUDED.no_entidade,
            no_regiao = EXCLUDED.no_regiao,
            co_regiao = EXCLUDED.co_regiao,
            no_uf = EXCLUDED.no_uf,
            sg_uf = EXCLUDED.sg_uf,
            co_uf = EXCLUDED.co_uf,
            no_municipio = EXCLUDED.no_municipio,
            co_municipio = EXCLUDED.co_municipio,
            no_mesorregiao = EXCLUDED.no_mesorregiao,
            co_mesorregiao = EXCLUDED.co_mesorregiao,
            no_microrregiao = EXCLUDED.no_microrregiao,
            co_microrregiao = EXCLUDED.co_microrregiao,
            qt_mat_bas = EXCLUDED.qt_mat_bas,
            qt_mat_eja = EXCLUDED.qt_mat_eja,
            qt_mat_esp = EXCLUDED.qt_mat_esp,
            qt_mat_fund = EXCLUDED.qt_mat_fund,
            qt_mat_inf = EXCLUDED.qt_mat_inf,
            qt_mat_med = EXCLUDED.qt_mat_med,
            qt_mat_prof = EXCLUDED.qt_mat_prof
        """,(
            row['CO_ENTIDADE'], row['NO_ENTIDADE'], row['NU_ANO_CENSO'], row['NO_REGIAO'], row['CO_REGIAO'], row['NO_UF'], row['SG_UF'],
            row['CO_UF'], row['NO_MUNICIPIO'], row['CO_MUNICIPIO'], row['NO_MESORREGIAO'], row['CO_MESORREGIAO'], row['NO_MICRORREGIAO'],
            row['CO_MICRORREGIAO'], row['QT_MAT_BAS'], row['QT_MAT_EJA'], row['QT_MAT_ESP'], row['QT_MAT_FUND'], row['QT_MAT_INF'],
            row['QT_MAT_MED'], row['QT_MAT_PROF']
        )
    )
    
    conn.commit()


    #Inicializar o microdados/2024 com pandas. obs: deu errro por causa dos dados do de 2024
# chunksize = 10000
# df_chunks = pd.read_csv('./microdados_ed_basica_2024.csv', chunksize=chunksize, encoding='ISO-8859-1', sep=';', low_memory=False)

# colunas_escola = [
#     'CO_ENTIDADE', 'NO_ENTIDADE', 'NU_ANO_CENSO', 'NO_REGIAO', 'CO_REGIAO', 'NO_UF', 'SG_UF', 'CO_UF',
#     'NO_MUNICIPIO', 'CO_MUNICIPIO', 'NO_MESORREGIAO', 'CO_MESORREGIAO',
#     'NO_MICRORREGIAO', 'CO_MICRORREGIAO', 'QT_MAT_BAS', 'QT_MAT_EJA', 'QT_MAT_ESP', 'QT_MAT_FUND',
#     'QT_MAT_INF', 'QT_MAT_MED', 'QT_MAT_PROF'
# ]

# for chunk in df_chunks:
#     escola = chunk[colunas_escola]

#     for _, row in escola.iterrows():
#         cursor.execute(
#             """
#             INSERT INTO tb_instituicao (
#                 co_entidade, no_entidade, nu_ano_censo, no_regiao, co_regiao, no_uf, sg_uf, co_uf,
#                 no_municipio, co_municipio, no_mesorregiao, co_mesorregiao,
#                 no_microrregiao, co_microrregiao, qt_mat_bas, qt_mat_eja, qt_mat_esp,
#                 qt_mat_fund, qt_mat_inf, qt_mat_med, qt_mat_prof
#             ) VALUES (
#                 %s, %s, %s, %s, %s, %s, %s, %s,
#                 %s, %s, %s, %s,
#                 %s, %s, %s, %s, %s,
#                 %s, %s, %s, %s
#             )
#             ON CONFLICT (co_entidade, nu_ano_censo) DO UPDATE SET
#                 no_entidade = EXCLUDED.no_entidade,
#                 no_regiao = EXCLUDED.no_regiao,
#                 co_regiao = EXCLUDED.co_regiao,
#                 no_uf = EXCLUDED.no_uf,
#                 sg_uf = EXCLUDED.sg_uf,
#                 co_uf = EXCLUDED.co_uf,
#                 no_municipio = EXCLUDED.no_municipio,
#                 co_municipio = EXCLUDED.co_municipio,
#                 no_mesorregiao = EXCLUDED.no_mesorregiao,
#                 co_mesorregiao = EXCLUDED.co_mesorregiao,
#                 no_microrregiao = EXCLUDED.no_microrregiao,
#                 co_microrregiao = EXCLUDED.co_microrregiao,
#                 qt_mat_bas = EXCLUDED.qt_mat_bas,
#                 qt_mat_eja = EXCLUDED.qt_mat_eja,
#                 qt_mat_esp = EXCLUDED.qt_mat_esp,
#                 qt_mat_fund = EXCLUDED.qt_mat_fund,
#                 qt_mat_inf = EXCLUDED.qt_mat_inf,
#                 qt_mat_med = EXCLUDED.qt_mat_med,
#                 qt_mat_prof = EXCLUDED.qt_mat_prof
#             """,
#             tuple(row.where(pd.notnull(row), None))
#         )
#     conn.commit()


cursor.close()
conn.close()