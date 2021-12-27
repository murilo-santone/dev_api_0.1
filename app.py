from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [{
    'id':0,
    'nome':'Murilo',
    'habilidades':['Python','Flask']
},{
    'id':1,
    'nome':'Rafael',
    'habilidades':['Python','Django']
}]


#Devolve o desenvolvedor pelo ID, também altera ou deleta.
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    #Metodo GET retorna um dado
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'erro', 'mensagem':f'desenvolvedor de id {id} não existe'}
        except Exception:
            mensagem = 'Erro desconhecido, procure um administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return jsonify(response)
    #Metodo PUT faz uma alteração
    elif request.method == 'PUT':
        #import json > .loads pega os dados do metodo PUT enviado para fazer uma alteração.
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({"Status":"Sucesso", "Mensagem":"Resgistro excluido"})


#Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_dev():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)



if __name__ == '__main__':
    app.run(debug=True)