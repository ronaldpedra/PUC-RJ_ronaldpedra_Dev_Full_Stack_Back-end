"""Modelo dos Ativos cadastrados em DashInvest"""

# from datetime import datetime
from typing import Union
from sqlalchemy import Column, String


from models import Base


class Ativo(Base):
    """Tabela de Ativos"""
    __tablename__ = 'ativo'

    ticker = Column(String(10), primary_key=True)
    short_name = Column(String(60))
    long_name = Column(String(120))
    classe_b3 = Column(String(10))
    # data_insercao = Column(DateTime, default=datetime.now())


    def __init__(self, ticker: str, short_name: Union[str, None] = None,
                 long_name: Union[str, None] = None,
                 classe_b3: str = None):
        """
        Cria um ativo

        Arguments:
            ticker: Código do ativo na B3. Ex: PETR4
            short_name: Nome abreviado do ativo. Ex: PETROBRAS PN N2
            long_name: Nome completo do ativo. Ex: Petróleo Brasileiro S.A. - Petrobras
            classe_b3: Classe do ativo na B3. Ex: Ações
        """
        self.ticker = ticker
        self.short_name = short_name
        self.long_name = long_name
        self.classe_b3 = classe_b3

        # Se não for informada, será o data exata da inserção no banco
        # if data_insercao:
        #     self.data_insercao = data_insercao
