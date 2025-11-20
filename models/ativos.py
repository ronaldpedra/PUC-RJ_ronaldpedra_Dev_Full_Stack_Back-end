"""Modelo dos Ativos cadastrados em DashInvest"""

from datetime import datetime
from sqlalchemy import Column, String, DateTime, Enum

from models.enums import ClasseAtivoEnum
from models import Base


class Ativo(Base):
    """Tabela de Ativos"""
    __tablename__ = 'ativo'

    ticker = Column(String(10), primary_key=True)
    short_name = Column(String(60))
    long_name = Column(String(120))
    classe_b3 = Column(Enum(ClasseAtivoEnum))
    data_insercao = Column(DateTime, default=datetime.now)
