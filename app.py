""" Api DashInvest"""

from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from flask_cors import CORS

from models import Session, Ativo
import schemas


info = Info(title='DashInvest', version='1.0.0')
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name='Documentação', description='Documentação da API DashInvest - Swagger')
adicionar_ativo_tag = Tag(name='Adicionar Ativo', \
                          description='Adiciona ao Banco de Dados um novo ativo')
ativos_tag = Tag(name='Listar Ativos', \
                 description='Listas os Ativos cadastrados no Banco de Dados')
ativo_update_tag = Tag(name='Atualizar Ativo', \
                        description='Atualiza um Ativo existente no Banco de Dados')
ativo_delete_tag = Tag(name='Excluir Ativo', \
                       description='Exclui um Ativo do Banco de Dados')


# Rota home que direciona para a documentação da API DashInvest
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela exibe a documentação da API DashInvest."""
    return redirect('/openapi')


# Métodos para manipular ATIVOS
@app.post('/ativos', tags=[adicionar_ativo_tag], \
          responses={'200': schemas.AtivoViewSchema, '409': schemas.ErrorSchema, \
                     '400': schemas.ErrorSchema})
def add_ativo(form: schemas.AtivoSchema):
    """Adiciona um Ativo à base de dados e retorna uma representação do Ativo"""
    ativo = Ativo(
        ticker=form.ticker,
        short_name=form.short_name,
        long_name=form.long_name,
        classe_b3=form.classe_b3 # Pydantic já converteu a string para o Enum
        )
    try:
        session = Session()
        session.add(ativo)
        session.commit()
        return schemas.apresentar_ativo(ativo), 200

    except IntegrityError:
        error_msg = 'Ativo com o mesmo Ticker já cadastrado'
        return {'message': error_msg}, 409

    except SQLAlchemyError as e:
        error_msg = 'Não foi possível salvar o Ativo.'
        # Imprime o erro original no console para depuração
        print(e)
        return {'message': error_msg}, 500


@app.get('/ativos', tags=[ativos_tag], \
         responses={'200': schemas.ListarAtivosSchema, '404': schemas.ErrorSchema})
def get_ativos():
    """Retorna todos os Ativos cadastrados no Banco de Dados"""
    session = Session()
    ativos = session.query(Ativo).all()

    if not ativos:
        return {'ativos': []}, 200

    return schemas.apresentar_ativos(ativos), 200


@app.patch('/ativos', tags=[ativo_update_tag], \
           responses={'200': schemas.AtivoViewSchema, '404': schemas.ErrorSchema, '409': schemas.ErrorSchema, \
                      '400': schemas.ErrorSchema})
def update_ativo(query: schemas.AtivoBuscaSchema, form: schemas.AtivoUpdateSchema):
    """Atualiza um Ativo existente no Banco de Dados.

    Retorna uma representação atualizada do ativo.
    """
    ticker = unquote(unquote(query.ticker))
    session = Session()
    ativo = session.query(Ativo).filter(Ativo.ticker == ticker).first()

    if not ativo:
        error_msg = 'Ativo não encontrado na base de dados'
        return {'message': error_msg}, 404

    # Pega os dados do formulário que não são nulos
    update_data = form.model_dump(exclude_unset=True)

    # Verifica se algum dado foi enviado para atualização
    if not update_data:
        error_msg = 'Nenhum campo fornecido para atualização.'
        return {'message': error_msg}, 400

    # Atualiza os campos do objeto 'ativo'
    for key, value in update_data.items():
        setattr(ativo, key, value)

    try:
        session.commit()
        return schemas.apresentar_ativo(ativo), 200
    except IntegrityError:
        error_msg = 'Já existe um ativo com o ticker informado.'
        return {'message': error_msg}, 409

    except SQLAlchemyError as e:
        error_msg = 'Não foi possível atualizar o Ativo.'
        print(e)
        return {'message': error_msg}, 500


@app.delete('/ativos', tags=[ativo_delete_tag], \
            responses={'200': schemas.AtivoDeleteSchema, '404': schemas.ErrorSchema})
def delete_ativo(query: schemas.AtivoBuscaSchema):
    """Exclui um Ativo do Banco de Dados"""
    ticker = unquote(unquote(query.ticker))

    session = Session()
    ativo = session.query(Ativo).filter(Ativo.ticker == ticker).first()

    if ativo:
        session.delete(ativo)
        session.commit()
        return {'message': 'Ativo removido', 'ticker': ativo.ticker}
    else:
        error_msg = 'Ativo não encontrado na base de dados'
        return {'message': error_msg}, 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
