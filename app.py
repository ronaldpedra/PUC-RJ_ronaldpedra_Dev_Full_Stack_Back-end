""" Api DashInvest"""

from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from flask_cors import CORS

from models import *


info = Info(title='DashInvest', version='1.0.0')
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name='Documentação', description='Documentação da API DashInvest - Swagger')
adicionar_ativo_tag = Tag(name='Adicionar Ativo', description='Adiciona ao banco de dados um novo ativo')


# Rota home que direciona para a documentação da API DashInvest
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela exibe a documentação da API DashInvest."""
    return redirect('/openapi')


# @app.post('/adicionar_ativo', tags=[adicionar_ativo_tag], responses={'200': AtivoViewSchema, '409': ErrorSchema, '400': ErrorSchema})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
