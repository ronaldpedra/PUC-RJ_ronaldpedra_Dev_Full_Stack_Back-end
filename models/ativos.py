"""Modelo dos Ativos cadastrados em DashInvest"""

from sqlalchemy import Column, String, DateTime
from datetime import datetime
from typing import Union


from models import Base


class Ativo(Base):
    __tablename__ = 'ativo'

    ticker = Column(String(10), primary_key=True)
    nome = Column(String(60))
    classe_b3 = Column(String(10))
    data_insercao = Column(DateTime, default=datetime.now())


    def __init__(self, ticker: str, nome: Union[str, None] = None, 
                 classe_b3: str = None, 
                 data_insercao: Union[DateTime, None] = None):
        """
        Cria um ativo

        Arguments:
            ticker: Código do ativo na B3. Ex: PETR4
            nome: Nome do ativo. Ex: Petrobras
            classe_b3: Classe do ativo na B3. Ex: Ações
            data_insercao: Data de quando o ativo foi inserido à base
        """
        self.ticker = ticker
        self.nome = nome
        self.classe_b3 = classe_b3

        # Se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
