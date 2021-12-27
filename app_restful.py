from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades, EditarHabilidade

# app recebe flask
app = Flask(__name__)
# api recebe app
api = Api(app)

desenvolvedores = [{
    'id': 0,
    'nome': 'Murilo',
    'habilidades': ['Python', 'Flask']
}, {
    'id': 1,
    'nome': 'Rafael',
    'habilidades': ['Python', 'Django']
}]

# No restful vc tem uma classe recebendo o parametro Resource
class Desenvolvedor(Resource):
    # dentro da classe teremos os métodos
    def get(self, id):
        # não precisa retornar jsonify, automaticamente entende que está utilizando este formato
        # e retorna conforme o mesmo.
        # return {'nome': 'murilo'}
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'erro', 'mensagem':f'desenvolvedor de id {id} não existe'}
        except Exception:
            mensagem = 'Erro desconhecido, procure um administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {"Status": "Sucesso", "Mensagem": "Resgistro excluido"}

#Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

# Rota
api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev')
api.add_resource(Habilidades, '/habilidades')
api.add_resource(EditarHabilidade, '/habilidades/<int:index>')

if __name__ == '__main__':
    app.run(debug=True)
