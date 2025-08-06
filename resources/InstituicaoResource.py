import psycopg2
from flask_restful import Resource
from flask import request

from models.InstituicaoEnsino import InstituicaoEnsino, InstituicaoEnsinoSchema

from helpers.database import getConnection
from helpers.logging import logger

class InstituicaoResource(Resource):
    def get(self, co_entidade, nu_ano_censo):
        logger.info(f"GET - instituicoes/{co_entidade}/{nu_ano_censo}")
        
        try:
            cursor = getConnection().cursor()
            cursor.execute('''
                SELECT *
                FROM tb_instituicao
                WHERE co_entidade = %s AND nu_ano_censo = %s
            ''', (co_entidade, nu_ano_censo))
            row = cursor.fetchone()

            if row is None:
                logger.warning(f"Não encontrada a instituição: {co_entidade}, ano: {nu_ano_censo}")
                return {"mensagem": "Instituição não encontrada"}, 404

            return InstituicaoEnsino(*row).toDict(), 200

        except psycopg2.Error as e:
            logger.error(f"Erro ao acessar instituição: {str(e)}")
            return {"mensagem": "Erro ao acessar o banco"}, 500

    def put(self, co_entidade, nu_ano_censo):
        logger.info(f"PUT - instituicoes/{co_entidade}/{nu_ano_censo}")
        
        schema = InstituicaoEnsinoSchema()
        data = request.get_json()
        
        try:
            validado = schema.load(data)
            conn = getConnection()
            cursor = conn.cursor()

            cursor.execute('''
                SELECT 1 FROM tb_instituicao
                WHERE co_entidade = %s AND nu_ano_censo = %s
            ''', (co_entidade, nu_ano_censo))
            
            if cursor.fetchone() is None:
                return {"mensagem": "Instituição não encontrada"}, 404

            campos = (
                'co_entidade', 'no_entidade', 'nu_ano_censo', 'no_regiao', 'co_regiao',
                'no_uf', 'sg_uf', 'co_uf', 'no_municipio', 'co_municipio',
                'no_mesorregiao', 'co_mesorregiao', 'no_microrregiao', 'co_microrregiao',
                'qt_mat_bas', 'qt_mat_eja', 'qt_mat_esp', 'qt_mat_fund',
                'qt_mat_inf', 'qt_mat_med', 'qt_mat_prof'
            )

            valores = [validado[c] for c in campos]

            update_fields = ', '.join([f"{campo} = %s" for campo in campos])

            cursor.execute(f'''
                UPDATE tb_instituicao
                SET {update_fields}
                WHERE co_entidade = %s AND nu_ano_censo = %s
            ''', valores + [co_entidade, nu_ano_censo])
            conn.commit()

            cursor.execute(f'''
                SELECT {", ".join(campos)}
                FROM tb_instituicao
                WHERE co_entidade = %s AND nu_ano_censo = %s
            ''', (co_entidade, nu_ano_censo))
            row = cursor.fetchone()

            return InstituicaoEnsino(*row).toDict(), 200

        except Exception as e:
            logger.error(f"Erro ao atualizar instituição: {str(e)}")
            return {"mensagem": f"Erro ao atualizar: {str(e)}"}, 500

    def delete(self, co_entidade, nu_ano_censo):
        logger.info("DELETE - instituição")
        
        try:
            conn = getConnection()
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM tb_instituicao
                WHERE co_entidade = %s AND nu_ano_censo = %s
            ''', (co_entidade, nu_ano_censo))
            conn.commit()
            logger.info(f"DELETE - instituicoes/{co_entidade}/{nu_ano_censo} 'removido'")

            if cursor.rowcount == 0:
                return {"mensagem": "Instituição não encontrada"}, 404

            return '', 204
        except psycopg2.Error as e:
            logger.error(f"Erro ao deletar instituição: {str(e)}")
            return {"mensagem": "Problema com o banco de dados"}, 500

"""
@app.get("/instituicoes/<int:id>")
def instituicao_por_id(id):
    try:
        cursor = getConnection().cursor()
        cursor.execute('SELECT * FROM tb_instituicao WHERE co_entidade = %s', (id,))
        row = cursor.fetchone()

        if row is None:
            return jsonify({"mensagem": "Instituição não encontrada."}), 404

        return jsonify(InstituicaoEnsino(*row).toDict()), 200

    except psycopg2.Error:
        return jsonify({"mensagem": "Problema com o banco de dados."}), 500


@app.put("/instituicoes/<int:id>")
def atualizar_instituicao(id):
    schema = InstituicaoEnsinoSchema()
    data = request.get_json()

    try:
        validado = schema.load(data)
        cursor = getConnection().cursor()
        cursor.execute('SELECT * FROM tb_instituicao WHERE id = %s', (id,))
        if cursor.fetchone() is None:
            return jsonify({"mensagem": "Instituição não encontrada"}), 404

        update_fields = '''
            no_entidade = %s, co_entidade = %s, qt_mat_bas = %s, qt_mat_eja = %s,
            qt_mat_esp = %s, qt_mat_fund = %s, qt_mat_inf = %s, qt_mat_med = %s,
            qt_mat_prof = %s, no_regiao = %s, co_regiao = %s, no_uf = %s, sg_uf = %s,
            co_uf = %s, no_municipio = %s, co_municipio = %s, no_mesorregiao = %s,
            co_mesorregiao = %s, no_microrregiao = %s, co_microrregiao = %s
        '''

        valores = [
            validado['no_entidade'], validado['co_entidade'], validado['qt_mat_bas'],
            validado['qt_mat_eja'], validado['qt_mat_esp'], validado['qt_mat_fund'],
            validado['qt_mat_inf'], validado['qt_mat_med'], validado['qt_mat_prof'],
            validado['no_regiao'], validado['co_regiao'], validado['no_uf'],
            validado['sg_uf'], validado['co_uf'], validado['no_municipio'],
            validado['co_municipio'], validado['no_mesorregiao'],
            validado['co_mesorregiao'], validado['no_microrregiao'],
            validado['co_microrregiao'], id
        ]

        cursor.execute(f'''
            UPDATE tb_instituicao SET {update_fields} WHERE id = %s
        ''', valores)
        getConnection().commit()

        return jsonify(InstituicaoEnsino(id, **validado).toDict()), 200

    except Exception as e:
        return jsonify({"mensagem": f"Erro ao atualizar: {str(e)}"}), 500


@app.delete("/instituicoes/<int:id>")
def remover_instituicao(id):
    try:
        cursor = getConnection().cursor()
        cursor.execute('DELETE FROM tb_instituicao WHERE id = %s', (id,))
        getConnection().commit()
        if cursor.rowcount == 0:
            return jsonify({"mensagem": "Instituição não encontrada"}), 404
        return '', 204

    except psycopg2.Error:
        return jsonify({"mensagem": "Problema com o banco de dados."}), 500
"""