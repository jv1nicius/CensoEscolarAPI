import psycopg2
from flask_restful import Resource, reqparse
from flask import request
from marshmallow import ValidationError

from models.InstituicaoEnsino import InstituicaoEnsino, InstituicaoEnsinoSchema

from helpers.database import getConnection
from helpers.logging import logger

class InstituicoesResource(Resource):
    def get(self):
        logger.info("GET - instituições")
        
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)
        offset = (page - 1) * per_page

        try:
            cursor = getConnection().cursor()
            cursor.execute('SELECT * FROM tb_instituicao LIMIT %s OFFSET %s', (per_page, offset))
            result = cursor.fetchall()
            instituicoes = [InstituicaoEnsino(*row).toDict() for row in result]
            return instituicoes, 200
        
        except psycopg2.Error as e:
            logger.error(f"Erro ao consultar as intituições: {str(e)}")
            return {"mensagem": "Erro no banco", "erro": str(e)}, 500

    def post(self):
        logger.info("POST - instituições")
        
        schema = InstituicaoEnsinoSchema()
        data = request.get_json()

        try:
            validado = schema.load(data)
            campos = (
                'co_entidade', 'no_entidade', 'nu_ano_censo', 'no_regiao', 'co_regiao',
                'no_uf', 'sg_uf', 'co_uf', 'no_municipio', 'co_municipio',
                'no_mesorregiao', 'co_mesorregiao', 'no_microrregiao', 'co_microrregiao',
                'qt_mat_bas', 'qt_mat_eja', 'qt_mat_esp', 'qt_mat_fund',
                'qt_mat_inf', 'qt_mat_med', 'qt_mat_prof'
            )
            valores = [validado.get(campo) for campo in campos]

            cursor = getConnection().cursor()
            cursor.execute(f'''
                INSERT INTO tb_instituicao ({", ".join(campos)})
                VALUES ({", ".join(["%s"] * len(campos))})
                RETURNING co_entidade, nu_ano_censo
            ''', valores)

            co_entidade, nu_ano_censo = cursor.fetchone()
            getConnection().commit()

            return {"co_entidade": co_entidade, "nu_ano_censo": nu_ano_censo}, 201

        except ValidationError as e:
            logger.error(f"Erro na validação: {str(e)}")
            return {"mensagem": "Erro de validação", "erro": str(e)}, 400
        
        except psycopg2.Error as e:
            logger.error(f"Erro ao inserir instituição: {str(e)}")
            return {"mensagem": "Erro ao inserir", "erro": str(e)}, 500

"""
@app.get("/instituicoes")
def listar_instituicoes():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page

    try:
        cursor = getConnection().cursor()
        cursor.execute('''
            SELECT * FROM tb_instituicao
            LIMIT %s OFFSET %s
        ''', (per_page, offset))
        result = cursor.fetchall()

        instituicoes = [InstituicaoEnsino(*row).toDict() for row in result]
        return jsonify(instituicoes), 200

    except psycopg2.Error as e:
        return jsonify({"mensagem": "Problema com o banco de dados.", "erro": str(e)}), 500
        
@app.post("/instituicoes")
def criar_instituicao():
    schema = InstituicaoEnsinoSchema()
    data = request.get_json()
    
    try:
        validado = schema.load(data)

        campos = (
            'co_entidade', 'no_entidade', 'nu_ano_censo', 'no_regiao', 'co_regiao',
            'no_uf', 'sg_uf', 'co_uf', 'no_municipio', 'co_municipio',
            'no_mesorregiao', 'co_mesorregiao', 'no_microrregiao', 'co_microrregiao',
            'qt_mat_bas', 'qt_mat_eja', 'qt_mat_esp', 'qt_mat_fund',
            'qt_mat_inf', 'qt_mat_med', 'qt_mat_prof'
        )

        valores = [validado.get(campo) for campo in campos]

        cursor = getConnection().cursor()
        cursor.execute(f'''
            INSERT INTO tb_instituicao ({", ".join(campos)})
            VALUES ({", ".join(["%s"] * len(campos))})
            RETURNING co_entidade, nu_ano_censo
        ''', valores)

        co_entidade, nu_ano_censo = cursor.fetchone()
        getConnection().commit()

        return jsonify({"co_entidade": co_entidade, "nu_ano_censo": nu_ano_censo}), 201

    except ValidationError as e:
        return jsonify({"mensagem": f"Erro de validação: {str(e)}"}), 400
    except psycopg2.Error as e:
        return jsonify({"mensagem": "Erro ao inserir instituição", "erro": str(e)}), 500
"""