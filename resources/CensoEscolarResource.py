import psycopg2
from flask_restful import Resource
from flask import request

from helpers.database import getConnection
from helpers.logging import logger

class CensoEscolarResource(Resource):
    def get(self):
        #Coloquei o logger depois da consulta
        ano_censo = request.args.get('nu_ano_censo', default=2024, type=int)
        co_uf = request.args.get('co_uf', default=None, type=int)
        
        try:
            conn = getConnection()
            cursor = conn.cursor()
            sql = '''
                SELECT co_uf,
                    SUM(COALESCE( qt_mat_bas )) AS bas, 
	                SUM(COALESCE( qt_mat_eja )) AS eja, 
                    SUM(COALESCE( qt_mat_esp )) AS esp, 
                    SUM(COALESCE( qt_mat_fund )) AS fund, 
                    SUM(COALESCE( qt_mat_inf )) AS inf, 
                    SUM(COALESCE( qt_mat_med )) AS med, 
                    SUM(COALESCE( qt_mat_prof )) AS prof,
                    SUM(COALESCE(qt_mat_bas, 0) + COALESCE(qt_mat_prof, 0) +
                        COALESCE(qt_mat_inf, 0) + COALESCE(qt_mat_fund, 0) +
                        COALESCE(qt_mat_esp, 0)) AS total_matriculas
                FROM tb_instituicao
                WHERE nu_ano_censo = %s
            '''
            params = [ano_censo]
            if co_uf:
                sql += ' AND co_uf = %s'
                params.append(co_uf)
                logger.info(f"GET - Censo escolar por ano e estado: {ano_censo} , {co_uf}")
            else:
                logger.info(f"GET - Censo escolar por ano: {ano_censo}")
            sql += ' GROUP BY co_uf'
            cursor.execute(sql, params)
            result = cursor.fetchall()
            cursor.close()
            
            
            return {str(row[0]): {"bas": row[1], "eja": row[2], "esp": row[3], "fund": row[4], "inf": row[5], "med": row[6], "prof": row[7], "total":row[8]} for row in result}, 200


        except psycopg2.Error as e:
            logger.error(f"Erro ao consultar o Censo Escolar: {str(e)}")
            return {"mensagem": "Problema com o banco de dados.", "erro": str(e)}, 500
"""
@app.get("/censoescolar")
def matriculas_total():
    ano_censo = request.args.get('nu_ano_censo', default=2024, type=int)
    co_uf = request.args.get('co_uf', default=None, type=int)

    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql = '''
            SELECT co_uf,
                SUM(COALESCE(qt_mat_bas, 0) + COALESCE(qt_mat_prof, 0) +
                    COALESCE(qt_mat_inf, 0) + COALESCE(qt_mat_fund, 0) +
                    COALESCE(qt_mat_esp, 0)) AS total_matriculas
            FROM tb_instituicao
            WHERE nu_ano_censo = %s
        '''
        params = [ano_censo]
        if co_uf:
            sql += ' AND co_uf = %s'
            params.append(co_uf)

        sql += ' GROUP BY co_uf'
        cursor.execute(sql, params)
        result = cursor.fetchall()
        cursor.close()
        
        return jsonify({str(row[0]): row[1] for row in result}), 200

    except psycopg2.Error as e:
        return jsonify({"mensagem": "Problema com o banco de dados.", "erro": str(e)}), 500
"""