# ============================================
# 🏋️‍♂️ API Workout Python - Makefile
# ============================================

# Carrega variáveis do arquivo .env
include .env
export $(shell sed 's/=.*//' .env)

# Nome do serviço da aplicação definido em .env
APP_SERVICE := $(DOCKER_APP_SERVICE)
PYTHON := python
 
# =========================
# 🐳 COMANDOS DOCKER
# =========================

## 🟢 Subir os containers da aplicação (modo dev)
up:
	docker-compose up -d

## 🛑 Parar e remover os containers
down:
	docker-compose down

## 🔄 Subir e recompilar a imagem
build:
	docker-compose up -d --build

## 🔍 Ver logs da aplicação
logs:
	docker-compose logs -f $(APP_SERVICE)

## 🧹 Remover volumes e cache (cuidado!)
clean:
	docker-compose down -v --remove-orphans
	docker system prune -f

# =========================
# 🧰 AMBIENTE LOCAL
# =========================

## 🐍 Instalar dependências no ambiente virtual local
install:
	$(PYTHON) -m venv venv
	. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

## 🚀 Rodar aplicação localmente (sem Docker)
run:
	uvicorn app.main:app --host $(APP_HOST) --port $(APP_PORT) --reload

# =========================
# 🧪 TESTES
# =========================

## 🧪 Rodar todos os testes com Pytest
test:
	docker-compose exec $(APP_SERVICE) pytest -v

## 🧪 Testes com cobertura
coverage:
	docker-compose exec $(APP_SERVICE) pytest --cov=app --cov-report=term-missing

# =========================
# 🛢️ MIGRAÇÕES (ALEMBIC)
# =========================

## 📝 Criar uma nova migration: make migrate m="mensagem"
migrate:
ifndef m
	$(error ❌ Você precisa passar a descrição da migration. Ex: make migrate m="create atleta table")
endif
	docker-compose exec $(APP_SERVICE) alembic revision --autogenerate -m "$(m)"

## ⬆️ Aplicar migrations
upgrade:
	docker-compose exec $(APP_SERVICE) alembic upgrade head

## ⬇️ Reverter última migration
downgrade:
	docker-compose exec $(APP_SERVICE) alembic downgrade -1

# =========================
# 🧼 FORMATAÇÃO / LINT
# =========================

## 🧼 Formatar código com Black e isort
format:
	docker-compose exec $(APP_SERVICE) black app tests
	docker-compose exec $(APP_SERVICE) isort app tests

## 🔍 Verificar lint (sem alterar arquivos)
lint:
	docker-compose exec $(APP_SERVICE) black --check app tests
	docker-compose exec $(APP_SERVICE) isort --check-only app tests
	docker-compose exec $(APP_SERVICE) flake8 app tests

# =========================
# 🧠 AJUDA
# =========================

## 📜 Exibir todos os comandos disponíveis
help:
	@echo "============================================"
	@echo " 🏋️‍♂️ API Workout Python - Comandos Makefile"
	@echo "============================================"
	@echo "🐳 Docker:"
	@echo "  make up              - Subir containers"
	@echo "  make down            - Parar containers"
	@echo "  make build           - Recompilar imagem e subir"
	@echo "  make logs            - Acompanhar logs da aplicação"
	@echo "  make clean           - Remover containers, volumes e cache"
	@echo ""
	@echo "🐍 Ambiente Local:"
	@echo "  make install         - Instalar dependências no venv"
	@echo "  make run             - Rodar API localmente (sem Docker)"
	@echo ""
	@echo "🧪 Testes:"
	@echo "  make test            - Rodar testes com Pytest"
	@echo "  make coverage        - Rodar testes com relatório de cobertura"
	@echo ""
	@echo "🛢️ Migrações Alembic:"
	@echo "  make migrate m=\"msg\"  - Criar nova migration"
	@echo "  make upgrade         - Aplicar migrations"
	@echo "  make downgrade       - Reverter última migration"
	@echo ""
	@echo "🧼 Formatação e Lint:"
	@echo "  make format          - Formatar código com black + isort"
	@echo "  make lint            - Rodar linters e verificações"
	@echo ""
	@echo "🧠 Ajuda:"
	@echo "  make help            - Exibir esta ajuda"
