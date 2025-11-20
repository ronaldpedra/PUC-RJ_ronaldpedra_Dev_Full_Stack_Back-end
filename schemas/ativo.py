"""Esquema de representação de Ativos"""
from typing import Optional, List
from pydantic import BaseModel

from models.ativos import Ativo


class AtivoSchema(BaseModel):
    """Define como um novo Ativo inserido deve ser representado"""
    ticker: str = 'PETR4'
    short_name: Optional[str] = 'PETROBRAS PN N2'
    long_name: Optional[str] = 'Petróleo Brasileiro S.A. - Petrobras'
    classe_b3: str = 'Ações'
    # data_insercao: Union[datetime, None] = None

class AtivoViewSchema(BaseModel):
    """Define como será retornado o Ativo"""
    ticker: str = 'PETR4'
    short_name: Optional[str] = 'PETROBRAS PN N2'
    long_name: Optional[str] = 'Petróleo Brasileiro S.A. - Petrobras'
    classe_b3: str = 'Ações'

def apresentar_ativo(ativo: Ativo):
    """Retorna uma representação do Ativo"""
    return {
        'ticker': ativo.ticker,
        'short_name': ativo.short_name,
        'long_name': ativo.long_name,
        'classe_b3': ativo.classe_b3
    }

class ListarAtivosSchema(BaseModel):
    """Define como uma listagem de Ativos será retornada"""
    ativos:List[AtivoSchema]

def apresentar_ativos(ativos: List[Ativo]):
    """Retorna uma representação do Ativo seguindo o schema definido em 
    AtivoViewSchema"""
    result = []
    for ativo in ativos:
        result.append({
            'ticker': ativo.ticker,
            'short_name': ativo.short_name,
            'long_name': ativo.long_name,
            'classe_b3': ativo.classe_b3
        })
    return {'ativos': result}
