"""Rotas para o recurso Movimentação"""

from flask_openapi3.blueprint import APIBlueprint
from flask_openapi3.models.tag import Tag

from models import Session, Movimentacao
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
          description='Adiciona uma Movimentação à base de dados e retorna uma representação da mesma.',
          responses={'200': schemas.MovimentacaoViewSchema, '409': schemas.ErrorSchema,
                     '400': schemas.ErrorSchema})

