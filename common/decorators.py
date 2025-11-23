"""Decorators para uso geral na aplicação."""

from functools import wraps
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from pydantic import BaseModel
from models import Session

def db_session_manager(f):
    """
    Decorator para gerenciar a sessão do banco de dados em uma rota Flask.
    Abre uma sessão, executa a função, faz commit ou rollback e fecha a sessão.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        session = Session()
        try:
            # Passa a sessão como um argumento para a função da rota
            result = f(session=session, *args, **kwargs)
            session.commit()

            # Verifica se o resultado é um modelo Pydantic.
            if isinstance(result, BaseModel):
                # Converte para dict e retorna com status 200 OK.
                return result.model_dump(mode='json'), 200

            return result # Retorna o resultado como está (ex: tuplas de erro)
        except IntegrityError as e:
            session.rollback()
            # Retorna um erro 409 - Conflict
            print(f"Erro de integridade: {e.orig}")
            return {"message": "Erro de integridade nos dados. Um registro similar pode já existir."}, 409
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Erro de banco de dados: {e}")
            return {"message": "Ocorreu um erro ao processar sua requisição."}, 500
        finally:
            session.close()
    return decorated_function
