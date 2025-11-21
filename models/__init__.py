"""Este arquivo é responsável pela gestão de criação e conexão com o 
Banco de Dados DashInvest"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

# Importando elementos definidos no modelo
from models.base import Base
from models.ativos import Ativo
from models.movimentacao import Movimentacao


DB_PATH = 'database/'  # Não poderia ser instance como no flask-SQLAlchemy?

# Verifica se o diretório não existe
if not os.path.exists(DB_PATH):
    # então cria o diretório
    os.mkdir(DB_PATH)

# URL de acesso ao Banco de Dados DashInvest (SQLite)
DB_URL = f'sqlite:///{DB_PATH}/dashinvest.sqlite3'

# Cria a engine de conexão com o banco
engine = create_engine(DB_URL, echo=False)

# Instacia um criador de Seção com o banco
Session = sessionmaker(bind=engine)

# Cria o Banco de Dados DashInvest se não existir
if not database_exists(engine.url):
    create_database(engine.url)

# Cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)
