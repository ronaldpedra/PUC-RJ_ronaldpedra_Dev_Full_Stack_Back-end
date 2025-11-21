""" Api DashInvest"""

from flask_openapi3.openapi import OpenAPI
from flask_openapi3.models.info import Info
from flask_openapi3.models.tag import Tag
from flask import redirect
from flask_cors import CORS

from routes.ativo import api as ativo_api

# Informações da API
info = Info(title='DashInvest', version='1.0.0')
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo a tag da documentação
home_tag = Tag(name='Documentação',
               description='Documentação da API DashInvest - Swagger')

# Registra o blueprint de Ativos na aplicação principal
app.register_api(ativo_api)


# Rota home que direciona para a documentação da API DashInvest
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela exibe a documentação da API DashInvest."""
    return redirect('/openapi')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
