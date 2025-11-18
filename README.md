# Projeto Back-end - MVP Full Stack Básico

Este repositório contém o código-fonte do back-end para o MVP do curso de Desenvolvimento Full Stack Básico da PUC-RJ.

## 🚀 Sobre o Projeto

*(Aqui você pode adicionar uma descrição mais detalhada sobre o que a sua API faz, quais são seus objetivos e principais funcionalidades.)*

---

## 🛠️ Pré-requisitos

Antes de começar, garanta que você tenha o [Python 3.14.0](https://www.python.org/downloads/) instalado em sua máquina.

## ⚙️ Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto localmente.

1.  **Clone o repositório**

    ```bash
    gh repo clone ronaldpedra/PUC-RJ_ronaldpedra_Dev_Full_Stack_Back-end
    ```

    ```bash
    cd PUC-RJ_ronaldpedra_Dev_Full_Stack_Back-end
    ```

2.  **Crie e ative o ambiente virtual**

    -   Crie o ambiente:
        ```bash
        python -m venv venv
        ```

    -   Ative o ambiente:
        -   No Windows (PowerShell):
            ```bash
            .\venv\Scripts\Activate.ps1
            ```
        -   No Linux ou macOS:
            ```bash
            source venv/bin/activate
            ```

3.  **Instale as dependências**

    Com o ambiente virtual ativo, instale todas as dependências listadas no arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação**

    *(Adicione aqui o comando para iniciar sua aplicação. Exemplo abaixo para Flask)*
    ```bash
    set FLASK_APP=app.py
    ```

    ```bash
    flask run
    ```