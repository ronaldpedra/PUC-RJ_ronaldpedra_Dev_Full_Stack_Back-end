"""Rotas para o recurso Ativo"""

from urllib.parse import unquote
from flask_openapi3.blueprint import APIBlueprint
from flask_openapi3.models.tag import Tag
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from models import Session, Ativo
import schemas

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
def add_ativo(form: schemas.AtivoSchema):
    """Adiciona um Ativo à base de dados e retorna uma representação do Ativo"""
    session = Session()
    try:
        ativo = Ativo(
            ticker=form.ticker,
            short_name=form.short_name,
            long_name=form.long_name,
            classe_b3=form.classe_b3
        )
        session.add(ativo)
        session.commit()
        return schemas.apresentar_ativo(ativo), 200

    except IntegrityError:
        session.rollback()
        error_msg = 'Ativo com o mesmo Ticker já cadastrado'
        return {'message': error_msg}, 409

    except SQLAlchemyError as e:
        session.rollback()
        error_msg = 'Não foi possível salvar o Ativo.'
        print(e)
        return {'message': error_msg}, 500
    finally:
        session.close()


@api.get('/',
         summary='Lista todos os Ativos',
         description='Retorna todos os Ativos cadastrados no Banco de Dados.',
         responses={'200': schemas.ListarAtivosSchema, \
                    '404': schemas.ErrorSchema})
def get_ativos():
    """Retorna todos os Ativos cadastrados no Banco de Dados"""
    session = Session()
    try:
        ativos = session.query(Ativo).all()

        if not ativos:
            return {'ativos': []}, 200

        return schemas.apresentar_ativos(ativos), 200
    finally:
        session.close()


@api.patch('/',
           summary='Atualiza um Ativo existente',
           description='Atualiza um Ativo existente no Banco de Dados ' \
           'com base no ticker.',
           responses={'200': schemas.AtivoViewSchema, \
                      '400': schemas.ErrorSchema, '404': schemas.ErrorSchema, \
                      '409': schemas.ErrorSchema})
def update_ativo(query: schemas.AtivoBuscaSchema, \
                 form: schemas.AtivoUpdateSchema):
    """Atualiza um Ativo existente no Banco de Dados.

    Retorna uma representação atualizada do ativo.
    """
    ticker = unquote(unquote(query.ticker))
    session = Session()
    try:
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

        session.commit()
        return schemas.apresentar_ativo(ativo), 200
    except IntegrityError:
        session.rollback()
        error_msg = 'Já existe um ativo com o ticker informado.'
        return {'message': error_msg}, 409

    except SQLAlchemyError as e:
        session.rollback()
        error_msg = 'Não foi possível atualizar o Ativo.'
        print(e)
        return {'message': error_msg}, 500
    finally:
        session.close()


@api.delete('/',
            summary='Exclui um Ativo',
            description='Exclui um Ativo do Banco de Dados com base no ticker.',
            responses={'200': schemas.AtivoDeleteSchema, \
                       '404': schemas.ErrorSchema, '500': schemas.ErrorSchema})
def delete_ativo(query: schemas.AtivoBuscaSchema):
    """Exclui um Ativo do Banco de Dados"""
    ticker = unquote(unquote(query.ticker))
    session = Session()
    try:
        ativo = session.query(Ativo).filter(Ativo.ticker == ticker).first()

        if not ativo:
            error_msg = 'Ativo não encontrado na base de dados'
            return {'message': error_msg}, 404

        session.delete(ativo)
        session.commit()
        return {'message': 'Ativo removido', 'ticker': ativo.ticker}, 200
    except SQLAlchemyError as e:
        session.rollback()
        error_msg = "Não foi possível excluir o ativo."
        print(e)
        return {"message": error_msg}, 500
    finally:
        session.close()
