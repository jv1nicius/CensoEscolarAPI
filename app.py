from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

def carregarJson():
    with open('microdados2024.json', encoding='utf-8') as f:
        return json.load(f)

#constante que carrega os dados do json
DADOS = carregarJson()

#salvar os dados no json
def salvar():
    with open('microdados2024.json', 'w', encoding='utf-8') as f:
            json.dump(DADOS, f, ensure_ascii=False, indent=4)
            
#buscar item nos dados
def getItem(id):
    for item in DADOS:
        if item["CO_ENTIDADE"] == id:
            return item
    return None

class TodoSimple(Resource):
    def get(self, todo_id):
        item = getItem(todo_id)
        if (item):
            return {todo_id: item}
        
        return 'Não Encontrado', 404

    def put(self, todo_id):
        item = getItem(todo_id)
        if (item):
            itemAtualizado = request.get_json()
            item.update(itemAtualizado)
            salvar()
            return {todo_id: item}, 200
        
        return 'Não Encontrado', 404
    
    def delete(self, todo_id):
        item = getItem(todo_id)
        if (item):
            DADOS.remove(item)
            salvar()
            return '', 200
        
        return 'Não Encontrado', 404


class TodoList(Resource):
    def get(self):
        resposta = json.dumps(DADOS, ensure_ascii=False)
        return Response(resposta, mimetype='application/json')
    
    def post(self):
        novoItem = request.get_json()
        DADOS.insert(0, novoItem)
        salvar()
        return novoItem, 200

api.add_resource(TodoList, '/instituicoesensino')
api.add_resource(TodoSimple, '/instituicoesensino/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
