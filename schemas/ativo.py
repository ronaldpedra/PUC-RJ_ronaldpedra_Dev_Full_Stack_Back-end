"""Esquema de representação de Ativos"""
from typing import Optional, Union
from datetime import datetime
from pydantic import BaseModel

from models.ativos import Ativo


class AtivoSchema(BaseModel):
    """Define como um novo Ativo inserido deve ser representado"""
    ticker: str = 'PETR4'
    nome: Optional[str] = 'Petrobras'
    classe_b3: str = 'Ações'
    # data_insercao: Union[datetime, None] = None

class AtivoViewSchema(BaseModel):
    """Define como será retornado o Ativo"""
    ticker: str = 'PETR4'
    nome: Optional[str] = 'Petrobras'
    classe_b3: str = 'Ações'

def apresentar_ativo(ativo: Ativo):
    """Retorna uma representação do Ativo"""
    return {
        'ticker': ativo.ticker,
        'nome': ativo.nome,
        'classe_b3': ativo.classe_b3
    }
