"""Esquema de representação de Movimentações"""
from typing import List
from pydantic import BaseModel

from models.movimentacao import Movimentacao

class MovimentacaoPostSchema(BaseModel):
    """Define como uma nova Movimentação deve ser representada ao ser criada"""
    movimento: str = 'Compra'
    ticker: str = 'PETR4'
    qtd_operacao: int = 100
    qtd_carteira: int = 100
    valor: float = 34.21
    preco_medio: float = 34.21
    total_operacao: float = 3421.00
    total_investido: float = 3421.00
    lucro_operacao: float = 0.0
    lucro_investimento: float = 0.0


class MovimentacaoViewSchema(BaseModel):
    """Define como uma Movimentação será retornada"""
    id: int = 1
    data_registro: str = '2025-11-20 04:24:36.531165'
    movimento: str = 'Compra'
    ticker: str = 'PETR4'
    qtd_operacao: int = 100
    qtd_carteira: int = 100
    valor: float = 34.21
    preco_medio: float = 34.21
    total_operacao: float = 3421.00
    total_investido: float = 3421.00
    lucro_operacao: float = 0.0
    lucro_investimento: float = 0.0

class ListarMovimentacoesSchema(BaseModel):
    """Define como uma listagem de Movimentações será retornada"""
    movimentacoes:List[MovimentacaoViewSchema]

class ListarCarteiraSchema(BaseModel):
    """Define como uma listagem de Carteira será retornada"""
    carteira:List[MovimentacaoViewSchema]

def apresentar_movimentacao(movimentacao: Movimentacao):
    """Retorna uma representação da Movimentação"""
    return {
        'id': movimentacao.id,
        'data_registro': movimentacao.data_registro,
        'movimento': movimentacao.movimento,
        'ticker': movimentacao.ticker,
        'qtd_operacao': movimentacao.qtd_operacao,
        'qtd_carteira': movimentacao.qtd_carteira,
        'valor': movimentacao.valor,
        'preco_medio': movimentacao.preco_medio,
        'total_operacao': movimentacao.total_operacao,
        'total_investido': movimentacao.total_investido,
        'lucro_operacao': movimentacao.lucro_operacao,
        'lucro_investimento': movimentacao.lucro_investimento
    }

def apresentar_movimentacoes(movimentacoes: List[Movimentacao]):
    """Retorna uma representação da Movimentação seguindo o schema definido em 
    MovimentacaoViewSchema"""
    result = [{
        'id': m.id,
        'data_registro': m.data_registro,
        'movimento': m.movimento,
        'ticker': m.ticker,
        'qtd_operacao': m.qtd_operacao,
        'qtd_carteira': m.qtd_carteira,
        'valor': m.valor,
        'preco_medio': m.preco_medio,
        'total_operacao': m.total_operacao,
        'total_investido': m.total_investido,
        'lucro_operacao': m.lucro_operacao,
        'lucro_investimento': m.lucro_investimento
    } for m in movimentacoes]
    return {'movimentacoes': result}

def apresentar_carteira(carteira: List[Movimentacao]):
    """Retorna uma representação da Movimentação seguindo o schema definido em 
    MovimentacaoViewSchema"""
    result = [{
        'id': ativo.id,
        'data_registro': ativo.data_registro,
        'movimento': ativo.movimento,
        'ticker': ativo.ticker,
        'qtd_operacao': ativo.qtd_operacao,
        'qtd_carteira': ativo.qtd_carteira,
        'valor': ativo.valor,
        'preco_medio': ativo.preco_medio,
        'total_operacao': ativo.total_operacao,
        'total_investido': ativo.total_investido,
        'lucro_operacao': ativo.lucro_operacao,
        'lucro_investimento': ativo.lucro_investimento
    } for ativo in carteira]
    return {'carteira': result}
