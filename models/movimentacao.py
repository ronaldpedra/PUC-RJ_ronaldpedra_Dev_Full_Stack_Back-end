"""Modelo de como as movimentações financeiras são registradas na 
Carteira de Investimentos de DashInvest"""

from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer, DECIMAL, \
    ForeignKey
from models import Base


class Movimentacao(Base):
    """Tabela de Movimentações"""
    __tablename__ = 'movimentacao'

    id = Column(Integer, primary_key=True)
    data_registro = Column(DateTime, default=datetime.now, nullable=False)
    movimento = Column(String(10), nullable=False)  # Compra ou Venda
    ticker = Column(String(10), ForeignKey('ativo.ticker'), nullable=False)
    qtd_operacao = Column(Integer, nullable=False)
    qtd_carteira = Column(Integer, nullable=False)
    valor = Column(DECIMAL(10, 2), nullable=False)
    preco_medio = Column(DECIMAL(10, 2), nullable=False)
    total_operacao = Column(DECIMAL(10, 2), nullable=False)
    total_investido = Column(DECIMAL(10, 2), nullable=False)
    lucro_operacao = Column(DECIMAL(10, 2), nullable=False)
    lucro_investimento = Column(DECIMAL(10, 2), nullable=False)
