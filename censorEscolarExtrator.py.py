import csv, json

escolas = list()

regiao = "Nordeste"
""" estados = ['PB','PE','RN'] """

with open('C:/Users/jose_/Downloads/microdados_censo_escolar_2024/microdados_censo_escolar_2024/dados/microdados_ed_basica_2024.csv', 'r') as arquivo:
    reader = csv.reader(arquivo, delimiter=';')
    cabecalho = next(reader)
    #Localização das colunas
    indexRegiaoNo = cabecalho.index('NO_REGIAO')
    indexRegiaoCo = cabecalho.index('CO_REGIAO')
    indexEstadoNo = cabecalho.index('NO_UF')
    indexEstadoSg = cabecalho.index('SG_UF')
    indexEstadoCo = cabecalho.index('CO_UF')
    indexMunicipioNo = cabecalho.index('NO_MUNICIPIO')
    indexMunicipioCo = cabecalho.index('CO_MUNICIPIO')
    indexMesorregiaoNo = cabecalho.index('NO_MESORREGIAO')
    indexMesorregiaoCo = cabecalho.index('CO_MESORREGIAO')
    indexMicrorregiaoNo = cabecalho.index('NO_MICRORREGIAO')
    indexMicrorregiaoCo = cabecalho.index('CO_MICRORREGIAO')
    indexEntidadeNo = cabecalho.index('NO_ENTIDADE')
    indexEntidadeCo = cabecalho.index('CO_ENTIDADE')
    
        #Local das quantidades de matrículas
    indexMatBas = cabecalho.index('QT_MAT_BAS')
    indexMatEja = cabecalho.index('QT_MAT_EJA')
    indexMatEsp = cabecalho.index('QT_MAT_ESP')
    indexMatFund = cabecalho.index('QT_MAT_FUND')
    indexMatInf = cabecalho.index('QT_MAT_INF')
    indexMatMed = cabecalho.index('QT_MAT_MED')
    indexMatProf = cabecalho.index('QT_MAT_PROF')
    
    for row in reader:
        if row[indexRegiaoNo] == regiao:
            escola = dict()
            escola['NO_REGIAO'] = row[indexRegiaoNo]
            escola['CO_REGIAO'] = row[indexRegiaoCo]
            escola['NO_UF'] = row[indexEstadoNo]
            escola['SG_UF'] = row[indexEstadoSg]
            escola['CO_UF'] = row[indexEstadoCo]
            escola['NO_MUNICIPIO'] = row[indexMunicipioNo]
            escola['CO_MUNICIPIO'] = row[indexMunicipioCo]
            escola['NO_MESORREGIAO'] = row[indexMesorregiaoNo]
            escola['CO_MESORREGIAO'] = row[indexMesorregiaoCo]
            escola['NO_MICRORREGIAO'] = row[indexMicrorregiaoNo]
            escola['CO_MICRORREGIAO'] = row[indexMicrorregiaoCo]
            escola['NO_ENTIDADE'] = row[indexEntidadeNo]
            escola['CO_ENTIDADE'] = row[indexEntidadeCo]
            
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

""" A lista de escolas possui 75054 itens """