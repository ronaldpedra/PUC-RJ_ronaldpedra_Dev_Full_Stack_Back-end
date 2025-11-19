""" Api DashInvest"""

from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from sqlalchemy.exc import IntegrityError

from flask_cors import CORS

from models import Session, Ativo
from schemas import *


info = Info(title='DashInvest', version='1.0.0')
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name='Documentação', description='Documentação da API DashInvest - Swagger')
adicionar_ativo_tag = Tag(name='Adicionar Ativo', \
                          description='Adiciona ao Banco de Dados um novo ativo')
ativos_tag = Tag(name='Listar Ativos', \
                 description='Listas os Ativos cadastrados no Banco de Dados')


# Rota home que direciona para a documentação da API DashInvest
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela exibe a documentação da API DashInvest."""
    return redirect('/openapi')


@app.post('/adicionar_ativo', tags=[adicionar_ativo_tag], \
          responses={'200': AtivoViewSchema, '409': ErrorSchema, \
                     '400': ErrorSchema})
def add_ativo(form: AtivoSchema):
    """Adiciona um Ativo à base de dados e retorna uma representação do Ativo"""
    ativo = Ativo(
        ticker=form.ticker,
        nome=form.nome,
        classe_b3=form.classe_b3
        )

    try:
        session = Session()
        session.add(ativo)
        session.commit()
        return apresentar_ativo(ativo), 200

    except IntegrityError:
        error_msg = 'Ativo com o mesmo Ticker já cadastrado'
        return {'message': error_msg}, 409

    except Exception:
        error_msg = 'Não foi possível salvar o Ativo.'
        return {'message': error_msg}


@app.get('/ativos', tags=[ativos_tag], \
         responses={'200': ListarAtivosSchema, '404': ErrorSchema})
def get_ativos():
    """Retorna todos os Ativos cadastrados no Banco de Dados"""
    session = Session()
    ativos = session.query(Ativo).all()

    if not ativos:
        return {'ativos': []}, 200

    print(ativos)
    return apresentar_ativos(ativos), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
