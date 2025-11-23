"""Esquema de representação de Movimentações"""
from typing import List
from datetime import datetime
from pydantic import BaseModel
from models.enums import ClasseAtivoEnum


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
    data_registro: datetime
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

    class Config:
        """Configuração que permite ao Pydantic criar o schema a partir de
        atributos de um objeto (modo ORM), não apenas de dicionários.
        """
        from_attributes = True

class CarteiraViewSchema(MovimentacaoViewSchema):
    """Define como um ativo na carteira será retornado.
    
    Herda todos os campos de MovimentacaoViewSchema e adiciona a classe B3 do ativo.
    """
    classe_b3: ClasseAtivoEnum = ClasseAtivoEnum.ACOES

class ListarMovimentacoesSchema(BaseModel):
    """Define como uma listagem de Movimentações será retornada"""
    movimentacoes:List[MovimentacaoViewSchema]

class ListarCarteiraSchema(BaseModel):
    """Define como uma listagem de Carteira será retornada"""
    carteira:List[CarteiraViewSchema]
