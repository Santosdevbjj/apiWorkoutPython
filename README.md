## Desenvolvendo sua Primeira API com FastAPI, Python e Docker




---

WorkoutAPI: API de Competição de Crossfit (FastAPI & Async SQLAlchemy)
Este projeto implementa uma API assíncrona de alto desempenho para gerenciar Atletas, Categorias e Centros de Treinamento em uma competição de Crossfit, utilizando o FastAPI, SQLAlchemy (Async) e PostgreSQL orquestrados via Docker Compose.
🎯 Requisitos  e Desafio Final Implementados
O projeto foi construído seguindo boas práticas de POO e arquitetura de API, com foco nos seguintes requisitos:
 * Arquitetura Modular: Separação de responsabilidades em core, models, schemas e routers.
 * Query Parameters (Atleta): Filtros por nome e cpf no endpoint de listagem de atletas (GET /atletas).
 * Response Customizado (Atleta GET all): A lista paginada de atletas retorna apenas o nome, centro_treinamento (nome) e categoria (nome) através do schema AtletaAllOut.
 * Tratamento de Integridade (CPF Duplicado): Manipulação de sqlalchemy.exc.IntegrityError, retornando o status_code: 303 (See Other) com a mensagem personalizada "Já existe um atleta cadastrado com o cpf: [cpf_do_atleta]".
 * Paginação: Implementada em todos os endpoints de listagem (GET /) utilizando a biblioteca fastapi-pagination (parâmetros limit e offset).
 * Orquestração: Configuração completa com Docker Compose e Alembic para migrações assíncronas.
📁 Estrutura do Repositório
/apiWorkoutPython
├── .env.example              # Exemplo de arquivo de variáveis de ambiente
├── .gitignore                # Arquivo de ignorados do Git
├── Dockerfile                # Define a imagem da API
├── docker-compose.yml        # Orquestra os serviços (API e PostgreSQL)
├── Makefile                  # Comandos de automação (docker, alembic, run)
├── README.md                 # Este arquivo
├── alembic.ini               # Configuração do Alembic
├── requirements.txt          # Lista de dependências Python
├── migrations/               # Scripts de migração do banco de dados
│   ├── env.py                # Script de ambiente do Alembic (configurado para Async)
│   └── versions/             # Pasta de scripts de migração gerados
└── src/
    ├── core/                 # Módulos centrais (configs, database, exceptions)
    ├── main.py               # Ponto de entrada da aplicação FastAPI
    ├── models/               # Modelos SQLAlchemy ORM
    ├── routers/              # Rotas da API (lógica de negócio e tratamento de exceções)
    └── schemas/              # Schemas Pydantic (validação e tipagem de dados)

🛠 Guia de Execução
Pré-requisitos
 * Docker e Docker Compose: Essenciais para rodar o banco de dados.
 * Python 3.11+: Recomendado.
1. Configuração
Crie o arquivo .env (opcional, mas recomendado) na raiz do projeto:
DATABASE_URL=postgresql+asyncpg://workout:workout@localhost:5432/workout_api

2. Iniciar o Banco de Dados
Suba o container do PostgreSQL usando o comando make:
make run-docker
# Inicia o serviço 'postgres' em background.

3. Instalar Dependências e Migrações
Instale as dependências e crie/aplique a estrutura do banco:
# Instala as dependências Python
pip install -r requirements.txt

# Cria o script de migração (o nome da migration é "initial_setup")
make create-migrations d="initial_setup" 

# Aplica as migrações ao banco de dados (cria as tabelas)
make run-migrations

4. Rodar a API
Execute a aplicação FastAPI localmente:
make run

A API estará disponível em: http://127.0.0.1:8000/docs (Documentação Swagger UI)
📌 Exemplos de Uso no Postman / Docs
| Endpoint | Método | Descrição e Observações |
|---|---|---|
| /atletas | POST | Regra 303: Tente cadastrar o mesmo CPF duas vezes para ver o tratamento de exceção. |
| /atletas | GET | Query Params & Paginação: Use ?limit=5&offset=0&nome=joao ou ?cpf=12345678901. |
| /categorias | GET | Paginação: Use ?limit=3&offset=0. |


