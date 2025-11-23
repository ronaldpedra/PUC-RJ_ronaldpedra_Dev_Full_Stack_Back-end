"""Esquema de representação de Ativos"""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
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
    data_insercao: datetime

    class Config:
        """Configuração que permite ao Pydantic criar o schema a partir de
        atributos de um objeto (modo ORM), não apenas de dicionários.
        """
        from_attributes = True

class ListarAtivosSchema(BaseModel):
    """Define como uma listagem de Ativos será retornada"""
    ativos:List[AtivoViewSchema]

class AtivoUpdateSchema(BaseModel):
    """Define os campos que podem ser atualizados em um Ativo"""
    ticker: Optional[str] = 'PETR3'
    short_name: Optional[str] = 'PETROBRAS ON N2'
    long_name: Optional[str] = 'Petróleo Brasileiro S.A. - Petrobras'
    classe_b3: Optional[ClasseAtivoEnum] = 'Ações'

class AtivoDeleteSchema(BaseModel):
    """Define como deve ser a estrutura do dado retornado após uma requisição
    de remoção"""
    message: str
    ticker: str

class AtivoBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca, que será
    feita apenas com base no ticker do ativo."""
    ticker: str = 'PETR4'
