"""Rotas para o recurso Movimentação"""

from flask_openapi3.blueprint import APIBlueprint
from flask_openapi3.models.tag import Tag
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func, inspect

from models import Session, Movimentacao, Ativo
import schemas


# Define a tag para o recurso Movimentação
movimentacao_tag = Tag(
    name='Movimentação',
    description='Operações relacionadas às Movimentações: adição, listagem, \
        atualização e exclusão sobre as Compras e Vendas de Ativos.')

# Cria o blueprint para o recurso Movimentação
api = APIBlueprint('movimentacao', __name__, url_prefix='/movimentacoes',
                   abp_tags=[movimentacao_tag])

@api.post('/',
          summary='Adiciona uma nova Movimentação',
          description='Adiciona uma Movimentação à base de dados e ' \
          'retorna uma representação da mesma.',
          responses={'200': schemas.MovimentacaoViewSchema, \
                     '409': schemas.ErrorSchema,
                     '400': schemas.ErrorSchema})
def add_movimentacao(form: schemas.MovimentacaoPostSchema):
    """Adiciona uma Movimentação à base de dados e retorna uma 
    representação da Movimentação"""
    session = Session()
    try:
        movimentacao = Movimentacao(
            movimento = form.movimento,
            ticker = form.ticker,
            qtd_operacao = form.qtd_operacao,
            qtd_carteira = form.qtd_carteira,
            valor = form.valor,
            preco_medio = form.preco_medio,
            total_operacao = form.total_operacao,
            total_investido = form.total_investido,
            lucro_operacao = form.lucro_operacao,
            lucro_investimento = form.lucro_investimento
        )
        session.add(movimentacao)
        session.commit()
        return schemas.apresentar_movimentacao(movimentacao), 200

    except SQLAlchemyError as e:
        session.rollback()
        error_msg = 'Não foi possível salvar a Movimentação.'
        print(e)
        return {'message': error_msg}, 500
    finally:
        session.close()


@api.get('/carteira',
         summary='Retorna a carteira de investimentos atual',
         description='Retorna o último registro de cada ativo que já foi ' \
         'negociado, mesmo que a quantidade atual seja zero.',
         responses={'200': schemas.ListarCarteiraSchema, \
                    '404': schemas.ErrorSchema})
def get_carteira():
    """Retorna a carteira de investimentos do usuário.

    A carteira é composta pelo último registro de cada ativo (ticker),
    independentemente da quantidade atual em custódia.
    """
    session = Session()
    try:

        # Subquery para encontrar o ID da última movimentação para cada ticker
        latest_mov_subquery = session.query(
            Movimentacao.ticker,
            func.max(Movimentacao.id).label('max_id')
        ).group_by(Movimentacao.ticker).subquery()

        # Query para buscar as movimentações e a classe_b3 do ativo
        # correspondentes aos IDs da subquery
        results = session.query(Movimentacao, Ativo.classe_b3).join(
            Ativo, Movimentacao.ticker == Ativo.ticker
        ).join(
            latest_mov_subquery,
            (Movimentacao.id == latest_mov_subquery.c.max_id)
        ).all()

        # Monta a resposta combinando os dados da movimentação e do ativo
        carteira = []
        for movimentacao, classe_b3 in results:
            mov_dict = {c.key: getattr(movimentacao, c.key) for c in inspect(movimentacao).mapper.column_attrs}
            mov_dict['classe_b3'] = classe_b3
            carteira.append(mov_dict)

        # A função apresentar_carteira agora espera a lista de dicionários
        # e a retorna no formato correto.
        return schemas.apresentar_carteira(carteira), 200

    except SQLAlchemyError as e:
        session.rollback()
        error_msg = 'Erro ao buscar a carteira.'
        print(e)
        return {'message': error_msg}, 500
    finally:
        session.close()
