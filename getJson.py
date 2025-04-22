import csv, json

escolas = list()

estados = ['PB','PE','RN']

with open('C:/Users/jose_/Downloads/microdados_censo_escolar_2024/microdados_censo_escolar_2024/dados/microdados_ed_basica_2024.csv', 'r') as arquivo:
    reader = csv.reader(arquivo, delimiter=';')
    cabecalho = next(reader)
    #Localização das colunas
    indexEstado = cabecalho.index('SG_UF')
    indexRegiao = cabecalho.index('NO_REGIAO')
    indexMunicipio = cabecalho.index('NO_MUNICIPIO')
    indexMesorregiao = cabecalho.index('NO_MESORREGIAO')
    indexMicrorregiao = cabecalho.index('NO_MICRORREGIAO')
    indexEntidade = cabecalho.index('NO_ENTIDADE')
    indexCOEntidade = cabecalho.index('CO_ENTIDADE')
    
        #Local das quantidades de matrículas
    indexMatBas = cabecalho.index('QT_MAT_BAS')
    indexMatEja = cabecalho.index('QT_MAT_EJA')
    indexMatEsp = cabecalho.index('QT_MAT_ESP')
    indexMatFund = cabecalho.index('QT_MAT_FUND')
    indexMatInf = cabecalho.index('QT_MAT_INF')
    indexMatMed = cabecalho.index('QT_MAT_MED')
    indexMatProf = cabecalho.index('QT_MAT_PROF')
    
    for row in reader:
        if row[indexEstado] in estados:
            escola = dict()
            escola['CO_ENTIDADE'] = row[indexCOEntidade]
            escola['SG_UF'] = row[indexEstado]
            escola['NO_REGIAO'] = row[indexRegiao]
            escola['NO_MUNICIPIO'] = row[indexMunicipio]
            escola['NO_MESORREGIAO'] = row[indexMesorregiao]
            escola['NO_MICRORREGIAO'] = row[indexMicrorregiao]
            escola['NO_ENTIDADE'] = row[indexEntidade]
            escola['QT_MAT_BAS'] = row[indexMatBas]
            escola['QT_MAT_EJA'] = row[indexMatEja]
            escola['QT_MAT_ESP'] = row[indexMatEsp]
            escola['QT_MAT_FUND'] = row[indexMatFund]
            escola['QT_MAT_INF'] = row[indexMatInf]
            escola['QT_MAT_MED'] = row[indexMatMed]
            escola['QT_MAT_PROF'] = row[indexMatProf]
            
            escolas.append(escola)
    
with open('microdados2024.json', 'w', encoding='utf-8') as dadosJson:
    json.dump(escolas, dadosJson, indent="\t", ensure_ascii=False)