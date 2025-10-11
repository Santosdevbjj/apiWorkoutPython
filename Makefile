# ==========================
# 📌 Variáveis Globais
# ==========================
DOCKER_COMPOSE := docker-compose
DOCKER_COMPOSE_PROD := docker-compose -f docker-compose.yml -f docker-compose.prod.yml
PYTHON := python3
APP_SERVICE := app
DB_SERVICE := db

# ==========================
# 🧪 Desenvolvimento
# ==========================

## Subir o ambiente de desenvolvimento com reload
dev-up:
	@echo "🚀 Subindo ambiente de desenvolvimento..."
	$(DOCKER_COMPOSE) up --build

## Derrubar o ambiente de desenvolvimento
dev-down:
	@echo "🛑 Derrubando ambiente de desenvolvimento..."
	$(DOCKER_COMPOSE) down

## Restart do ambiente de desenvolvimento
dev-restart: dev-down dev-up

## Acessar o container do app em modo interativo
dev-shell:
	$(DOCKER_COMPOSE) exec $(APP_SERVICE) bash

## Instalar dependências dentro do container de desenvolvimento
dev-install:
	$(DOCKER_COMPOSE) exec $(APP_SERVICE) pip install -r requirements.txt

# ==========================
# 🏭 Produção
# ==========================

## Subir o ambiente de produção com Gunicorn
prod-up:
	@echo "🚀 Subindo ambiente de produção..."
	$(DOCKER_COMPOSE_PROD) up -d --build

## Derrubar o ambiente de produção
prod-down:
	@echo "🛑 Derrubando ambiente de produção..."
	$(DOCKER_COMPOSE_PROD) down

## Restart da aplicação em produção
prod-restart: prod-down prod-up

## Ver logs em produção
prod-logs:
	$(DOCKER_COMPOSE_PROD) logs -f $(APP_SERVICE)

## Acessar shell do app em produção
prod-shell:
	$(DOCKER_COMPOSE_PROD) exec $(APP_SERVICE) bash

# ==========================
# 🗃️ Banco de Dados / Alembic
# ==========================

## Criar nova migration Alembic
migrate-create:
	@if [ -z "$(d)" ]; then \
		echo "❌ ERRO: Informe o nome da migration com d=\"nome\""; \
		exit 1; \
	fi
	$(DOCKER_COMPOSE) exec $(APP_SERVICE) alembic revision --autogenerate -m "$(d)"

## Aplicar migrations
migrate-up:
	$(DOCKER_COMPOSE) exec $(APP_SERVICE) alembic upgrade head

## Desfazer última migration (downgrade)
migrate-down:
	$(DOCKER_COMPOSE) exec $(APP_SERVICE) alembic downgrade -1

## Ver histórico de migrations
migrate-history:
	$(DOCKER_COMPOSE) exec $(APP_SERVICE) alembic history

# ==========================
# 🧪 Testes e Qualidade
# ==========================

## Rodar testes com Pytest no container
test:
	@echo "🧪 Executando testes..."
	$(DOCKER_COMPOSE) exec $(APP_SERVICE) pytest -v

## Rodar lint com flake8
lint:
	@echo "🔍 Rodando flake8..."
	$(DOCKER_COMPOSE) exec $(APP_SERVICE) flake8 app

## Rodar formatação com black
format:
	@echo "✨ Formatando código com Black..."
	$(DOCKER_COMPOSE) exec $(APP_SERVICE) black app tests

## Rodar isort para ordenar imports
imports:
	@echo "📚 Organizando imports com isort..."
	$(DOCKER_COMPOSE) exec $(APP_SERVICE) isort app tests

# ==========================
# 🚀 Deploy / CI
# ==========================

## Simular pipeline de deploy (testes + lint + build)
deploy-check:
	@echo "🏗️ Verificando código antes do deploy..."
	make lint
	make test

## Deploy produção (build + migração + restart)
deploy:
	@echo "🚀 Realizando deploy..."
	make prod-up
	$(DOCKER_COMPOSE_PROD) exec $(APP_SERVICE) alembic upgrade head

# ==========================
# 🧹 Limpeza
# ==========================

## Remover containers, volumes e imagens não utilizadas
clean:
	@echo "🧹 Limpando containers e volumes..."
	$(DOCKER_COMPOSE) down -v --remove-orphans
	docker system prune -f

## Recriar tudo do zero (dev)
rebuild-dev: clean dev-up

## Recriar tudo do zero (prod)
rebuild-prod: clean prod-up

# ==========================
# 📝 Ajuda
# ==========================
help:
	@echo "📚 Comandos disponíveis:"
	@grep -E '^[a-zA-Z0-9_.-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-30s\033[0m %s\n", $$1, $$2}'
