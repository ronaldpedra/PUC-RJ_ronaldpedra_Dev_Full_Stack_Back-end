"""Modelo dos Ativos cadastrados em DashInvest"""

from sqlalchemy import Column, String, Integer, DateTime, Float

from models import Base


class Ativo(Base):
    __tablename__ = 'ativo'

    ticker = Column(String(10), primary_key=True)
    nome = Column(String(60))

