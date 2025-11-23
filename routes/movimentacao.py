"""Rotas para o recurso Movimentação"""

from flask_openapi3.blueprint import APIBlueprint
from flask_openapi3.models.tag import Tag
from sqlalchemy import func

import schemas
from models import Movimentacao, Ativo
from common.decorators import db_session_manager


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
@db_session_manager
def add_movimentacao(session, form: schemas.MovimentacaoPostSchema):
    """Adiciona uma Movimentação à base de dados e retorna uma 
    representação da Movimentação"""
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
    # Faz o flush para o banco para obter os dados gerados (como id e data_registro)
    # antes de fazer o commit (que é feito pelo decorator).
    session.flush()

    return schemas.MovimentacaoViewSchema.model_validate(movimentacao)


@api.get('/carteira',
         summary='Retorna a carteira de investimentos atual',
         description='Retorna o último registro de cada ativo que já foi ' \
         'negociado, mesmo que a quantidade atual seja zero.',
         responses={'200': schemas.ListarCarteiraSchema, \
                    '500': schemas.ErrorSchema})
@db_session_manager
def get_carteira(session):
    """Retorna a carteira de investimentos do usuário.

    A carteira é composta pelo último registro de cada ativo (ticker),
    independentemente da quantidade atual em custódia.
    """
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

    # Adiciona dinamicamente o atributo 'classe_b3' ao objeto de movimentação.
    # O Pydantic usará 'from_attributes' para ler este novo atributo.
    carteira_objetos = []
    for movimentacao, classe_b3 in results:
        movimentacao.classe_b3 = classe_b3
        carteira_objetos.append(movimentacao)

    return schemas.ListarCarteiraSchema(carteira=carteira_objetos)
