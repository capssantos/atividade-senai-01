from flask import Flask, jsonify, request

from libs.api import *
from libs.banco import *

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def main():

    if request.method == 'GET':
        return 'Ola'

    payload = request.json
    cep = payload.get('cep').replace("-","")
    viacep = via_cep(cep=cep)
    inserir_tabela(cep=viacep.get('cep'),
                   logradouro=viacep.get('logradouro'),
                   complemento=viacep.get('complemento'),
                   unidade=viacep.get('unidade'),
                   bairro=viacep.get('bairro'),
                   localidade=viacep.get('localidade'),
                   uf=viacep.get('uf'),
                   estado=viacep.get('estado'),
                   regiao=viacep.get('regiao'),
                   ibge=viacep.get('ibge'),
                   gia=viacep.get('gia'),
                   ddd=viacep.get('ddd'),
                   siafi=viacep.get('siafi'))

    return jsonify({'cep':viacep.get('cep'),
                   'logradouro':viacep.get('logradouro'),
                   'complemento':viacep.get('complemento'),
                   'unidade':viacep.get('unidade'),
                   'bairro':viacep.get('bairro'),
                   'localidade':viacep.get('localidade'),
                   'uf':viacep.get('uf'),
                   'estado':viacep.get('estado'),
                   'regiao':viacep.get('regiao'),
                   'ibge':viacep.get('ibge'),
                   'gia':viacep.get('gia'),
                   'ddd':viacep.get('ddd'),
                   'siafi':viacep.get('siafi')})

app.run(debug=True, port=8000)