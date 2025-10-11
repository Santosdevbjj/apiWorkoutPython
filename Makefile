.PHONY: run run-docker create-migrations run-migrations install test

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

run-docker:
	docker-compose up --build -d

create-migrations:
	alembic revision --autogenerate -m "$(m)"

run-migrations:
	alembic upgrade head

install:
	pip install -r requirements.txt

test:
	pytest -q
