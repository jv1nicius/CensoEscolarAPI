from flask import Flask, request, jsonify, g
import sqlite3
from marshmallow import ValidationError

from models.InstituicaoEnsino import InstituicaoEnsino, InstituicaoEnsinoSchema

DATABASE = 'censoescolar.db'

app = Flask(__name__)


def getConnection():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def closeConnection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    versao = {"versao": "0.0.1"}
    return jsonify(versao), 200


@app.get("/instituicoes")
def instituicoesResource():
    print("Get - Instituições")

    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    
    try:
        instituicoesEnsino = []

        cursor = getConnection().cursor()
        
        offset = (page - 1) * per_page
        
        cursor.execute(
            'SELECT * FROM tb_instituicao LIMIT ? OFFSET ?', (per_page, offset))
        resultSet = cursor.fetchall()

        for row in resultSet:
            # Montar o conjunto de instituições.
            id = row[0]
            no_entidade = row[1]
            co_entidade = row[2]
            qt_mat_bas = row[3]
            qt_mat_eja = row[4]
            qt_mat_esp = row[5]
            qt_mat_fund = row[6]
            qt_mat_inf = row[7]
            qt_mat_med = row[8]
            qt_mat_prof = row[9]
            no_regiao = row[10]
            co_regiao = row[11]
            no_uf = row[12]
            sg_uf = row[13]
            co_uf = row[14]
            no_municipio = row[15]
            co_municipio = row[16]
            no_mesorregiao = row[17]
            co_mesorregiao = row[18]
            no_microrregiao = row[19]
            co_microrregiao = row[20]

            instituicaoEnsino = InstituicaoEnsino(
                id, no_entidade, co_entidade, qt_mat_bas, qt_mat_eja, qt_mat_esp, qt_mat_fund, qt_mat_inf, qt_mat_med, qt_mat_prof, no_regiao, co_regiao, no_uf, sg_uf, co_uf, no_municipio, co_municipio, no_mesorregiao, co_mesorregiao, no_microrregiao, co_microrregiao
            )
            instituicoesEnsino.append(instituicaoEnsino.toDict())

    except sqlite3.Error as e:
        return jsonify({"mensagem": "Problema com o banco de dados."}), 500

    return jsonify(instituicoesEnsino), 200


@app.post("/instituicoes")
def instituicaoInsercaoResource():
    print("Post - Instituição")
    instituicaoEnsinoSchema = InstituicaoEnsinoSchema()

    instituicaoData = request.get_json()
    try:
        instituicaoJson = instituicaoEnsinoSchema.load(instituicaoData)

        no_entidade = instituicaoJson['no_entidade']
        co_entidade = instituicaoJson['co_entidade']
        qt_mat_bas = instituicaoJson['qt_mat_bas']
        qt_mat_eja = instituicaoJson['qt_mat_eja']
        qt_mat_esp = instituicaoJson['qt_mat_esp']
        qt_mat_fund = instituicaoJson['qt_mat_fund']
        qt_mat_inf = instituicaoJson['qt_mat_inf']
        qt_mat_med = instituicaoJson['qt_mat_med']
        qt_mat_prof = instituicaoJson['qt_mat_prof']
        no_regiao = instituicaoJson['no_regiao']
        co_regiao = instituicaoJson['co_regiao']
        no_uf = instituicaoJson['no_uf']
        sg_uf = instituicaoJson['sg_uf']
        co_uf = instituicaoJson['co_uf']
        no_municipio = instituicaoJson['no_municipio']
        co_municipio = instituicaoJson['co_municipio']
        no_mesorregiao = instituicaoJson['no_mesorregiao']
        co_mesorregiao = instituicaoJson['co_mesorregiao']
        no_microrregiao = instituicaoJson['no_microrregiao']
        co_microrregiao = instituicaoJson['co_microrregiao']


        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO tb_instituicao (
            no_entidade, co_entidade, qt_mat_bas, qt_mat_eja, qt_mat_esp, qt_mat_fund, qt_mat_inf,qt_mat_med, qt_mat_prof, no_regiao, co_regiao, no_uf, sg_uf, co_uf, no_municipio, co_municipio, no_mesorregiao, co_mesorregiao, no_microrregiao, co_microrregiao
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
        no_entidade, co_entidade, qt_mat_bas, qt_mat_eja, qt_mat_esp, qt_mat_fund, qt_mat_inf, qt_mat_med, qt_mat_prof, no_regiao, co_regiao, no_uf, sg_uf, co_uf, no_municipio, co_municipio, no_mesorregiao, co_mesorregiao, no_microrregiao, co_microrregiao
        ))
        conn.commit()


        id = cursor.lastrowid

        instituicaoEnsino = InstituicaoEnsino(
                id, no_entidade, co_entidade, qt_mat_bas, qt_mat_eja, qt_mat_esp, qt_mat_fund, qt_mat_inf, qt_mat_med, qt_mat_prof, no_regiao, co_regiao, no_uf, sg_uf, co_uf, no_municipio, co_municipio, no_mesorregiao, co_mesorregiao, no_microrregiao, co_microrregiao
            )
        return jsonify(instituicaoEnsino.toDict()), 200
    
    except ValidationError as err:
        return jsonify(err.messages), 400
    except sqlite3.Error as e:
        return jsonify({"mensagem": "Problema com o banco de dados."}), 500
    return jsonify({"mensagem": "Não cadastrado"}), 406


@app.route("/instituicoes/<int:id>", methods=["DELETE"])
def instituicaoRemocaoResource(id):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(
            'DELETE FROM tb_instituicao WHERE id = ?;', (id, ))
        conn.commit()
    except sqlite3.Error as e:
        return jsonify({"mensagem": "Problema com o banco de dados. Não encontrado"}), 500
    return f"Entidade {id} removido!", 200


@app.route("/instituicoes/<int:id>", methods=["PUT"])
def instituicaoAtualizacaoResource(id):
    print("Put - Instituição")
    instituicaoEnsinoSchema = InstituicaoEnsinoSchema()

    instituicaoData = request.get_json()
    
    try:
        instituicaoJson = instituicaoEnsinoSchema.load(instituicaoData)
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM tb_instituicao WHERE id = ?''', (id,))
        row = cursor.fetchone()
        if row is None:
            return jsonify({"mensagem": "Instituição não encontrada"}), 404
        cursor.execute('''UPDATE tb_instituicao SET
            no_entidade = ?,
            co_entidade = ?,
            qt_mat_bas = ?,
            qt_mat_eja = ?,
            qt_mat_esp = ?,
            qt_mat_fund = ?,
            qt_mat_inf = ?,
            qt_mat_med = ?,
            qt_mat_prof = ?,
            no_regiao = ?,
            co_regiao = ?,
            no_uf = ?,
            sg_uf = ?,
            co_uf = ?,
            no_municipio = ?,co_municipio = ?,
            no_mesorregiao = ?,
            co_mesorregiao = ?,
            no_microrregiao = ?,
            co_microrregiao = ?
            WHERE id = ?
        ''', (
            instituicaoJson['no_entidade'],
            instituicaoJson['co_entidade'],
            instituicaoJson['qt_mat_bas'],
            instituicaoJson['qt_mat_eja'],
            instituicaoJson['qt_mat_esp'],
            instituicaoJson['qt_mat_fund'],
            instituicaoJson['qt_mat_inf'],
            instituicaoJson['qt_mat_med'],
            instituicaoJson['qt_mat_prof'],
            instituicaoJson['no_regiao'],
            instituicaoJson['co_regiao'],
            instituicaoJson['no_uf'],
            instituicaoJson['sg_uf'],
            instituicaoJson['co_uf'],
            instituicaoJson['no_municipio'],
            instituicaoJson['co_municipio'],
            instituicaoJson['no_mesorregiao'],
            instituicaoJson['co_mesorregiao'],
            instituicaoJson['no_microrregiao'],
            instituicaoJson['co_microrregiao'],
            id
        ))
        conn.commit()
        instituicaoAtualizada = InstituicaoEnsino(
            id,
            instituicaoJson['no_entidade'],
            instituicaoJson['co_entidade'],
            instituicaoJson['qt_mat_bas'],
            instituicaoJson['qt_mat_eja'],
            instituicaoJson['qt_mat_esp'],
            instituicaoJson['qt_mat_fund'],
            instituicaoJson['qt_mat_inf'],
            instituicaoJson['qt_mat_med'],
            instituicaoJson['qt_mat_prof'],
            instituicaoJson['no_regiao'],
            instituicaoJson['co_regiao'],
            instituicaoJson['no_uf'],
            instituicaoJson['sg_uf'],
            instituicaoJson['co_uf'],
            instituicaoJson['no_municipio'],
            instituicaoJson['co_municipio'],
            instituicaoJson['no_mesorregiao'],
            instituicaoJson['co_mesorregiao'],
            instituicaoJson['no_microrregiao'],
            instituicaoJson['co_microrregiao']
        )
        return jsonify(instituicaoAtualizada.toDict()), 200
    except Exception as e:
            return jsonify({"mensagem": f"Erro ao atualizar: {str(e)}"}), 500
    finally:
        conn.close()

@app.route("/instituicoes/<int:id>", methods=["GET"])
def instituicoesByIdResource(id):
    try:
        cursor = getConnection().cursor()
        cursor.execute(
            'SELECT * FROM tb_instituicao WHERE id = ?', (id, ))
        row = cursor.fetchone()

        # Montar a de instituição.
        id = row[0]
        no_entidade = row[1]
        co_entidade = row[2]
        qt_mat_bas = row[3]
        qt_mat_eja = row[4]
        qt_mat_esp = row[5]
        qt_mat_fund = row[6]
        qt_mat_inf = row[7]
        qt_mat_med = row[8]
        qt_mat_prof = row[9]
        no_regiao = row[10]
        co_regiao = row[11]
        no_uf = row[12]
        sg_uf = row[13]
        co_uf = row[14]
        no_municipio = row[15]
        co_municipio = row[16]
        no_mesorregiao = row[17]
        co_mesorregiao = row[18]
        no_microrregiao = row[19]
        co_microrregiao = row[20]

        instituicaoEnsino = InstituicaoEnsino(
                id, no_entidade, co_entidade, qt_mat_bas, qt_mat_eja, qt_mat_esp, qt_mat_fund, qt_mat_inf, qt_mat_med, qt_mat_prof, no_regiao, co_regiao, no_uf, sg_uf, co_uf, no_municipio, co_municipio, no_mesorregiao, co_mesorregiao, no_microrregiao, co_microrregiao
            )

    except sqlite3.Error as e:
        return jsonify({"mensagem": "Problema com o banco de dados."}), 500


    return jsonify(instituicaoEnsino.toDict()), 200

if __name__ == "__main__":
    app.run(debug=True)