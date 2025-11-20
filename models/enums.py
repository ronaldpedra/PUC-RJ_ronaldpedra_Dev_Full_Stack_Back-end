"""Define Enums utilizados nos modelos"""

import enum


class ClasseAtivoEnum(str, enum.Enum):
    """Enum para as classes de ativos da B3"""
    ACOES = 'Ações'
    FII = 'FII'
    ETF = 'ETF'
    BDR = 'BDR'
