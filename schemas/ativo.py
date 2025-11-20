"""Esquema de representação de Ativos"""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from models.ativos import Ativo
from models.enums import ClasseAtivoEnum


class AtivoSchema(BaseModel):
    """Define como um novo Ativo inserido deve ser representado"""
    ticker: str = 'PETR4'
    short_name: Optional[str] = 'PETROBRAS PN N2'
    long_name: Optional[str] = 'Petróleo Brasileiro S.A. - Petrobras'
    classe_b3: ClasseAtivoEnum = ClasseAtivoEnum.ACOES

class AtivoViewSchema(BaseModel):
    """Define como será retornado o Ativo"""
    ticker: str = 'PETR4'
    short_name: Optional[str] = 'PETROBRAS PN N2'
    long_name: Optional[str] = 'Petróleo Brasileiro S.A. - Petrobras'
    classe_b3: ClasseAtivoEnum = ClasseAtivoEnum.ACOES
    data_insercao: datetime = datetime.now()

def apresentar_ativo(ativo: Ativo):
    """Retorna uma representação do Ativo"""
    return {
        'ticker': ativo.ticker,
        'short_name': ativo.short_name,
        'long_name': ativo.long_name,
        'classe_b3': ativo.classe_b3,
        'data_insercao': ativo.data_insercao
    }

class ListarAtivosSchema(BaseModel):
    """Define como uma listagem de Ativos será retornada"""
    ativos:List[AtivoViewSchema]

def apresentar_ativos(ativos: List[Ativo]):
    """Retorna uma representação do Ativo seguindo o schema definido em 
    AtivoViewSchema"""
    result = [{
        'ticker': a.ticker,
        'short_name': a.short_name,
        'long_name': a.long_name,
        'classe_b3': a.classe_b3,
        'data_insercao': a.data_insercao
    } for a in ativos]
    return {'ativos': result}
