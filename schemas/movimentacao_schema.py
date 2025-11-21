"""Esquema de representação de Movimentações"""
from typing import List
from pydantic import BaseModel

from models.movimentacao import Movimentacao

class MovimentacaoPostSchema(BaseModel):
    """Define como uma nova Movimentação deve ser representada ao ser criada"""
    movimento: str = 'Compra'
    ticker: str = 'PETR4'
    quantidade: int = 100
    valor: float = 34.21
    preco_medio: float = 34.21
    valor_total: float = 3421.00

class MovimentacaoViewSchema(BaseModel):
    """Define como uma Movimentação será retornada"""
    id: int = 1
    data_registro: str = '2025-11-20 04:24:36.531165'
    movimento: str = 'Compra'
    ticker: str = 'PETR4'
    quantidade: int = 100
    valor: float = 34.21
    preco_medio: float = 34.21
    valor_total: float = 3421.00

class ListarMovimentacoesSchema(BaseModel):
    """Define como uma listagem de Movimentações será retornada"""
    movimentacoes:List[MovimentacaoViewSchema]

def apresentar_movimentacao(movimentacao: Movimentacao):
    """Retorna uma representação da Movimentação"""
    return {
        'id': movimentacao.id,
        'data_registro': movimentacao.data_registro,
        'movimento': movimentacao.movimento,
        'ticker': movimentacao.ticker,
        'quantidade': movimentacao.quantidade,
        'valor': movimentacao.valor,
        'preco_medio': movimentacao.preco_medio,
        'valor_total': movimentacao.valor_total
    }

def apresentar_movimentacoes(movimentacoes: List[Movimentacao]):
    """Retorna uma representação da Movimentação seguindo o schema definido em 
    MovimentacaoViewSchema"""
    result = [{
        'id': m.id,
        'data_registro': m.data_registro,
        'movimento': m.movimento,
        'ticker': m.ticker,
        'quantidade': m.quantidade,
        'valor': m.valor,
        'preco_medio': m.preco_medio,
        'valor_total': m.valor_total
    } for m in movimentacoes]
    return {'movimentacoes': result}
