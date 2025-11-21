"""Modelo de como as movimentações financeiras são registradas na 
Carteira de Investimentos de DashInvest"""

from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer, DECIMAL, \
    BigInteger, ForeignKey
from models import Base


class Movimentacao(Base):
    """Tabela de Movimentações"""
    __tablename__ = 'movimentacao'

    id = Column(BigInteger, primary_key=True)
    data_registro = Column(DateTime, default=datetime.now, nullable=False)
    movimento = Column(String(10), nullable=False)  # Compra ou Venda
    ticker = Column(String(10), ForeignKey('ativo.ticker'), nullable=False)
    quantidade = Column(Integer, nullable=False)
    valor = Column(DECIMAL(10, 2), nullable=False)
