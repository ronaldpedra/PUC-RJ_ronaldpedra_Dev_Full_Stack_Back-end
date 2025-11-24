![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.14+-blue.svg)

# DashInvest API - MVP

Este repositório contém o código-fonte do back-end para o MVP do curso de Desenvolvimento Full Stack Básico da PUC-RJ.

## 🚀 Sobre o Projeto

A **DashInvest API** é uma aplicação back-end desenvolvida em Python com Flask, projetada para gerenciar um portfólio de investimentos. Ela permite o cadastro de diferentes tipos de ativos financeiros (como Ações, FIIs, BDRs, etc.) e o registro de todas as movimentações de compra e venda.

O principal objetivo é fornecer endpoints robustos para que uma aplicação front-end possa consumir os dados e apresentar ao usuário sua carteira de investimentos consolidada e atualizada.

### ✨ Principais Funcionalidades

- **Gerenciamento de Ativos (CRUD):** Adicionar, listar, atualizar e remover ativos da base de dados.
- **Registro de Movimentações:** Registrar operações de compra e venda de ativos.
- **Visualização de Carteira:** Um endpoint dedicado que retorna a posição consolidada de cada ativo na carteira, mostrando a quantidade atual, preço médio e outras informações relevantes.
- **Documentação Automática:** A API gera automaticamente uma documentação interativa com Swagger UI.

---

## 📚 Documentação da API

Toda a documentação dos endpoints, incluindo modelos de requisição e resposta, está disponível de forma interativa através do Swagger UI.

Após iniciar a aplicação, acesse a seguinte URL no seu navegador:

**[http://127.0.0.1:5000/openapi](http://127.0.0.1:5000/openapi)**

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3.14+](https://www.python.org/)**: Linguagem de programação.
- **[Flask](https://flask.palletsprojects.com/)**: Micro-framework web para a construção da API.
- **[Flask-OpenAPI3](https://github.com/luopei/flask-openapi3)**: Geração automática de documentação OpenAPI (Swagger).
- **[SQLAlchemy](https://www.sqlalchemy.org/)**: ORM para interação com o banco de dados.
- **[Pydantic](https://docs.pydantic.dev/)**: Validação de dados e serialização de schemas.
- **[Flask-CORS](https://flask-cors.readthedocs.io/)**: Gerenciamento de Cross-Origin Resource Sharing.

---

## ⚙️ Instalação e Execução Local

Siga os passos abaixo para configurar e executar o projeto em seu ambiente de desenvolvimento.

### Pré-requisitos

- [Python 3.14](https://www.python.org/downloads/) ou superior.
- [Git](https://git-scm.com/) instalado.

### Passos

1.  **Clone o repositório:**

    ```bash
    gh repo clone ronaldpedra/PUC-RJ_ronaldpedra_Dev_Full_Stack_Back-end
    cd PUC-RJ_ronaldpedra_Dev_Full_Stack_Back-end
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    # Cria o ambiente virtual
    python -m venv venv

    # Ativa o ambiente
    # No Windows (PowerShell):
    .\venv\Scripts\Activate.ps1
    # No Linux ou macOS:
    source venv/bin/activate
    ```

3.  **Instale as dependências:**

    Com o ambiente virtual ativo, instale todas as dependências listadas no arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**

    ```bash
    # O modo debug irá recarregar o servidor automaticamente a cada alteração.
    set FLASK_APP=app.py
    flask run --debug
    ```

5.  **Acesse a API:**

    A aplicação estará rodando em `http://127.0.0.1:5000`.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

## 👨‍💻 Autor

*   **Ronald Pedra** - [ronaldpedra (github)](https://github.com/ronaldpedra)