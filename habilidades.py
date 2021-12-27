from flask_restful import Resource
from flask import request
import json

lista_habilidades = ['Python', 'Java', 'NodeJS', 'JavaScript']

class Habilidades(Resource):
    #retorna as habilidades
    def get(self):
        return lista_habilidades

    #adiciona uma habilidade a lista
    def post(self):
        dados = json.loads(request.data)
        #validação de habilidade
        if dados in lista_habilidades:
            return {'erro':'habilidade já está na lista'}
        else:
            lista_habilidades.append(dados)
            return {'sucesso':'habilidade inserida na lista'}


class EditarHabilidade(Resource):
    def get(self, index):
        return lista_habilidades[index]

    def put(self, index):
        try:
            dados = json.loads(request.data)
            if dados in lista_habilidades:
                response = {'erro':'habilidade já está na lista'}
            else:
                lista_habilidades.pop(index)
                lista_habilidades.insert(index, dados)
                response = lista_habilidades
        except IndexError:
            response = {'mensagem de erro':'posicao nao existe'}
        return response

    def delete(self, index):
        lista_habilidades.pop(index)
        return {'mensagem':'habilidade excluida no sistema'}