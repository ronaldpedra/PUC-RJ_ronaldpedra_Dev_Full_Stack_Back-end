"""Esquema de representação de erros da API DashInvest"""
from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """ Define como uma mensagem de erro será representada
    """
    mesage: str
