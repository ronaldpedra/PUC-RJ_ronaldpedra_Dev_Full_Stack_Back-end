"""Rotas para o recurso Ativo"""

from urllib.parse import unquote
from flask_openapi3.blueprint import APIBlueprint
from flask_openapi3.models.tag import Tag

import schemas
from models import Ativo
from common.decorators import db_session_manager

# Define a tag para o recurso Ativo
ativo_tag = Tag(
    name='Ativo',
    description='Operações relacionadas a Ativos: adição, listagem, \
        atualização e exclusão.')

# Cria o blueprint para o recurso Ativo
api = APIBlueprint('ativo', __name__, url_prefix='/ativos',
                   abp_tags=[ativo_tag])


@api.post('/',
          summary='Adiciona um novo Ativo',
          description='Adiciona um Ativo à base de dados e retorna uma representação do mesmo.',
          responses={'200': schemas.AtivoViewSchema, '409': schemas.ErrorSchema,
                     '400': schemas.ErrorSchema})
@db_session_manager
def add_ativo(session, form: schemas.AtivoSchema):
    """Adiciona um Ativo à base de dados e retorna uma representação do Ativo"""
    ativo = Ativo(
        ticker=form.ticker,
        short_name=form.short_name,
        long_name=form.long_name,
        classe_b3=form.classe_b3
    )
    session.add(ativo)
    # Faz o flush para o banco para obter os dados gerados (como a data_insercao)
    # antes de fazer o commit (que é feito pelo decorator).
    session.flush()

    return schemas.AtivoViewSchema.model_validate(ativo)


@api.get('/',
         summary='Lista todos os Ativos',
         description='Retorna todos os Ativos cadastrados no Banco de Dados.',
         responses={'200': schemas.ListarAtivosSchema, \
                    '404': schemas.ErrorSchema})
@db_session_manager
def get_ativos(session):
    """Retorna todos os Ativos cadastrados no Banco de Dados"""
    ativos = session.query(Ativo).all()

    if not ativos:
        return schemas.ListarAtivosSchema(ativos=[])
    return schemas.ListarAtivosSchema(ativos=ativos)


@api.patch('/',
           summary='Atualiza um Ativo existente',
           description='Atualiza um Ativo existente no Banco de Dados ' \
           'com base no ticker.',
           responses={'200': schemas.AtivoViewSchema, \
                      '400': schemas.ErrorSchema, '404': schemas.ErrorSchema, \
                      '409': schemas.ErrorSchema})
@db_session_manager
def update_ativo(session, query: schemas.AtivoBuscaSchema, \
                 form: schemas.AtivoUpdateSchema):
    """Atualiza um Ativo existente no Banco de Dados.

    Retorna uma representação atualizada do ativo.
    """
    ticker = unquote(unquote(query.ticker))
    ativo = session.query(Ativo).filter(Ativo.ticker == ticker).first()

    if not ativo:
        error_msg = 'Ativo não encontrado na base de dados'
        return {'message': error_msg}, 404

    update_data = form.model_dump(exclude_unset=True)

    if not update_data:
        error_msg = 'Nenhum campo fornecido para atualização.'
        return {'message': error_msg}, 400

    for key, value in update_data.items():
        setattr(ativo, key, value)

    return schemas.AtivoViewSchema.model_validate(ativo)


@api.delete('/',
            summary='Exclui um Ativo',
            description='Exclui um Ativo do Banco de Dados com base no ticker.',
            responses={'200': schemas.AtivoDeleteSchema, \
                       '404': schemas.ErrorSchema, '500': schemas.ErrorSchema})
@db_session_manager
def delete_ativo(session, query: schemas.AtivoBuscaSchema):
    """Exclui um Ativo do Banco de Dados"""
    ticker = unquote(unquote(query.ticker))
    ativo = session.query(Ativo).filter(Ativo.ticker == ticker).first()

    if not ativo:
        error_msg = 'Ativo não encontrado na base de dados'
        return {'message': error_msg}, 404

    session.delete(ativo)
    return {'message': 'Ativo removido', 'ticker': ativo.ticker}
