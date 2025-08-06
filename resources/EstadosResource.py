import psycopg2
from flask_restful import Resource

from helpers.database import getConnection
from helpers.logging import logger

class EstadosResource(Resource):
    def get(self):
        logger.info("GET - Estados")

        try:
            cursor = getConnection().cursor()
            cursor.execute('SELECT id, nome, uf FROM tb_uf')
            result = cursor.fetchall()
            estados = [{"idUf": r[0], "nomeUf": r[1], "siglaUf": r[2]} for r in result]
            return estados, 200

        except psycopg2.Error as e:
            logger.error(f"Erro ao consultar estados: {str(e)}")
            return {"mensagem": "Problema com o banco de dados.", "erro": str(e)}, 500
"""
@app.get("/estados")
def listar_estados():
    try:
        cursor = getConnection().cursor()
        cursor.execute('SELECT id, nome, uf FROM tb_uf')
        result = cursor.fetchall()
        estados = [{"id_uf": r[0], "nome_uf": r[1], "sigla_uf": r[2]} for r in result]
        return jsonify(estados), 200

    except psycopg2.Error as e:
        return jsonify({"mensagem": "Problema com o banco de dados.", "erro": str(e)}), 500
"""