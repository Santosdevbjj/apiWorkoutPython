## Desenvolvendo sua Primeira API com FastAPI, Python e Docker


![PythonDeveloper001](https://github.com/user-attachments/assets/925b7f1e-5e0c-4c09-b26b-3ab76cb2f819)



**Bootcamp Luizalabs - Back-end com Python.**


---


 🏋️‍♂️ **API Workout Python**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-brightgreen?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)
![CI](https://github.com/Santosdevbjj/apiWorkoutPython/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> API RESTful para gerenciamento de **atletas**, **categorias** e **centros de treinamento**, construída com FastAPI, SQLAlchemy, Alembic e Docker.  
> Projetada com arquitetura modular, testes automatizados e integração contínua.

---

 🧭 **Índice**

- [⚡ Tecnologias](#-tecnologias)
- [🖥️ Requisitos de Hardware e Software](#️-requisitos-de-hardware-e-software)
- [📁 Estrutura de Pastas](#-estrutura-de-pastas)
- [🧰 Arquivos Importantes](#-arquivos-importantes)
- [🚀 Como Rodar o Projeto](#-como-rodar-o-projeto)
- [📡 Exemplos de Requisições](#-exemplos-de-requisições)
- [🧪 Testes Automatizados](#-testes-automatizados)
- [🐳 Uso com Docker](#-uso-com-docker)
- [📬 Coleção Postman](#-coleção-postman)
- [📜 Licença](#-licença)

---

 ⚡ **Tecnologias**

- **Linguagem:** Python 3.11+
- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Migrações:** Alembic
- **Banco de Dados:** PostgreSQL
- **Testes:** Pytest
- **Containerização:** Docker + Docker Compose
- **CI/CD:** GitHub Actions

---

 🖥️ **Requisitos de Hardware e Software**

   **Hardware (mínimo recomendado)**
- CPU Dual-Core (2 GHz+)
- 4 GB de RAM
- 500 MB de espaço em disco para o projeto e dependências

  **Software**
- [Python 3.11+](https://www.python.org/downloads/)
- [PostgreSQL 15+](https://www.postgresql.org/)
- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) (opcional, para execução containerizada)
- [Git](https://git-scm.com/)

---

 📁 **Estrutura de Pastas**

<img width="838" height="1766" alt="Screenshot_20251011-191149" src="https://github.com/user-attachments/assets/a570aae9-8a25-4520-9aed-4a031f4b4afe" />


---

---

 🧰 **Arquivos Importantes**

| Arquivo | Função |
|---------|--------|
| `app/exceptions/handlers.py` | Define handlers globais de exceções (ex: 404, 500). |
| `app/utils/pagination.py` | Funções auxiliares para paginação de resultados nas rotas. |
| `tests/conftest.py` | Configuração global dos testes (ex: fixtures de BD e client). |
| `tests/test_atleta.py` | Testes automatizados dos endpoints de Atleta. |
| `migrations/` | Diretório gerado pelo Alembic para versionar schema do banco. |
| `docker/Dockerfile` | Receita de build da imagem da aplicação. |
| `docker/gunicorn_conf.py` | Configuração do Gunicorn para produção. |
| `docker-compose.yml` | Sobe os containers de app e banco com um comando. |
| `.env.example` | Modelo de variáveis de ambiente (DB_HOST, DB_USER, etc). |
| `.gitignore` | Arquivos e pastas ignorados pelo Git. |
| `Makefile` | Comandos prontos: `make run`, `make test`, `make migrate`. |
| `requirements.txt` | Lista de pacotes Python necessários. |

---

 🚀 **Como Rodar o Projeto**

 1️⃣ **Clonar o repositório**
```bash
git clone https://github.com/Santosdevbjj/apiWorkoutPython.git
cd apiWorkoutPython


---
```



2️⃣ **Configurar variáveis de ambiente**

cp .env.example .env
# Edite as variáveis conforme seu ambiente (DB, PORTA, etc.)

3️⃣ **Instalar dependências**

python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
pip install -r requirements.txt

4️⃣ **Criar banco de dados e aplicar migrações**

alembic upgrade head

5️⃣ **Rodar servidor de desenvolvimento**

uvicorn app.main:app --reload

Acesse 👉 http://localhost:8000/docs para testar a API.


---

📡 **Exemplos de Requisições**

✅ **Criar Atleta (POST /api/v1/atletas/)**

cURL

curl -X POST http://localhost:8000/api/v1/atletas/ \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João Silva",
    "idade": 25,
    "categoria_id": 1,
    "centro_treinamento_id": 1
  }'

**Postman**

Método: POST

URL: http://localhost:8000/api/v1/atletas/

Body: raw (JSON) conforme exemplo acima.



---

📋 **Listar Atletas (GET /api/v1/atletas/)**

curl http://localhost:8000/api/v1/atletas/?page=1&size=10


---

✏️ **Atualizar Atleta (PUT /api/v1/atletas/{id})**

curl -X PUT http://localhost:8000/api/v1/atletas/1 \
  -H "Content-Type: application/json" \
  -d '{"nome": "João Souza"}'


---

🗑️ **Deletar Atleta (DELETE /api/v1/atletas/{id})**

curl -X DELETE http://localhost:8000/api/v1/atletas/1


---

🧪 **Testes Automatizados**

Executar todos os testes com Pytest:

pytest -v


---

🐳 **Uso com Docker**

Build + Start

docker-compose up --build

A aplicação estará disponível em: http://localhost:8000


---

📬 **Coleção Postman**

Você pode importar a coleção Postman disponível em:

postman/apiWorkoutPython.postman_collection.json

> A coleção inclui exemplos prontos de requisições para todos os endpoints principais.




---

📜 **Licença**

Distribuído sob a licença MIT. Veja LICENSE para mais detalhes.


---

✨ **Autor**

Sérgio Santos
📌 Desenvolvedor | Analista de Sistemas


---











