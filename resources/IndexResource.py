from flask_restful import Resource
from flask import jsonify

from helpers.logging import logger

class IndexResource(Resource):
    def get(self):
        versao = {"versao": "0.0.1"}
        logger.info("GET - Rota principal")
        return versao, 200